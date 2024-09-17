#link -> https://www.codewars.com/kata/586f6741c66d18c22800010a
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    return sum(i for i in range(begin, end + 1, step) if i <= end)

print(sequence_sum(2, 2, 2))  
print(sequence_sum(2, 6, 2))  
print(sequence_sum(1, 5, 1))  
print(sequence_sum(1, 5, 3))  
