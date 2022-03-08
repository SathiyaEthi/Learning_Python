import sys


class DateDiffCalc:
    def __init__(self, date, month, year):
        self.date = int(date)
        self.month = int(month)
        self.year = int(year)


# store total no of days for each month
daysmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leapyear_days(curdate):  # Calculate the leap year days till the current year passed

    years = curdate.year

    # if leap year is given and the month is lesser than 2nd Month, then dont count that year
    if curdate.month <= 2:
        years -= 1
    leapyear_days_count = (years / 4) - (years / 100) + (years / 400)
    return int(leapyear_days_count)


def calculate_days(x):  # calculate the total number of days till the date passed

    # add the year days with the date value
    no_of_days = x.year * 365 + x.date

    # Add days for months in given date
    for i in range(0, x.month - 1):
        no_of_days += daysmonth[i]

    # add the leap year days
    no_of_days += leapyear_days(x)

    return (no_of_days)


def verify_date_format(date):  # verify the date format. If wrong, then exception
    try:
        print("date ==> ", date)
        if len(str(date[0])) > 2 | len(str(date[1])) > 2 or len(str(date[2])) > 4 or date[1] > 12:
            raise ValueError("Date is not in valid format:", date)

        if date[2] % 4 == 0:
            if date[1] == 2:
                if date[0] > 29:
                    raise ValueError("Leap year has 29 DAYS in Feb month. Please pass the correct date")
        if date[0] > daysmonth[date[1] - 1]:
            raise ValueError("Day field is wrong: ", date[0])

    except ValueError as e:
        raise ValueError


# finally:
#     dt = date
# return (date)


def input_date_validation(fdt1, fdt2):
    try:
        if fdt1[2] > fdt2[2]:
            raise ValueError("First date is latest than second date given.So difference can't be found")

        elif fdt1[1] > fdt2[1]:
            raise ValueError("First date is latest than second date given.So difference can't be found")

        elif fdt1[0] > fdt2[1]:
            raise ValueError("First date is latest than second date given.So difference can't be found")
    except ValueError as e:
        raise ValueError


def dateformat(s):  # split the date into subparts
    [day, month, year] = map(int, s.split('/'))
    return day, month, year


def date_diff_finder(first_date, last_date):
    # create the object for Base class and initiate
    first_days = DateDiffCalc(first_date[0], first_date[1], first_date[2])
    last_days = DateDiffCalc(last_date[0], last_date[1], last_date[2])

    # print the output result
    diff = calculate_days(last_days) - calculate_days(first_days)

    return diff


def final(first_date, last_date):
    return date_diff_finder(dateformat(first_date), dateformat(last_date))
