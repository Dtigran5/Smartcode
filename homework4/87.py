def calculate_shipping(num_items):
    if num_items < 1:
        return 0
    elif num_items == 1:
        return 10.95
    else:
        return 10.95 + (num_items - 1) * 2.95

def main():
    num_items = int(input("Enter the number of items purchased: "))
    shipping_charge = calculate_shipping(num_items)
    print(f"The shipping charge for your order is: ${shipping_charge:.2f}")

if __name__ == "__main__":
    main()
