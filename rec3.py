
# Determines if an integer n is even

def even(n):
    if n == 0:
        return True
    elif n==1:
        return False
    else:
        return even(n-2)

print(even(6))
