import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    rolls = 1000
    results = [0] * 13  

    for _ in range(rolls):
        total = roll_dice()
        results[total] += 1

    print(f"{'Total':<10}{'Simulated Percent':<20}{'Expected Percent':<20}")
    expected_percentages = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    for total in range(2, 13):
        simulated_percent = (results[total] / rolls) * 100
        expected_percent = expected_percentages[total]
        print(f"{total:<10}{simulated_percent:<20.2f}{expected_percent:<20.2f}")

if __name__ == "__main__":
    main()
