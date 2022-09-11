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



#a = dict([4, "apple"])
#print(a)
