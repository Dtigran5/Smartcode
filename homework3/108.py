def convert_volume(units, unit):
    conversions = {
        'cup': 48,
        'tablespoon': 3,
        'teaspoon': 1
    }
    
    if unit not in conversions:
        return "Invalid unit"
    
    total_teaspoons = units * conversions[unit]
    
    cups = total_teaspoons // conversions['cup']
    total_teaspoons %= conversions['cup']
    
    tablespoons = total_teaspoons // conversions['tablespoon']
    total_teaspoons %= conversions['tablespoon']
    
    teaspoons = total_teaspoons
    
    result = []
    if cups:
        result.append(f"{cups} cup{'s' if cups > 1 else ''}")
    if tablespoons:
        result.append(f"{tablespoons} tablespoon{'s' if tablespoons > 1 else ''}")
    if teaspoons:
        result.append(f"{teaspoons} teaspoon{'s' if teaspoons > 1 else ''}")
    
    return ', '.join(result)

print(convert_volume(59, 'teaspoon'))
print(convert_volume(50, 'tablespoon'))