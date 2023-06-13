from datetime import datetime

print(datetime.now().ctime())
print(datetime.now().date())
print(datetime.now().time())

my_date = "01/01/2023"
str_to_day = datetime.strptime(my_date, "%d/%m/%Y")
print(str_to_day.date())


