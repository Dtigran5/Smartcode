import random

def generate_bingo_card():
    card = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    card['N'][2] = 0  
    return card

def display_bingo_card(card):
    print("\n B     I     N     G     O")
    for i in range(5):
        print(f"\n {card['B'][i]:<5} {card['I'][i]:<5} {card['N'][i]:<5} {card['G'][i]:<5} {card['O'][i]:<5}")
def check_bingo(card):
    for i in range(5):
        if all(card[col][i] == 0 for col in card):  # Check vertical
            return True
    for row in card.values():
        if all(num == 0 for num in row):  # Check horizontal
            return True
    if all(card['B'][i] == 0 for i in range(5)):  # Check diagonal
        return True
    if all(card['B'][4-i] == 0 for i in range(5)):  # Check other diagonal
        return True
    return False

def simulate_bingo_game():
    calls = [f"{letter}{num}" for letter in "BINGO" for num in range(1, 16)]
    random.shuffle(calls)
    card = generate_bingo_card()
    display_bingo_card(card) 
    calls_made = 0
    for call in calls:
        letter = call[0]
        number = int(call[1:])
        if number in card[letter]:
            card[letter][card[letter].index(number)] = 0
        calls_made += 1
        if check_bingo(card):
            return calls_made
    return calls_made

if __name__ == "__main__":
    results = []
    for _ in range(1000):
        results.append(simulate_bingo_game())
    print(f"Minimum calls: {min(results)}")
    print(f"Maximum calls: {max(results)}")
    print(f"Average calls: {sum(results) / len(results)}")
