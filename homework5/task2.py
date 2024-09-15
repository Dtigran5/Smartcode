def grid_index(grid, indexes):
    result = ''
    for index in indexes:
        row = (index - 1) // len(grid)
        col = (index - 1) % len(grid)
        result += grid[row][col]
    return result

grid = [['m', 'y', 'e'], 
        ['x', 'a', 'm'], 
        ['p', 'l', 'e']]

indexes = [1, 3, 5, 8]
output = grid_index(grid, indexes)
print(output)  