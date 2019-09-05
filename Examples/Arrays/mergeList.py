def mergeSortedList(list1, list2):
    output= []
    i= 0
    j=0
    while True:
        if i >= len(list1):
            output.extend(list2[j:])
            return output
        if j >= len(list2):
            output.extend(list1[i:])
            return output
        
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1


print(mergeSortedList([2,4,5,6,8,9,10], [1,3,7,11]))

