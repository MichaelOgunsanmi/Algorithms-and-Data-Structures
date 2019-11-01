import sys

sys.path.append(r'C:\Users\MICHAEL OGUNSANMI\Desktop\AI & '
                r'CS\Studying Source Codes\Software Intervierw '
                r'Preparation Codes\Algorithms-and-Data-Structures')

from StacksAndQueues.stacksWithArrays import Stack


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        self.moveStack1ToStack2()

        return self.stack2.pop()

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def moveStack1ToStack2(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())


if __name__ == '__main__':
    driver = QueueWithTwoStacks()
    driver.enqueue(1)
    driver.enqueue(2)
    driver.enqueue(3)
    driver.enqueue(4)
    driver.enqueue(5)
    driver.enqueue(6)
    driver.enqueue(7)
    print(driver.dequeue())
    print(driver.dequeue())
    print(driver.dequeue())
    print(driver.dequeue())
    print(driver.dequeue())
    print(driver.dequeue())