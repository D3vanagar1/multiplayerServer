# DATA TYPES

# tuples
x = () #emtpy tuple
#print(x)

tuplex = tuple() # built in function
#print(tuplex)

x = ("tuple", False, 3.2, 1)
#print(x)

# save item from list into variable
a = [3, 5, "apple"]
string = a[2] # string = apple
#print(string)

# save item from tuple into variable
n1, n2, n3, n4 = x
#print(n3+n4)

#tuplex = n1, n2, n3
#print(tuplex)

#example: get item from tuple (letter s)
tuplex = ("w",3,"r","e", " s", "o", "u", "r")
item= tuplex[-3]
#print(item)


#challenge convert tuple into dictionary
tuplex = ((69420, "Vallen"), (42069, "Ethan"))

#method 1
dct = dict()
for x,y in tuplex:
    dct[y] = x
print(dct)



#method 2
dct = dict(map(reversed, tuplex))
print(dct)



# reversed()
print(list(reversed(("a", "b", "c"))))

#map()

# ex func
def mutlby2(n):
    return 2*n

numbers = [1,2,3,4]
result = list(map(mutlby2, numbers))
print(result)


#excersise 2
# mutliple all numbers of a tuple

def multiply_tuple(tup):
    temp = list(tup)
    product = 1
    for x in temp:
        product *= x
    return product


nums = (4, 3, 2, 2, -1 , 18)
print(nums)
print(multiply_tuple((nums)))