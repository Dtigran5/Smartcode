#link -> https://leetcode.com/problems/longest-palindromic-substring/description/
def longest_palindrome(s):
    if len(s) < 1:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]

def expand_around_center(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

s = "babad"
result = longest_palindrome(s)
print(result)

s = "cbbd"
result = longest_palindrome(s)
print(result)

