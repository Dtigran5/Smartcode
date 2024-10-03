def sum_numbers():
    total_sum = 0.0
    
    while True:
        user_input = input("Enter a number (or press Enter to exit): ")
        
        if user_input == "":
            break
        
        try:
            number = float(user_input)
            total_sum += number
            print(f"Current sum: {total_sum}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"Final sum: {total_sum}")

if __name__ == "__main__":
    sum_numbers()
