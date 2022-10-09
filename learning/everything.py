# Overview of everything
'''
# variable assignment and printing
a = 5
b = a
print(a)
print(b)

# change variables
a = a - 4
b -= 4
print(a)
print(b)


# types of variables
a = 1 # integer
a = 0.5 #float
s = "examples" #string
print(s[0].upper())


# strings
print(s[-3]) # string == array
# find letter with given index

a = "Apple"
b = "Banana"
c = a + b #concatination
print(c)





# functions

def goofyah(a,b):
    return a * b


print(goofyah(4, 12))


def goofyah2(s):
    return s[2].upper()


print(goofyah2("teddy"))


# write a function that adds 2 strings
# ex. func("vallen", "steven") == "vallensteven"



# 2D and 3D array
rows = 4
columns = 4
height = 4
arr = [[[2]*columns]*rows]*height

for i in range(0, rows):
    for j in range(0, columns):
        for k in range(0, height):
            arr[i][j][k] = i+j+k # makes all values in array 0


print(arr)


# tuples
a,b = (3, 4) # (3,4) is a tuple
c = (5,6)
c[0] -= 1
print("A:", str(a))
print("B:", str(b))
'''

# list exercises

# 1. reverse a list
list1 = [100, 200, 300, 400, 500]
#solution 1:
#list1.reverse()
#solution 2:
#list1 = list1[::-1]
#print(list1)


# 2. add two list by index
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = ['My', 'name', 'is', 'Kelly']

#zip
ziped = zip(list1, list2)
list3 = []
for i,j in ziped:
    list3.append(i+j)
print(list3)


# 3. Turn every item in list into its square
numbers = [1,2,3,4,5,6,7,8] #result: [1,4,9,16,25,36,49,64]
#hint use for loop


# 4. remove empty string from list
list1 = ["Mike", "","Emma", "Kelly", "", "Brad"] # result: ["Mike", "Emma", "Kelly", "Brad"]
#use filter
print(list(filter(None, list1)))


# 5. replace item(20) with new value (250)
list1 = [5, 10, 15, 20, 25, 50, 80] #result: [5, 10, 15, 250, 25, 50, 80]
#hint: used index()
index = list1.index(20)
list1[index] = 250
print(list1)
