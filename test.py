x = [2, 3, 4, 5, 6]
y = []
for v in x:
    y += [v * 5]
    print(v, y)
print(x)
print(y)

#
#
# assert x == [2, 3, 4, 5, 6]
# assert y == [10, 15, 20, 25, 30]
#
# y = [v * 5 for v in x]  # List comprehension
# assert x == [2, 3, 4, 5, 6]
# assert y == [10, 15, 20, 25, 30]
