#!/usr/bin/python
# -*- coding: utf-8 -*-

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
