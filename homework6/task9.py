#link -> https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"

print(high_and_low("1 2 3 4 5"))  
print(high_and_low("1 2 -3 4 5")) 
print(high_and_low("1 9 3 4 -5")) 
