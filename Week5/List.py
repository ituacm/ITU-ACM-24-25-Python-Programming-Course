from ListItem import ListItem

class List(object):
    def __init__(self, value):
        self.head = ListItem(value)
        self.tail = self.head

    def __str__(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_item = ListItem(value)
        self.tail.next = new_item
        self.tail = new_item

    def len(self):
        len_list = 0
        temp = self.head
        while temp is not None:
            len_list += 1
            temp = temp.next
        return len_list

    def __getitem__(self, index):
        if index >= self.len() or index < 0:
            print("ERROR")
        else:
            temp = self.head
            i = 0
            while i < index:
                temp = temp.next
                i += 1
            return temp.value

