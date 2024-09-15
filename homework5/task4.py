def moving_average(values, n):
    if n == 0 or len(values) < n:
        return None
    
    averages = []
    for i in range(len(values) - n + 1):
        window = values[i:i + n]
        averages.append(sum(window) / n)
    
    return averages

values = [1, 2, 3, 4, 5]
window_size = 3
result = moving_average(values, window_size)
print(result)
