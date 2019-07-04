#Hash maps and Hashing functions

Initial_capacity = 50     #an arbritrary value. Can be changed to any value

class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = Initial_capacity
        self.size = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        hashsum = 0
        for index, character in enumerate(key):         #for index and character in key,enumerate through the key 
            hashsum += (index + len(key)) ** ord(character)     # hashsum = (index value + length of key) raised to ordinal of character
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = node(key, value)
            parry = self.buckets[index]
            return parry
        current_node = node
        while node is not None:
            current_node = node
            node = node.next
        current_node.next = node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            print('Key is absent')
        else:
            return node.Value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node !=key:
            current_node = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if current_node is None:
                node = None
            else:
                current_node.next = current_node.next.next
            return result


s = HashTable()
s.insert('jay', 'rodriguez')
s.insert('1', 'michael')
s.insert('monte', 'carlo')
print(s.find('jay'))
