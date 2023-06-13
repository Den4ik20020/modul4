import time


class CodeTimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print('Время работы кода составило: ', t, ' сек.')

        return True



timer = CodeTimer()

with timer as t:
    l = [i for i in range(10)]
    l[100]