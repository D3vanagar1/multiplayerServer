'''
# Maximum: find maximum of 2 numbers
# input: 2 numbers
# output: 1 number (the larger number)
def maximum(a,b):
    # code goes here
    billy = a>b
    if billy: 
        return a
    else:
        return b

print(maximum(5,37))

# minimum
def minimum(a,b):
    # code goes here
    billy = a<b
    if billy: 
        return a
    else:
        return b

print(minimum(5,37))



#exercise 1: add beginning and end of list
def add_ends(lst):
    return lst[0]+lst[-1]


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
    bob = input[0]
    input[0] = input[-1]
    input[-1] = bob
    return input


print(swap_ends([12, 35, 9, 56, 24]))

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
    for chicken_nuggets in lst:
        #do_smth with chicken_nuggets
        if chicken_nuggets == x:
            # code here
            print(chicken_nuggets)

            
print(countX([8,6,10,8,20,10,8,8], 8))
print(countX([8,6,10,8,20,10,8,8], 4))

# need for loop and if statement


while eeee:
# exercise: find the average of 5 numbers using a while loop
arr = [3, -9, 8, 1, 4]
print("1.4")
loop




# exercise: using a for loop print all the vehicles in the list except for Bus
vehicles = ['Car', 'Cycle', 'Train', 'Bus', 'SkateBoard']
for bob in vehicles:
    if bob == "Bus":
        continue
    print(bob)
'''


# exercise print a triangle of stars using for loops and range
#hint: print('*', end=='')

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
rows = 5
#rows
for i in range(rows, 0, -1):
    # columns
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\n")