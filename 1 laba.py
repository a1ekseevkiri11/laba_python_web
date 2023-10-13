def recursia(n):
    if n == 1:
        return -10
    elif n == 2:
        return 2
    return abs(recursia(n - 2)) - 6 * recursia(n - 1)

print(recursia(4))