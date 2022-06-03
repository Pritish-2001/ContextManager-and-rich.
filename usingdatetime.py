import datetime as dt

# the date constructor

# f:
join_date=dt.date(2002,5,23)
td=dt.date.today()


print(td)

# access elements
print(td.year,td.month,td.day)
import time
date_time=dt.datetime.fromtimestamp(time.time())
print("hii",date_time)
s=dt.date.isoformat(td)
print(s)
print(type(s))
print(dt.datetime.now())

print("3 days from now",td+dt.timedelta(days=2,hours=26))

print(dt.datetime.now().astimezone())
print(dt.datetime.now().astimezone().tzname())

