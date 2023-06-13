class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value}'


root = Node(10)
left = Node(5)
left2 = Node(2)

left.left = left2

right = Node(15)

root.left = left
root.right = right

print(root.left.left)
