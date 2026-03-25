s1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
s2 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print(s1.union(s2))
print(s1.intersection(s2))
s1.pop
print(s1)
s2.pop
print(s2)
s1.update([13, 14])
print(s1)
s2.update([1, 22])
print(s2)
s1.remove(2)
print(s1)
s2.remove(10)
print(s2)
print(s1.difference(s2))
