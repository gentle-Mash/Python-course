import datetime as dt

now = dt.datetime.now()
# print(now)

year = now.year
month = now.month
day = now.day
week_day = now.weekday()

print(year,month,day,week_day)


date_of_birth = dt.datetime(year=1988, month=12, day=19, hour=6)
print(date_of_birth)