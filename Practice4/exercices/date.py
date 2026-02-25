from datetime import datetime, timedelta
#1 
x = datetime.now() - timedelta(days=5)
print(x) 

#2
print(datetime.today()) 
print(datetime.today() - timedelta(days=1))
print(datetime.today() + timedelta(days=1))

#3
now = datetime.now() 
print(now.replace(microsecond=0))

#4
d1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S") 
different = d2-d1
print(abs(different.total_seconds()))