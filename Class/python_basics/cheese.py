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

def countX(lst, x):
    count = 0
    for element in lst:
        if lst == x:
            count = count + 1
    return count

print(countX([8,6,10,8,20,10,8,8], 8))
print(countX([8,6,10,8,20,10,8,8], 4))


# need for loop and if statement