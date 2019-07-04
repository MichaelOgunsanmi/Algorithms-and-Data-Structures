# Queue class

class Queue:
    def __init__(self):
        self.items = list()

    def display(self):
        if self.items == []:
            print('Queue is empty')
            return
        else:
            print(self.items)

    def empty(self):
        if self.items == []:
            print('Queue is empty')
            return
        else:
            print('Queue is not empty')

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        self.items.pop(0)

    def top(self):
        if self.items != []:
            print(self.items[0])
        else:
            print('Queue is empty')
            return

    def size(self):
        return len(self.items)
