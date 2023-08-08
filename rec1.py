def square(n,r):
    if n<1:
        return 1
    else:
        return r* square(n - 1, r)
print(square(3,2))
