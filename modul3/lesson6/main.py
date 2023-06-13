class Year:
    def __init__(self):
        self.__days = 365

    def get_days(self):
        return self.__days

    def set_day(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise ValueError(f"В году не может быть {days} дней.")


year = Year()
print(year.get_days())
year.set_day(365)
