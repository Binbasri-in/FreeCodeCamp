def add_time(start, duration, start_day=None):
  #get all the needed data
  time = start.split()
  mode = time[1]
  r_time = time[0].split(':')
  hour = int(r_time[0])
  min = int(r_time[1])
  colons = duration.find(':')
  d_hour = int(duration[0:colons])
  d_min = int(duration[colons+1:])
  
  #the minutes and additional hours from it
  min_hour = int((min + d_min)/60)
  r_min = (min + d_min) % 60

  # the hours and how many half days passed
  half_d = int((hour + d_hour + min_hour)/12)
  r_hour = (hour + d_hour + min_hour) % 12
  #check PM or AM
  if mode == 'PM':
    add_mode = 1
    if half_d % 2 == 0:
      mode = 'PM'
    else:
      mode = 'AM'
  else:
    add_mode = 0
    if half_d % 2 == 0:
      mode = 'AM'
    else:
      mode = 'PM'
  #exceptions
  if r_hour == 0:
    r_hour = 12
  if r_min < 10:
    r_min = '0'+str(r_min)
  # count days
  days = int((add_mode+half_d)/2)
  if days == 1:
    day = '(next day)'
  elif days == 0:
    day = ''
  else:
    day = f"({days} days later)"
  day_name = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
  if not start_day == None:
    start_day = day_name.index(start_day.lower())
    dayName = day_name[(start_day+days) % 7].capitalize()
    return f"{r_hour}:{r_min} {mode}, {dayName} {day}".strip()

  
  return f"{r_hour}:{r_min} {mode} {day}".strip()