#link ->  https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
def longest_common_prefix(arr1, arr2):
    max_length = 0
    
    for x in arr1:
        for y in arr2:
            common_length = 0
            str_x, str_y = str(x), str(y)
            min_length = min(len(str_x), len(str_y))
            
            for i in range(min_length):
                if str_x[i] == str_y[i]:
                    common_length += 1
                else:
                    break
            
            max_length = max(max_length, common_length)
    
    return max_length

arr1 = [1, 10, 100]
arr2 = [1000]
print(longest_common_prefix(arr1, arr2))  

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(longest_common_prefix(arr1, arr2))  

arr1 = [5,25,35]
arr2 = [525, 625, 2552]
print(longest_common_prefix(arr1,arr2))