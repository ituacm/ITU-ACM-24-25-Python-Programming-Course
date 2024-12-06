from List import List


class MutableList(List):
    def __init__(self, value):
        super().__init__(value)

    def __setitem__(self, index, value):
        if index >= self.len() or index < 0:
            print("ERROR")
        else:
            temp = self.head
            i = 0
            while i < index:
                temp = temp.next
                i += 1
            temp.value = value

    def __add__(self, other):
        pass #TODO - problem set q2

    def __mul__(self, times):
        pass #TODO - problem set q3