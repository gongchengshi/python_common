class SortedList:
    def __init__(self, initial_items=None, accessor=None):
        self.items = initial_items if initial_items is not None else []
        self.accessor = accessor if accessor else lambda x: x
        self.cmp = lambda x, y: self.accessor(y) - self.accessor(y)

    def add(self, new_item):
        i = 0
        for item in self.items:
            if self.accessor(new_item) < self.accessor(item):
                self.items.insert(i, new_item)
                return
            i += 1
        if i == len(self.items):
            self.items.append(new_item)

    def items_changed(self):
        self.items.sort(key=self.accessor)

    def __len__(self):
        return len(self.items)
