#link -> https://www.codewars.com/kata/56b7f2f3f18876033f000307
def in_asc_order(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

print(in_asc_order([1,2,4,7,19])) 
print(in_asc_order([1,2,3,4,5])) 
print(in_asc_order([1,6,10,18,2,4,20])) 
print(in_asc_order([9,8,7,6,5,4,3,2,1])) 
