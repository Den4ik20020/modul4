class MyFile:
    def __init__(self, filename, mode, encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile('file.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
