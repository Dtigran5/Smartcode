def elements_sum(arr, d = 0):
    total_sum = 0
    length = len(arr)
    
    for i in range(length):
        if len(arr[i]) >= length - i:
            total_sum += arr[i][length - i - 1]
        else:
            total_sum += d
            
    return total_sum

arrays = [[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]]
result = elements_sum(arrays)
print(result)  