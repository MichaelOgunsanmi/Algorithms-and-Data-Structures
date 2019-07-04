# Stacks class

class Stacks:
    def __init__(self):
        self.items = list()

    def display(self):
        if self.items == []:
            print('No item in stack')
            return
        else:
            print(self.items[::-1])

    def empty(self):
        if self.items == []:
            print('Stack is empty')
            return
        else:
            print('Stack is not empty.')

    def push(self,value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def top(self):
        if self.items != []:
            print(self.items[-1])
        else:
            print('Stack is empty')
            return

    def size(self):
        return len(self.items)
