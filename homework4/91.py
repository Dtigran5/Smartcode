def ordinalDate(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    ordinal_day = sum(days_in_month[:month - 1]) + day
    return ordinal_day

if __name__ == "__main__":
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    
    result = ordinalDate(day, month, year)
    print(f"The ordinal date is: {result}")
