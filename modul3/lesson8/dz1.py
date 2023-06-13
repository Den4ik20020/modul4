class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return self.brand


item_list = [
    Item(1000, "Aplle"),
    Item(1200, "Apple"),
    Item(900, "Samsung"),
    Item(700, "Samsung"),
    Item(660, "Xiaomi")
]

filtered_list = list(x for x in item_list if x.brand == 'Samsung')
print(filtered_list)

names_list = ['данил', 'артём', 'никита', 'влад']
print([x[0].upper() + x[1:] for x in names_list])
print([w.capitalize() for w in names_list])