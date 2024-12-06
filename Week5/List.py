from list_item import ListItem

class List:
    def __init__(self, list_item):
        if isinstance(list_item, int):
            list_item = ListItem(list_item)
        else:
            raise TypeError("Can only add nodes and integers to a list")
        self.head = list_item
        self.tail = list_item
        
    def __str__(self):
        s = ''
        cur = self.head
        while cur != None:
            s += (str(cur) + ' ')
            cur = cur.next
        
        return s.strip()
    
    def __repr__(self):
        return self.__str__()

    def print_list(self):
        print(self)
    
    def __len__(self):
        l = 0
        cur = self.head
        while cur != None:
            l += 1
            cur = cur.next
        return l

    def __getitem__(self, index):
        if len(self) <= index:
            raise IndexError(f"List object has length {len(self)}, attepmted to reach index {index}")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        return cur