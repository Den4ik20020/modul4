class Windows:
    def __init__(self, version, country):
        self.__version = version
        self.country = country

    def get_version(self):
        return self.__version


w = Windows(version=10, country="China")
print('Версия:', w.__version)
w.__version = 7
print('Версия:', w.__version)

print('Версия:', w._Windows__version)
w._Windows__version = 7
print('Версия:', w._Windows__version)
