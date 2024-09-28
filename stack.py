class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.li = []
    def isEmpty(self):
        if(len(self.li)==0):
            return True
        return False
    def push(self,ele):
        self.li.append(ele)
    def pop(self):
        if(self.isEmpty()):
            raise IndexError("Popping from an empty list")
        self.li.pop()
    def top(self):
        if(self.isEmpty()):
            raise IndexError("List is empty so no element at the top")
        return self.li[-1]
    def getList(self):
        return self.li
    # You can implement this class however you like