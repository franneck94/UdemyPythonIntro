l1 = ["a", "b", "a", "c"]
print(l1)


s1 = set(l1)
print(s1)


s2 = {"a", "d"}
print(s2)


print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
