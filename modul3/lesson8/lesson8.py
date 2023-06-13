if __name__ == '__main__':

    goods = [
        {
            'name': 'Iphone 7',
            'brand': 'Apple',
            'price': 250
        },
        {
            'name': 'Ipad',
            'brand': 'Apple',
            'price': 350
        },
        {
            'name': 'Windows 7',
            'brand': 'Microsoft',
            'price': 100
        }
    ]


    def on_price(item):
        return item['price']


    print(sorted(goods, key=lambda item: item['price']))

    filtered_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
    print(filtered_list)

    numbers = ['1', '2', '3', '4', '5']
    print(numbers)
    new_numbers = list(map(int, numbers))
    print(new_numbers)

    names_list = ['Егор', 'Сергей', 'Валера', 'Денис']
    surnames_list = ['Новиков', 'X', 'Шмелёв', 'Y']

    persons_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
    print(persons_list)

    new_goods_list = []

    for index, item in enumerate(goods):
        new_goods_list.append({index: item})

    print(new_goods_list)

    names_list = ['Диана', 'Дмитрий', 'Ирина', 'Мария', 'Иван']
    surname_list = ['Назарова', 'None', 'Шишкина', 'Верушкина', 'X']

    for name, surname in zip(names_list, surname_list):
        print(name, surname)

    print(__name__)
else:
    print('Запущенно из другого файла')