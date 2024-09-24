#link -> https://leetcode.com/problems/string-to-integer-atoi/description/
def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0

    sign = 1
    index = 0
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    result *= sign
    int_min, int_max = -2**31, 2**31 - 1
    if result < int_min:
        return int_min
    if result > int_max:
        return int_max
    return result

s = "42"
result = myAtoi(s)
print(result)

s = " -042"
result = myAtoi(s)
print(result)

s = "1337c0d3"
result = myAtoi(s)
print(result)

s = "0-1"
result = myAtoi(s)
print(result)

s = "words and 987"
result = myAtoi(s)
print(result)