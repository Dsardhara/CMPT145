#Calculates 1 − 2 + 3 − 4 + 5 · · · n
def alt_sum(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return -n + alt_sum(n - 1)
    else:
        return n + alt_sum(n - 1)


print(alt_sum(3))
