#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import timedelta
a = timedelta(days = 3, hours = 4)
b = timedelta(hours = 6.5)
c = a + b
c.days
c.seconds
c.seconds / 3600


from datetime import datetime
a = datetime(2015, 3, 20)
print(a + timedelta(days = 5))
b = datetime(2015, 4, 30)
d = b - a
d.days
now = datetime.today()
print(now)
print(now + timedelta(days = 2))

a = datetime(2015, 3, 20)
a + timedelta(months = 1)


from dateutil.relativedelta import relativedelta
a + relativedelta(months =+ 1)


from datetime import datetime
from pytz import timezone
d  = datetime(2015, 3, 20, 8, 44, 0)
print(d)
chicago = timezone('US/Central')
loc = chicago.localize(d)
print(loc)



from datetime import datetime, date, timedelta
import calendar 

def month_range(start_date = None): 
    if start_date is None: 
        start_date = date.today().replace(day = 1)
    _, days_in_month = calendar.monthrange(start_date. year, start_date.month) 
    end_date = start_date + timedelta(days = days_in_month)
    
    return (start_date, end_date) 

a_day = timedelta(days = 1)
first_day, last_day = month_range()

while first_day < last_day: 
    print(first_day)
    first_day += a_day
    


from datetime import datetime
text = '2015-03-20'
d = datetime.strptime(text, '%Y-%m-%d')
d

text = '20-03-2015'
d = datetime.strptime(text, '%d-%m-%Y')
d
nice_date = datetime.strftime(d, '%A %B %d, %Y')
nice_date


import locale
locale.setlocale(locale.LC_ALL, ('bulgarian'))
nice_date = datetime.strftime(d, '%A %B %d, %Y')
nice_date
