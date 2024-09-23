def print_params (a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print()
values_list = ('Bosh', 232, True)
print_params(*values_list)
print()
values_dict = {'a': 'max', 'b': 'min', 'c': 33}
print_params(**values_dict)
print()
values_list_2 = [3.14, 'Песня']
print_params(*values_list_2, 24680)






