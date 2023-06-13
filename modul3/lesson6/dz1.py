class Year:
    def __init__(self):
        self.__days = 365

    @property
    def days(self):
        return self.__days


    @days.setter
    def days(self, days):
        if days < 365 or days > 366:
            raise ValueError(f"В году не может быть {days} дней.")
        self.__days = days



year = Year()
print(year.days)
year.days = 366
print(year.days)
