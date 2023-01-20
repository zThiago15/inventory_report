from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.items = data
        self.indexItem = 0

    def __next__(self):
        try:
            item = self.items[self.indexItem]
        except IndexError:
            StopIteration()
        else:
            self.indexItem += 1
        return item
