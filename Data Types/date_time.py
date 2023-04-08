# date_time.py

from datetime import date

today = date.today()
print("today is:", today)   # today is: 2023-04-07
print("day:", today.day)    # day: 7
print("month:", today.month)    # month: 4
print("year:", today.year)  # year: 2023

print(today.strftime("%A %d %B %Y"))    # Friday 07 April 2023
print(today.strftime("%A, %dth of %B in the year of our Lord %Y"))
    # Friday, 07th of April in the year of our Lord 2023
print(today.strftime("%a, %dth of %b \'%y"))
    # Fri, 07th of Apr '23

next_year = today.replace(year = today.year + 1)
print(next_year)    # 2024-04-07

difference = abs(next_year - today)
print("only {} days until next year".format(difference.days))
