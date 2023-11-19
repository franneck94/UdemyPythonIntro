dct = {"Jan": 27, "Peter": 33}
lst = [1, 2, 3]


try:
    print(lst[3])
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
