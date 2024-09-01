alphabet = 'abcdefg'

# 1
print(''.join([char for char in alphabet]))

# 2
print(''.join([alphabet[i] for i in range(len(alphabet) - 1, -1, -1)]))

# 3
print(''.join([alphabet[i] for i in range(0, len(alphabet), 2)]))

# 4
print(''.join([alphabet[i] for i in range(1, len(alphabet), 2)]))

# 5
print(''.join([alphabet[i] for i in range(2)]))

# 6
print(''.join([alphabet[i] for i in range(len(alphabet) - 2, len(alphabet))]))

# 7
print(''.join([alphabet[i] for i in range(3, 4)]))

# 8
print(''.join([alphabet[i] for i in range(len(alphabet) - 3, len(alphabet))]))

# 9
print(''.join([alphabet[i] for i in range(3, 5)]))

# 10
print(''.join([alphabet[i] for i in range(4, 2, -1)]))
