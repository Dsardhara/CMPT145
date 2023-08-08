# Determines if n is evenly divisible by m.

def even_div(n,m):
    # if n%m==0:
    #     return True
    # else:
    #     return False
    if n<m:
        return False
    elif n==m:
        return True
    else:
        return even_div(n-m,m)
print(even_div(10,2))

