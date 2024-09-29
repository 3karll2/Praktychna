def sort(list):
    element = list(set(input_list))

    int_sort = sorted([x for x in element if isinstance(x, (int, float))])
    str_sort = [x for x in element if not isinstance(x, (int, float))]

    return int_sort + str_sort


list = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']
result = sort(list)

print(result)
