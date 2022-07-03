my_list = [1, 3, 6, 10]

# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)


def generator(my_list):
    for x in my_list:
        yield x**2

for i in generator(my_list):
    print(i)