import random

N = 10
random_list = [random.randint(0, 2) for _ in range(N)]
print("List before compression:", random_list)
compressed_list = [num for num in random_list if num != 0]
print("List after compression:", compressed_list)
