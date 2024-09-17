#link -> https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def open_or_senior(data):
    categories = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories

input_data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output_data = open_or_senior(input_data)
print(output_data)
