from python_common.collections.sorted_list import SortedList


class Foo:
    def __init__(self, initial_value):
        self.bar = initial_value

    def __repr__(self):
        return str(self.bar)


target = SortedList(accessor=lambda x: x.bar)

changeable = Foo(5)
target.add(Foo(5))
target.add(Foo(6))
target.add(Foo(4))
target.add(changeable)
target.add(Foo(9))
target.add(Foo(8))

print target.items

changeable.bar = 7
target.items_changed()

print target.items
