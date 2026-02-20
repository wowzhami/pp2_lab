
#%A	Полный день недели	Friday
#%a	Сокращенный день недели	Fri
#%B	Полное название месяца	February
#%d	Число месяца (01-31)	20
#%Y	Год (4 цифры)	2026
#%H:%M	Часы и минуты	15:36


import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.datetime(2020, 5, 17)
print(x)
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #June