#link -> https://www.codewars.com/kata/5d9f95424a336600278a9632
def powers(n):
    result = []
    power = 1
    while n > 0:
        if n & power:
            result.append(power)
            n -= power  
        power <<= 1
    return sorted(result)

print(powers(6))  
print(powers(10))  
print(powers(1))  
print(powers(2))  
print(powers(4)) 
print(powers(5))
print(powers(7))
print(powers(11))
