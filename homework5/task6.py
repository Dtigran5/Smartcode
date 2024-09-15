def total(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(arr[i] for i in range(len(arr)) if is_prime(i))

array = [10, 20, 30, 40, 50]
result = total(array)
print(result) 
