

#number = range(1, 13)
#print (number)
#row = []
#column = []

#print (row)


#print (row)

#for i in number:
#    row.append(i)
#    for j in number:
#        column.append(j)
#        print(column[j]*row[i])


#print("Times: " , end="")
#for number in range(1,10):
#    print(number,end="\t")
#print()

# The double for-loop
#for multiplum in range(1,9):
#    print(multiplum, end="      ") # First column
#    for number in range(1,10):
#        print(multiplum*number, end="\t") # Next 9 columns
#    print()


#for i in range(1, 13):
#    for j in range (1,13):
#        print (i*j)

# fruit = 'Banana'
# r = tuple(fruit)
#d = ' '
#d.join(r)
# print(r)
#bic = [ 1 , 33, True, 'gerrt']
#bic [1] = 'bic'
#g = fruit.lower()
#print (bic)
#length = len(fruit)
#index = -1
#print (index)
#while index > -(length+1):
#    print (fruit[index])
#    index = index - 1


#t = 'banana'

#r = t[0 : 3]
#print(r)

# r = range(0, 21, 2)
# even = list (r)
# even.pop(0)
# print (even)
# r = range(len(even))
# k = list (r)
# print(k)
# for i in even:
    # for m in k:
        # if m%2 == 0:
            # good = even[m]
            # print (good)


# def reverse(word):
    # return s[::-1]

def Palindrome(word):
    reversed_word = word[::-1]       #reverses the string using advanced slicing

    if (word == reversed_word):      #Checking if both strings are equal or not
        return True
    return False


# Driver code
# s = "malayalam"
# ans = Palindrome(s)

# if ans == 1:
    # print("Yes")
# else:
    # print("No")


# input_numbers = [int(x) for x in input().split()]
# print(input_numbers)

#import array

#arr = array.array('i', [1,2,3,4,5])

#arr.reverse()


def URLify(value):
    list_value = value.split()
    result = str()
    result = result + list_value[0] + '%20'
    result = result + list_value[1] + '%20'
    result = result + list_value[2]
    return result

s = URLify('Mr John Smith')
print(s)
