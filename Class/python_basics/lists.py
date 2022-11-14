# lists
lst1 = [7,2,91,11]
lst1.sort()
print(lst1)

lst2 = ['B', 'F', 'G', 'A', 'C', 'P']
lst2.sort()
print(lst2)

'''

print(add_ends([4,5,6,7,8,9]))
print(add_ends(['B','F','D','Q']))
'''

'''
    - sorting:
        - sorts the list from smallest to largest
    - append:
        - add item to end of list
    - start of list:
        list[0]
    - end of list:
        list[-1]
    - swap:
'''

#swap

# challenge: swap first and last element of list
'''
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

'''

# swapping 2 variables
a = 5
b = 3

tmp = a
a = b
b = tmp

'''

# challenge 2: count number of times element is in list
'''
Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3 
Explanation: 10 appears three times in given list.

Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
Output: 0
Explanation: 16 appears zero times in given list.
'''
'''
def countX(lst, x):
    count = 0
    for element in lst:
        if element == x:
            count = count + 1
    return count



print(countX([8,6,10,8,20,10,8,8], 8))
print(countX([8,6,10,8,20,10,8,8], 4))
print(countX([4,4,4,4,4], 4))
'''
#how to count in python:
'''
a = 0
for b in range(0, 10):
    if b//2 == 0:
        a = a + 1
        print(a)
'''


# write a function that multiples all numbers in the list
def multList(myList):
    pass

print(multList([4,5,6]))
print(multList([-4,0.5,10]))