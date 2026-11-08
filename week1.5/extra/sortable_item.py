"""Example of sorting class instances using __lt__."""
class SortableItem:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"SortableItem({self.value})"

items = [SortableItem(3), SortableItem(1), SortableItem(2)]
print(sorted(items))
