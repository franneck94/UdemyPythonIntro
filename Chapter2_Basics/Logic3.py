my_name_is_jan = True
my_name_is_ben = False


print(not my_name_is_jan)
print(not my_name_is_ben)

my_var = 10

if my_var < 100 and my_var > 0:  # (0, 100)
    print("yes")
else:
    print("no")

if not(my_var < 100 and my_var > 0):  # (-inf, 0] or [100, inf)
    print("yes")
else:
    print("no")

if my_var >= 100 or my_var <= 0:  # (-inf, 0] or [100, inf)
    print("yes")
else:
    print("no")
