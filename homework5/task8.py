def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    
    tribonacci_sequence = signature[:]
    for i in range(3, n):
        next_value = tribonacci_sequence[i-1] + tribonacci_sequence[i-2] + tribonacci_sequence[i-3]
        tribonacci_sequence.append(next_value)
    
    return tribonacci_sequence

signature1 = [1, 1, 1]
n1 = 10
print(tribonacci(signature1, n1)) 

signature2 = [0, 0, 1]
n2 = 10
print(tribonacci(signature2, n2))  
