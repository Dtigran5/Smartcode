import random

def flip_coin():
    return 'H' if random.random() < 0.5 else 'T'

def simulate_flips():
    flips = []
    consecutive_count = 1
    previous_flip = flip_coin()
    flips.append(previous_flip)
    
    while consecutive_count < 3:
        current_flip = flip_coin()
        flips.append(current_flip)
        
        if current_flip == previous_flip:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        previous_flip = current_flip
    
    print(" ".join(flips), f"- {len(flips)} flips")
    return len(flips)

def main():
    total_flips = 0
    simulations = 10
    
    print("Simulating 10 series of coin flips...")
    for i in range(simulations):
        flips_needed = simulate_flips()
        total_flips += flips_needed
    
    average_flips = total_flips / simulations
    print(f"\nAverage number of flips needed: {average_flips:.2f}")

if __name__ == "__main__":
    main()
