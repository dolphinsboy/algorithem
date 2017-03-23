def is_even(k):
    while k > 1:
        k = k - 2
    if k == 0:
        return False
    elif k == 1:
        return True

def is_even_bit(k):
    return True if k & 1 else False

print is_even(10)
print is_even(11)

print is_even_bit(10)
print is_even_bit(11)



