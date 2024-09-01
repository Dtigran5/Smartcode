numbers = []
while True:
    nums = input("Enter an integer (or leave blank to finish): ")
    if nums == "":
        break
    numbers.append(int(nums))

negatives = [num for num in numbers if num < 0]
zeros = [num for num in numbers if num == 0]
positives = [num for num in numbers if num > 0]

for num in negatives + zeros + positives:
    print(num)
