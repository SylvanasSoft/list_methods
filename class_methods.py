# ==========================================
# list-class
class MyList:

    def __init__(self, massiv):
        self.massiv = massiv

    def __str__(self):
        return f"{self.massiv}"

    def append(self, item: int):
        self.massiv += [item]

    def clear(self):
        self.massiv = []

    def copy(self):
        return self.massiv

    def count(self, value=None):
        return sum([True for i in self.massiv if i == value])

    def extend(self, iterable: list | set | dict | str | tuple = None):
        self.massiv += iterable

    def index(self, iterable, start: int = 0, end: int = 0):
        end = len(self.massiv)
        item_index = None
        for i, v in enumerate(self.massiv[start:end + 1]):
            if v == iterable:
                item_index = i + start
                break
        return item_index

    def insert(self, index: int, object: int):
        self.massiv = self.massiv[:index] + [object] + self.massiv[index:]

    def pop(self, index: int = -1):
        return_val = self.massiv[index]
        del self.massiv[index]
        return return_val

    def remove(self, item: int):
        return [i for i in self.massiv if i != item]

    def reverse(self):
        self.massiv = self.massiv[::-1]

    def sort(self, reverse=False):
        self.massiv = sorted(self.massiv, reverse=reverse)


a = MyList([1, 6, 5])
