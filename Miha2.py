class Miha:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_course(self):
        if self.birth_year:
            course = 2025 - (self.birth_year + 16) + 1
            return max(course, 1)
        return None

    def get_full_name_list(self):
        return [self.name, self.surname]

class Student(Miha):
    def __init__(self, name=None, surname=None, birth_year=None,
                 university=None, specialty=None, average_grade=None):
        super().__init__(name, surname, birth_year)
        self.university = university
        self.specialty = specialty
        self.average_grade = average_grade

    def is_eligible_for_scholarship(self):
        return self.average_grade >= 70

    def _format_profile(self):
        return f"{self.name} {self.surname}, {self.specialty} в {self.university}, середній бал: {self.average_grade}"


student = Student("Михайло", "Оніщук", 2008, "ТФК ЛНТУ", "Інформатика", 71)

print("Курс:", student.get_course())
print("ПІБ:", student.get_full_name_list())
print("Стипендія:", "Так" if student.is_eligible_for_scholarship() else "Ні")
print("Профіль:", student._format_profile())