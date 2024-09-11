from datetime import *

start = input("Enter time in hh:mm:ss\n")
end = input("Enter time in hh:mm:ss\n")

t1 = datetime.strptime(start, '%H:%M:%S')
t2 = datetime.strptime(end, '%H:%M:%S') 

diff = t2 - t1

print("Mint : ",diff.total_seconds()//60)
print("Hour : ",diff.total_seconds()//3600)