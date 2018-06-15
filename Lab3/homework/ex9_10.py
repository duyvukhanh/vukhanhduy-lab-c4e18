def get_even_list(l):
    new_list = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new_list.append(l[i])
    return new_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")