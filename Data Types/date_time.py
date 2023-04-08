# date_time.py

from datetime import date, datetime, time

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
    # only 366 days until next year

# NikolaTesla = date(1856, 7, 10)   # alternate to following line
NikolaTesla = date.fromisoformat("1856-07-10")
print("Nickola Tesla was born on", NikolaTesla)
    # Nickola Tesla was born on 1856-07-10
print(NikolaTesla.weekday())    # 3 [which represents Thursday as where 0 = Monday and 6 = Sunday]

now = datetime.now()
print("right now it's:", now)   # right now it's: 2023-04-07 23:03:18.915554
print("it's the {}th minute of the {}th hour of the {}th day of the {}th month".format(
    now.minute,
    now.hour,
    now.day,
    now.month
))
    # it's the 7th minute of the 23th hour of the 7th day of the 4th month

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
print("the nuclear disaster in Chernobyl occurred on:", chernobyl)
    # the nuclear disaster in Chernobyl occurred on: 1986-04-26 01:23:40+04:00
print(chernobyl.strftime("The Chernobyl disaster occurred on %A %B %dth, %Y at %X MSD(%Z)"))
    # The Chernobyl disaster occurred on Saturday April 26th, 1986 at 01:23:40 MSD(UTC+04:00)
print("MSD is actually:", chernobyl.tzinfo)
    # MSD is actually: UTC+04:00

