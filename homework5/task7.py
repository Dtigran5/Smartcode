def first_n_smallest(arr, n):
    if n > len(arr):
        raise ValueError("n cannot be greater than the length of the list")

    smallest = sorted(arr)[:n]
    
    result = []
    for num in arr:
        if num in smallest:
            result.append(num)
            smallest.remove(num)
        if len(result) == n:
            break
            
    return result

print(first_n_smallest([1, 2, 3, 4, 5], 3)) 
print(first_n_smallest([5, 4, 3, 2, 1], 3))  
print(first_n_smallest([1, 2, 3, 4, 1], 3))  
print(first_n_smallest([1, 2, 3, -4, 0], 3))  
print(first_n_smallest([1, 2, 3, 4, 5], 0))