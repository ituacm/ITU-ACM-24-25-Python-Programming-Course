from list import List
from list_item import ListItem

class MutableList(List):
    def __init__(self, list_item):
        super().__init__(list_item)
        
    def append(self, new_node):
        if not isinstance(new_node, ListItem):
            if isinstance(new_node, int):
                new_node = ListItem(new_node)
            else:
                raise TypeError("Can only add nodes and integers to a list")
        
        self.tail.next = new_node
        self.tail = new_node
    
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            if isinstance(value, ListItem):
                value = value.value
            else:
                raise TypeError("Item assignment only supports ListItem and int types")
        
        if len(self) <= index:
            raise IndexError(f"List object has length {len(self)}, attepmted to reach index {index}")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        cur.value = value
