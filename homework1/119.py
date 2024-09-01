numbers = []
while True:
    user_input = input("Enter a number (or press Enter to skip): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Average: {average:.2f}")

    below_average = [num for num in numbers if num < average]
    equal_average = [num for num in numbers if num == average]
    above_average = [num for num in numbers if num > average]

    print("\nNumbers below average:")
    print(below_average)

    print("\nNumbers equal to average:")
    print(equal_average)

    print("\nNumbers above average:")
    print(above_average)
else:
    print("No numbers were entered.")
