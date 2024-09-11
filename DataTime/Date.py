from datetime import *
def inf():
    temp = input("Enter Date in dd/mm/yyy format")
    days,month,year = temp.split('/')
    return datetime(int(year), int(month), int(days))

d1 = inf()
d2 = inf()
d3 = d2 - d1
print('\nNo of Days : ',d3.days,"\nNo of Week : ", d3.days//7,"\nNo of Month : ", d3.days//12,"\nNO of Year : ", d3.days//365)