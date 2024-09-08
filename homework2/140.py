def get_postal_info(postal_code):
    province_map = {
        'A': 'Newfoundland',
        'B': 'Nova Scotia',
        'C': 'Prince Edward Island',
        'E': 'New Brunswick',
        'G': 'Quebec',
        'H': 'Quebec',
        'J': 'Quebec',
        'K': 'Ontario',
        'L': 'Ontario',
        'M': 'Ontario',
        'N': 'Ontario',
        'P': 'Ontario',
        'R': 'Manitoba',
        'S': 'Saskatchewan',
        'T': 'Alberta',
        'V': 'British Columbia',
        'X': 'Nunavut or Northwest Territories',
        'Y': 'Yukon'
    }

    if len(postal_code) != 7 or postal_code[3] != ' ':
        return "Invalid postal code format. Please use the format 'A1A 1A1'."

    first_char = postal_code[0].upper()
    second_char = postal_code[1]

    if first_char not in province_map:
        return "Invalid postal code. It begins with an invalid character."

    if not second_char.isdigit():
        return "Invalid postal code. The second character must be a digit."

    province = province_map[first_char]
    address_type = "rural" if second_char == '0' else "urban"

    return f"The postal code is for an {address_type} address in {province}."

postal_code = input("Enter a Canadian postal code: ")
print(get_postal_info(postal_code))
