from src.DateDiffCalc import *

if __name__ == "__main__":

    # Program Starts from here
    first_date = str(input("Enter the First Date(Date Format in DD/MM/YYYY):"))
    last_date = str(input("Enter the second Date(Date Format in DD/MM/YYYY):"))

    # format the input date into day,month,year
    first_date_formatted = dateformat(first_date)
    last_date_formatted = dateformat(last_date)

    # Verify the format of the date given and store it for testing purpose
    verify_date_format(first_date_formatted)
    verify_date_format(last_date_formatted)

    input_date_validation(first_date_formatted, last_date_formatted)

    print("Different between the dates {} {} {} ",first_date, last_date, date_diff_finder(first_date_formatted, last_date_formatted), "days")
