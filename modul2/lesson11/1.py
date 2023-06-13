class Windows:
    def __init__(self, versions, country):
        self.__versions = versions
        self.country = country

    def get_version(self):
        return self.__versions


w = Windows(versions=10, country="China")
print('Версия: ', w._versions)
w._versions = 7
print('Версия: ', w._versions)

print('Версия: ', w._Windows__versions)
w._Windows__versions = 7
print('Версия: ', w._Windows__versions)
