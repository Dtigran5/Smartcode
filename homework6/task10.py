#link -> https://www.codewars.com/kata/586bca7fa44cfc833e00005c
def create_array_of_tiers(num):
    return [str(num)[:i] for i in range(1, len(str(num)) + 1)]

print(create_array_of_tiers(420))   
print(create_array_of_tiers(2017))   
print(create_array_of_tiers(2010))   
print(create_array_of_tiers(4020))   
print(create_array_of_tiers(80200))  
