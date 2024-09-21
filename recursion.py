def some(x):
    print(x)
    if x < 10:
        return x + some(x + 1)
    if x > 10:
        return 1


print(some(5))
