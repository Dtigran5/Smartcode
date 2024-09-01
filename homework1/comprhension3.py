import random

first_team = [random.uniform(5, 10) for _ in range(20)]
second_team = [random.uniform(5, 10) for _ in range(20)]

winners = [max(pair) for pair in zip(first_team, second_team)]

print("First team:", first_team)
print("Second team:", second_team)
print("Winners:", winners)
