a = (1, 2, 3)
b = list(a)
last_item = len(b) - 1
b.remove(b[last_item])
c = tuple(b)
print(c)
