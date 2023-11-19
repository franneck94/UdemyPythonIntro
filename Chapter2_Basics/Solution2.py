"""Exercise 2:
1.)
Write code that takes a list of integer numbers and one
integer number "a" and prints the index of the number
if its in the list.

2.)
Write code that takes two integers (x, y) computes the following:
Sum up all integer numbers from x (inclusive) to y (non-inclusive)
with a step width of 2.
"""

# exercise1
lst = [1, 2, 3]
a = 3
if a in lst:
    print(lst.index(a))


# exercise2
x = 2
y = 10

result = 0
for i in range(x, y, 2):
    result += i
print(result)
