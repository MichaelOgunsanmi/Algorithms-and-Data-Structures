# Heaps class

class BinHeap:
    def __init__(self):
        self.heap = [0]*10
        self.currentposition = -1

    def insert(self, item):
        self.currentposition += 1
        self.heap[self.currentposition] = item
        self.fixup(self.currentposition)

    def isheapfull(self):
        pass

    def fixup(self, index):
        parent_index = int((index-1)/2)
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp
            index = parent_index
            parent_index = int((index-1)/2)

    def getmaximum(self):
        result = self.heap[0]
        self.currentposition -= 1
        self.heap[0] = self.heap[self.currentposition]
        del self.heap[self.currentposition +1]
        self.fixdown(0, -1)
        return result

    def fixdown(self, index, uptoindex):
        if uptoindex < 0:
            uptoindex = self.currentposition
        while index <= uptoindex:
            left_child = 2*index + 1
            right_child = 2*index + 2
            if left_child <= uptoindex:
                childtoswap = None
                if right_child > uptoindex:
                    childtoswap = left_child
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        childtoswap = left_child
                    else:
                        childtoswap = right_child
                if self.heap[index] < self.heap[childtoswap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childtoswap]
                    self.heap[childtoswap] = temp
                else:
                    break
                index = childtoswap
            else:
                break

    def heapsort(self):
        for i in range(0, self.currentposition+1):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.currentposition -i]
            self.heap[self.currentposition -i] = temp
            self.fixdown(0, self.currentposition -i -1)


s = BinHeap()
s.insert(12)
s.insert(3)
s.insert(23)
s.insert(4)
print(s.getmaximum())
print('###############')
print(s.getmaximum())
print('###############')
print(s.getmaximum())
print('###############')
print(s.getmaximum())
print('###############')
print(s.getmaximum())
print('###############')
# s.heapsort()
