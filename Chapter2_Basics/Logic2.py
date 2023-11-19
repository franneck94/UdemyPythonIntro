# or := logische oder
# and := logische und
# not := logische verneinung

my_age = 28

if my_age < 3:
    print("You are a baby")
elif my_age < 12:
    print("You are a teenager")
elif my_age < 18:
    print("You are a child")
elif my_age < 67:
    print("You are an adult!")
else:
    print("You are a pensioneer!")

my_bank_account = 900.0

if (my_bank_account < 0.0) or (my_bank_account > 1000.0):
    print("If")
else:
    print("Else")

if (my_bank_account > 0.0) and (my_bank_account < 1000.0):
    print("If")
else:
    print("Else")
