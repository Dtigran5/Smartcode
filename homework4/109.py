def days_in_month(month, year):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def is_magic_date(day, month, year):
    return day * month == year % 100

def find_magic_dates():
    magic_dates = []
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                if is_magic_date(day, month, year):
                    magic_dates.append(f"{month}/{day}/{year}")
    return magic_dates

if __name__ == "__main__":
    magic_dates = find_magic_dates()
    for date in magic_dates:
        print(date)
