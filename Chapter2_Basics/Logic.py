# == (Equal)
# < (Less than)
# > (Greater than)
# != (Not equal)
# <= (Less or equal than)
# >= (Greater or equal than)

my_bank_account = 130.0

i_am_broke = my_bank_account <= 0.0

if i_am_broke:
    print("I am broke!")
else:
    print("I am not broke!")

gpu_price = 800.0
my_bank_account = my_bank_account - gpu_price

i_am_broke = my_bank_account <= 0.0

if i_am_broke:
    print("I am broke!")
else:
    print("I am not broke!")

my_age = 28

if my_age < 18:
    print("You are a child!")
elif my_age < 67:
    print("You are an adult!")
else:
    print("You are a pensioneer!")
