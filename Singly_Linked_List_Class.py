# # Singly Linked list
#
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def display(self):                              #display elements in the SinglyLinkedList
#         if self.head is None:
#             print('List is Empty')
#             return
#         current_node = self.head
#         while current_node.next !=None:
#             print(current_node.data)
#             current_node = current_node.next
#         print(current_node.data)
#
#     def length(self):                           #find length of SinglyLinkedList
#         current_node = self.head
#         total = 0
#         while current_node != None:
#             total += 1
#             current_node = current_node.next
#         return total
#
#     def Einsert(self, new_node):                    #Insert at the End
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next != None:
#                 current_node = current_node.next
#             current_node.next = new_node
#
#     def Binsert(self, new_node):                #Insert at the Beginning
#         current_node = self.head
#         self.head = new_node
#         self.head.next = current_node
#         del current_node
#
#     def Iinsert(self, new_node, index):     #Index Insert
#         if index is 0:
#             self.Binsert(new_node)
#             return
#         elif index < 0 or index >= self.length():
#             print('Invalid Position')
#             return
#         elif index == (self.length() - 1):
#             self.Einsert(new_node)
#             return
#         else:
#             current_node = self.head
#             current_index = 0
#             while True:
#                 if current_index == index:
#                     previous_node.next = new_node
#                     new_node.next = current_node
#                     break
#                 previous_node = current_node
#                 current_node = current_node.next
#                 current_index += 1
#
#     def Bdelete(self):                          #delete at the beginning
#         current_node = self.head
#         rest_node = current_node.next
#         self.head = rest_node
#         current_node.next = None
#         del current_node
#
#     def Edelete(self):                         #delete at the end
#         last_node = self.head
#         while last_node.next is not None:
#             previous_node = last_node
#             last_node = last_node.next
#         previous_node.next = None
#
#     def Idelete(self, index):                               #Index delete
#         if index < 0 or index >= self.length():
#             print('Invalid Position')
#             return
#         else:
#             current_node = self.head
#             current_index = 0
#             while True:
#                 if current_index == index:
#                     previous_node.next = current_node.next
#                     current_node.next = None
#                     break
#                 previous_node = current_node
#                 current_node = current_node.next
#                 current_index +=1
#
#     def Iextraction(self, index):                           #index extraction
#         if index < 0 or index >= self.length():
#             print('Invalid Position')
#             return
#         else:
#             current_node = self.head
#             current_index = 0
#             while True:
#                 if current_index == index:
#                     print(current_node.data)
#                     break
#                 current_node = current_node.next
#                 current_index += 1
#
#     def search(self, data):                                     #search for an element in the linked list
#         current_node = self.head
#         found = False
#         while found is False:    #ben-michael-daniel-grace
#             if current_node.data == data:
#                 found = True
#                 print(str(data) + ' is in the list')
#                 break
#             current_node = current_node.next
#             if current_node is None:
#                 print('Error, element not in list')
#                 break
#
# print
print(5//2)







#
#
#
#
# # firstnode = node(56)
# # singlyLinkedlist = SinglyLinkedList()
# # singlyLinkedlist.Einsert(firstnode)
# # secondnode = node('ogunsanmi')
# # singlyLinkedlist.Einsert(secondnode)
# # thirdnode = node('michael')
# # singlyLinkedlist.Einsert(thirdnode)
# # fouthnode = node(10000000)
# # #singlyLinkedlist.Binsert(fouthnode)
# # singlyLinkedlist.display()
# # print(singlyLinkedlist.length())
# # print('#########################')
# # fifthnode = node('aarin')
# # singlyLinkedlist.Idelete(0)
# # singlyLinkedlist.display()
# # print(singlyLinkedlist.length())
# # singlyLinkedlist.search('goat')
