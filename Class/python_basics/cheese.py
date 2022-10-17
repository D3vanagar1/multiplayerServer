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
'''


#exercise 1: add beginning and end of list
def add_ends(lst):
    return lst[0] + lst[-1]

print(add_ends([4,5,6,7,8,9]))
print(add_ends(['B','F','D','Q']))
