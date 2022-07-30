from datetime import datetime, timedelta

# date & time now
current_time = datetime.now()
print(current_time)

# all info about current time
print(f'{current_time.minute} minutes')
print(f'{current_time.year} year')
print(f'{current_time.microsecond} microseconds')

print(f'{current_time.date()} date')
print(f'{current_time.time()} time')

# set date
date1 = datetime(year=2001, day=12, month=3, hour=23, minute=55)
print(f'{date1} custom date')

# weekday; monday=0, sunday=6
print(f'{date1.weekday()} recognize weekday')

# compare dates
print(f'{current_time>date1} date comparison')

# timedelta
timedelta1 = current_time - date1
print(f'{timedelta1} timedelta')
print(f'{timedelta1.total_seconds()} timedelta total seconds')

four_weeks_time = timedelta(weeks=4)
print(f'{current_time - four_weeks_time} four weeks after now')

# seconds after 1970-01-01
print(f'{current_time.timestamp()} seconds after 1970-01-01')

# get date from total seconds
ts_from_birth = date1.timestamp()
print(f'{datetime.fromtimestamp(ts_from_birth+100000)} date after 100.000 seconds from my birth')

# strftime - datetime to str
print(date1.strftime('%A %d %B %Y'))

#strptime - str to datetime
s = '27 February 1980'
print(datetime.strptime(s, '%d %B %Y'))
