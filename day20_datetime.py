#exercise 1
from datetime import datetime, timedelta

user_date = input("enter a date in this format(yyyy/mm/dd): ")
today = datetime.now()

event_date = datetime.strptime(user_date, "%Y/%m/%d")

days_left = (event_date - today).days
print("Days left until event:", days_left)

#exercise 2
from datetime import datetime

today = datetime.now()
formated_date = today.strftime("%A %d %B %y") #%A and %B which is weekday and month name respectively
print(formated_date)

#exercise 3
from datetime import datetime

today = datetime.now()
formated_date = today.strftime("%I %M %S %p")
print(formated_date)

#exercise 4 this is my attempt
from datetime import datetime, timedelta

today = datetime.now()
birthday = "15/01/2008"
datetimes_birthday = datetime.strptime(birthday, "%d/%m/%y")

days_left = (datetimes_birthday - today).days
print(days_left)

from datetime import datetime, timedelta

today = datetime.now()
birthday_str = "15/01/2008"  # only the day/month really matter
bday = datetime.strptime(birthday_str, "%d/%m/%Y")
#below here is the answer
# replace year with current year
next_birthday = bday.replace(year=today.year)

# if this year's birthday already passed, move to next year
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print("Days until next birthday:", days_left)

#exercise 5
from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=100)

future_str = future.strftime("%d/%B/%Y, %A")

print(future_str, "is the date after 100 days")

#exercise 6
from datetime import datetime
from zoneinfo import ZoneInfo

today = datetime.now(ZoneInfo("Asia/Kolkata"))
today_ny = today.astimezone(ZoneInfo("America/New_york"))
print(today)
print(today_ny)