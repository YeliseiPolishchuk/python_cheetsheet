list_comprehension = [x for x in range(1, 5 + 1)]
set_comprehension = {x ** 2 for x in list_comprehension}
print(list_comprehension, '\n', set_comprehension)
dict_comprehension = {x: x**2 for x in list_comprehension}
print('\n', dict_comprehension)