'''
# Maximum: find maximum of 2 numbers
# input: 2 numbers
# output: 1 number (the larger number)
def maximum(a,b):
    # code goes here
    
    POOP = a>b
    if a>b:
        return a
    else:
        return b
print (maximum(420,69)) # a>b
print(maximum(1, 200)) # b>a


# minimum: find minimum of 2 numbers
# input: 2 numbers
# output: 1 number (the smaller number)
def minimum(a,b):
    #code here
    if a<b:
        return a
    else:
        return b

print (minimum(420, 6969))



#exercise 1: add beginning and end of list
def add_ends(lst):
    return lst[0] + lst[-1]

print(add_ends([4,5,6,7,8,9]))
print(add_ends(['B','F','D','Q']))
'''


# challenge: swap first and last element of list
'''
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''
'''
def swap_ends(input):
    input[0],input[-1] = input[-1],input[0]
    return input


print(swap_ends([69,1,2,3,4,420]))

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
'''
'''
# write a function that multiples all numbers in the list
def multList(myList):
    result = 1
    for element in myList:
        result = result*element
    return result

print(multList([4,5,6]))
print(multList([-4,0.5,10]))

# write a function that adds all numbers in the list
def addList(myList):
    result = 0
    for element in myList:
        result = result+element
    return result

print(addList([4,5,6]))
print(addList([-4,0.5,10]))
'''

'''
# find the smallest number in a list
def mini(myList):
    result = myList[0]
    for element in myList:
        print("element is" , str(element))
        if result>element:
            result = element
            print("result is", str(result))
    return result

print(mini([12, 1,-2,3]))



# exercise: find the average of 5 numbers with a while loop
arr = [3, -9, 8, 1, 4]
#while arr:
print("1.4")



# exercise: using a for loop print all the vehicles in the list except for Bus
vehicles = ['Car', 'Cycle', 'Train', 'Bus', 'SkateBoard']
for e in vehicles:
    if e == "Bus":
        continue
    print(e)
'''


# exercise print a triangle of stars using for loops and range
#hint: print('*', end='')


'''
*
**
***
****
'''



# exercise print the following patter using a for loop
'''
5 4 3 2 1
4 3 2 1 
3 2 1 
2 1
1
'''
eggman = 5

for i in range(0, eggman):
    # columns
    for j in range(0, i + 1):
        print("*", end=' ')
