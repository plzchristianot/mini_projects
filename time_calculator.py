#this is a time calculator, please use it this way: add_time('8:16 PM', '466:02', 'tuesday'). This should return this: 6:18 AM, Monday (20 days later)

def add_time(start, duration, day=''):
    
#variables
    time, am_pm = start.split(' ')
    hour,mins = time.split(':')
    hour = int(hour)
    mins = int(mins)
    am_pm_old = am_pm
    hour_dur, mins_dur = duration.split(':')
    hour_dur = int(hour_dur)
    mins_dur = int(mins_dur)

    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index=0
    day_count=0
    day_number=0
    number_days=''
    new_time=''

#se hace match con el dia de la lista days
    for i in range(len(days)):
        if day.lower() == days[i].lower():
            day = days[i]

#se le asigna el valor 
    for day_index, match in enumerate(days):
        if day == match:
            day_number = day_index

#suma de start and duration
    total_hours =  hour + hour_dur
    total_mins = mins + mins_dur

#pasar 60mins a 1hr
    while total_mins >= 60:
        total_hours += 1
        total_mins -= 60

#cambiar am a pm o viceversa si suman más de 12hr
    while total_hours>=12 and total_mins>=0:
        if am_pm_old == 'AM':
            am_pm_old = 'PM'
        else:
            am_pm_old = 'AM'
            day_number+=1
            day_count+=1
        am_pm = am_pm_old
        total_hours -= 12

    if total_hours == 0:
        total_hours = 12

#condiciones para aclarar si es al dia siguiente o cuantos días siguientes son   
    if day_count <1:
        pass
    elif day_count==1:
        number_days=' (next day)'
    elif day_count >=2:
        number_days=' ('+ str(day_count) +' days later)'
    
    while day_number>6:
        day_number-=7

#condicion para agregar 0 a los minutos si no tiene decenas
    if total_mins <10:
        total_mins='0' + str(total_mins)

#condicion para ver si hay dia declarado o no y relleno de new_time
    if day:
        new_time = str(total_hours) + ':' + str(total_mins) + ' ' + am_pm + ', ' + days[day_number] + number_days
    else:
        new_time = str(total_hours) + ':' + str(total_mins) + ' ' + am_pm + number_days

    return new_time


