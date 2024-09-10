def ordinal_date(year, day_of_year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 0
    while day_of_year > days_in_month[month]:
        day_of_year -= days_in_month[month]
        month += 1

    return day_of_year, month + 1

def future_date(year, day_of_year, days_to_add):
    total_days = day_of_year + days_to_add
    while True:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_year = 366
        else:
            days_in_year = 365

        if total_days <= days_in_year:
            return ordinal_date(year, total_days)
        else:
            total_days -= days_in_year
            year += 1

def main():
    year = int(input("Enter the year: "))
    day_of_year = int(input("Enter the day of the year (1-365/366): "))
    days_to_add = int(input("Enter the number of days to add: "))

    future_day, future_month = future_date(year, day_of_year, days_to_add)
    print(f"The future date is: {future_day}/{future_month}/{year}")

if __name__ == "__main__":
    main()
