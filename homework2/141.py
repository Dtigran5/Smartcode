def number_to_words(n):
    if n < 0 or n > 999:
        return "Number out of range"

    ones = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen"
    }

    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    if n < 20:
        return ones[n]
    elif n < 100:
        ten, below_ten = divmod(n, 10)
        return tens[ten * 10] + ('' if below_ten == 0 else ' ' + ones[below_ten])
    else:
        hundred, below_hundred = divmod(n, 100)
        return ones[hundred] + " hundred" + ('' if below_hundred == 0 else ' ' + number_to_words(below_hundred))
    
number = int(input("Enter an integer between 0 and 999: "))
print(number_to_words(number))



