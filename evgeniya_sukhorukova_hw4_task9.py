a = [1, 'two', 3, (4, 5)]
b = [6, 'seven', 9, (10, 11)]
c = bool(set(a) & set(b))
print(c)
