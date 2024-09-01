N = int(input("Enter the length of the list: "))
result = [1 if i % 2 == 0 else i % 5 for i in range(N)]
print("Result:", result)
