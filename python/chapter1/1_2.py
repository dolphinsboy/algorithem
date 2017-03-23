def is_even(k):
    while k > 1:
        k = k - 2
    if k == 0:
        return False
    elif k == 1:
        return True

print is_even(10)
print is_even(11)



