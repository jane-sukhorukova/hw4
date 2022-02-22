words = {item for item in input("Enter words via 'comma ' : ").split(', ')}
result = sorted(words)
print(*result, sep=', ')
