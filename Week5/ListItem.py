class ListItem(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

x = ListItem(3)
y = ListItem(2, x)
z = ListItem(1, y)

class List(object):
    def __init__(self, head):
        self.head = head

    def print_list(self):
        print_head = self.head
        while print_head is not None:
            print(print_head.value)
            print_head = print_head.next

my_list = List(z)
my_list.print_list()
