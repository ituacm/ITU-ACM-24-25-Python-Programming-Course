class ListItem: # PascalCase
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()