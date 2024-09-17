#link -> https://www.codewars.com/kata/594c6ad5d909ca19e200002f/
def byte_to_set(byte):
    binary_str = f'{byte:08b}'
    result_set = {index for index, bit in enumerate(binary_str) if bit == '1'}
    return result_set

print(byte_to_set(0b01100101))
print(byte_to_set(0b10101010))
print(byte_to_set(0b11100000))