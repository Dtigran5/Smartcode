def calculate_fare(distance_km):
    base_fare = 4.00
    cost_per_140m = 0.25
    distance_m = distance_km * 1000
    fare = base_fare + (distance_m / 140) * cost_per_140m
    return fare

if __name__ == "__main__":
    distance = float(input("Enter the distance travelled in kilometers: "))
    total_fare = calculate_fare(distance)
    print(f"The total fare for {distance} km is: ${total_fare:.2f}")
