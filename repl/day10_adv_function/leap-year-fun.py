no_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year, month):

    result = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
    if result:
        print(f"Number of days in {month} month is {no_days_in_month[month - 1]} and year is ", year)
    elif month == 2:
        non_leap_month_feb = 28
        print(f"Number of days in {month} month is {non_leap_month_feb} and year is ", year)
    else:
        print(f"Number of days in {month} month is {no_days_in_month[month - 1]} and year is ", year)


year = int(input("Enter year :"))
month = int(input("Enter a month :"))
print(is_leap(year, month))