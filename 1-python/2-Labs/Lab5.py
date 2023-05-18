#import BIT_MATH
def clear_bit(n, index):   
    mask = ~(1 << index)
    return n & mask
mask=1

print(mask)
clear_bit(mask,0)
print(mask)