import calendar
from datetime import datetime
from pprint import pprint as pp


now = datetime.now()


cal = calendar.monthcalendar(now.year, now.month)


next_month = now.month +1
cal = calendar.monthcalendar(now.year, next_month)



print(cal[0])
pp(cal)
print(now)
