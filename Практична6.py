import telebot

TOKEN = "7650499504:AAFZkcgGVbq_mA4m6k6GXVkCsz5de9cfZqE"

bot = telebot.TeleBot(TOKEN)

sizes = {
    '1': "Маленька (200 мл)",
    '2': "Середня (350 мл)",
    '3': "Велика (500 мл)"
}

shapes = {
    '1': "Кругла",
    '2': "Квадратна",
    '3': "З нестандартним дизайном"
}

patterns = {
    '1': "Квіти 🌸",
    '2': "Гори ⛰️",
    '3': "Космос 🌌",
    '4': "Тварини 🐾",
    '5': "Абстракція 🎨",
    '6': "Ваш текст 🖋️ (напишіть у наступному повідомлені)"
}

user_choices = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    user_choices[message.chat.id] = {}
    bot.send_message(
        message.chat.id,
        "Привєт! Цей бот допоможе створити дизайн для чашки, наприклад, на подарунок. Спочатку виберемо розмір:\n"
        "1. Маленька (200 мл)\n"
        "2. Середня (350 мл)\n"
        "3. Велика (500 мл)\n"
        "Вкажіть номер розміру."
    )

@bot.message_handler(func=lambda message: message.chat.id in user_choices and 'size' not in user_choices[message.chat.id])
def choose_size(message):
    size_choice = message.text.strip()

    if size_choice in sizes:
        user_choices[message.chat.id]['size'] = sizes[size_choice]
        user_choices[message.chat.id]['size_code'] = size_choice
        bot.send_message(
            message.chat.id,
            f"Ви обрали розмір: {sizes[size_choice]}.\n\n"
            "Тепер виберіть форму чашки:\n"
            "1. Кругла\n"
            "2. Квадратна\n"
            "3. З нестандартним дизайном\n"
            "Вкажіть номер форми."
        )
    else:
        bot.send_message(message.chat.id, "Невірний вибір. Вкажіть номер розміру (1, 2 або 3).")

@bot.message_handler(func=lambda message: message.chat.id in user_choices and 'size' in user_choices[message.chat.id] and 'shape' not in user_choices[message.chat.id])
def choose_shape(message):
    shape_choice = message.text.strip()

    if shape_choice in shapes:
        user_choices[message.chat.id]['shape'] = shapes[shape_choice]
        user_choices[message.chat.id]['shape_code'] = shape_choice
        bot.send_message(
            message.chat.id,
            f"Ви обрали форму: {shapes[shape_choice]}.\n\n"
            "Тепер вибирайте візерунок для чашки:\n"
            "1. Квіти\n"
            "2. Гори\n"
            "3. Космос\n"
            "4. Тварини\n"
            "5. Абстракція\n"
            "6. Ваш Дизайн або Текст (напишіть у наступному повідомленні).\n"
            "Вкажіть номер візерунка."
        )
    else:
        bot.send_message(message.chat.id, "Невірний вибір. Вкажіть номер форми (1, 2 або 3).")

@bot.message_handler(func=lambda message: message.chat.id in user_choices and 'shape' in user_choices[message.chat.id] and 'pattern' not in user_choices[message.chat.id])
def choose_pattern(message):
    pattern_choice = message.text.strip()

    if pattern_choice in patterns:
        if pattern_choice == '6':
            user_choices[message.chat.id]['pattern'] = "Ваш текст (напишіть у наступному повідомленні)"
            bot.send_message(message.chat.id, "Напишіть текст, який ви хочете нанести на чашку.")
        else:
            user_choices[message.chat.id]['pattern'] = patterns[pattern_choice]
            user_choices[message.chat.id]['pattern_code'] = pattern_choice
            confirm_order(message)
    else:
        bot.send_message(message.chat.id, "Невірний вибір. Вкажіть номер візерунка (1, 2, 3, 4, 5 або 6).")

@bot.message_handler(func=lambda message: message.chat.id in user_choices and user_choices[message.chat.id].get('pattern') == "Ваш текст (напишіть у наступному повідомленні)")
def add_custom_text(message):
    user_choices[message.chat.id]['pattern'] = f"Ваш текст: {message.text}"
    user_choices[message.chat.id]['pattern_code'] = 'custom'
    confirm_order(message)

def confirm_order(message):
    choices = user_choices[message.chat.id]
    bot.send_message(
        message.chat.id,
        f"Ваше замовлення:\n"
        f"Розмір чашки: {choices['size']}\n"
        f"Форма чашки: {choices['shape']}\n"
        f"Візерунок: {choices['pattern']}\n\n"
        "Якщо все вірно, натисніть /confirm для підтвердження або /cancel для скасування замовлення."
    )

@bot.message_handler(commands=['confirm'])
def confirm(message):
    if message.chat.id in user_choices and user_choices[message.chat.id]:
        choices = user_choices[message.chat.id]
        bot.send_message(
            message.chat.id,
            f"Замовлення підтверджено!\n\n"
            f"Розмір чашки: {choices['size']}\n"
            f"Форма чашки: {choices['shape']}\n"
            f"Візерунок: {choices['pattern']}\n"
            "Дякуємо за замовлення! Ми зв'яжемося з вами для уточнення деталей."
        )
        user_choices[message.chat.id] = {}
    else:
        bot.send_message(message.chat.id, "Немає активного замовлення. Почніть нове замовлення командою /start.")

@bot.message_handler(commands=['cancel'])
def cancel(message):
    if message.chat.id in user_choices and user_choices[message.chat.id]:
        user_choices[message.chat.id] = {}
        bot.send_message(message.chat.id, "Замовлення скасовано.")
    else:
        bot.send_message(message.chat.id, "Немає активного замовлення для скасування.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Вибачте, щось пішло не так")

bot.polling(none_stop=True)
