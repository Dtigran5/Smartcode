def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

print(search_insert([1, 3, 5, 6], 5))  
print(search_insert([1, 3, 5, 6], 2))  
print(search_insert([1, 3, 5, 6], 7))  

