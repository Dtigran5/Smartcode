#link -> https://leetcode.com/problems/reverse-integer/description/
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = int(str(x)[::-1])
    
    if reversed_x > 2**31 - 1:
        return 0
    return sign * reversed_x

print(reverse_integer(123))   
print(reverse_integer(-123))  
print(reverse_integer(120))  
