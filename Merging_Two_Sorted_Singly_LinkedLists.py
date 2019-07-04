from Singly_Linked_List_Class import node, SinglyLinkedlist

List1 = SinglyLinkedlist()
List2 = SinglyLinkedlist()
mergedlist = SinglyLinkedlist()

node_one = node(2)
node_two = node(6)
node_three = node(12)
node_four = node(6)
node_five = node(9)
node_six = node(24)

List1.Einsert(node_one)
List1.Einsert(node_two)
List1.Einsert(node_three)
List2.Einsert(node_four)
List2.Einsert(node_five)
List2.Einsert(node_six)

List1.display()
List2.display()
print('##################################################')

def mergelist(firstlist, secondlist, mergedlist):
    current_first = firstlist.head
    current_second = secondlist.head
    while True:
        if current_first is None:
            mergedlist.Einsert(current_second)
            break
        if current_second is None:
            mergedlist.Einsert(current_first)
            break
        if current_first.data <= current_second.data:   #2,6,12,   6,9,24
            current_first_next = current_first.next
            current_first.next = None
            mergedlist.Einsert(current_first)
            current_first = current_first_next
        else:
            current_second_next = current_second.next
            current_second.next = None
            mergedlist.Einsert(current_second)
            current_second = current_second_next

mergelist(List1, List2, mergedlist)
mergedlist.display()
