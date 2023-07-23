a = open('July.txt', 'r') # download/copy appropriate month's prayer times chart 
                          # (set to 18 degrees for Fajr and 'Isha (the latter to be safer))
                          # and manipulate list to look like July.txt or whatever month is shown
                          # https://www.islamicfinder.org/world/united-states/5128581/new-york-city-nyc-prayer-times/

b = a.read()

c = b.splitlines()

i = 0
sunset_list = []
sunrise_list = []

while i < 31:
    sunset_list.append(c[i].split()[11])
    i += 1
sunset_list.pop(-1)

i=0
while i < 30:
    sunrise_list.append(c[i+1].split()[3])
    i += 1

i=0
m = open("July_midnight.txt",'w')
s = ''
while i < 30:
    rise_hour = 12 + 10*int(sunrise_list[i][0]) + int(sunrise_list[i][1])
    rise_minute = 10*int(sunrise_list[i][3]) + int(sunrise_list[i][4])

    set_hour = 10*int(sunset_list[i][0]) + int(sunset_list[i][1])
    set_minute = 10*int(sunset_list[i][3]) + int(sunset_list[i][4])
    

    diff_hour = rise_hour - set_hour
    diff_minute = rise_minute - set_minute
    
    amt = int((diff_hour * 60 + diff_minute)/2)

    calc_hour = int((set_hour + (amt - amt%60)/60))

    calc_minute = int(amt%60 + set_minute)
    if calc_minute >= 60:
        calc_hour += 1
        calc_minute -= 60

    if calc_hour > 12:
        calc_hour -= 12
    
    if calc_hour < 12:
        if calc_minute < 10:
            print(f'July {i+1} : {calc_hour}:0{calc_minute} PM')
            s = 'July ' + str(i+1) + ': ' + str(calc_hour) + ':0' + str(calc_minute) + ' PM'
        else:
            print(f'July {i+1} : {calc_hour}:{calc_minute} PM')
            s = 'July ' + str(i+1) + ': ' + str(calc_hour) + ':' + str(calc_minute) + ' PM'
    else:
        if calc_minute < 10:
            print(f'July {i+1} : {calc_hour}:0{calc_minute} AM')
            s = 'July ' + str(i+1) + ': ' + str(calc_hour) + ':0' + str(calc_minute) + ' AM'
        else:
            print(f'July {i+1} : {calc_hour}:{calc_minute} AM')
            s = 'July ' + str(i+1) + ': ' + str(calc_hour) + ':' + str(calc_minute) + ' AM'
    
    m.write(s)
    m.write('\n')

    i+=1

m.close()
a.close()