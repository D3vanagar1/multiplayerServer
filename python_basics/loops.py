'''
- for loop
- while loop



# while loop
var = 5
while var > 0:
    print(var)
    var = var - 1


# infinity while loop
test = True
i = 0
while test:
    print("Help")
    if i == 3:
        test = False
    i += 1


# exercise: find the average of 5 numbers using a while loop
arr = [3, -9, 8, 1, 4, 55, 6]
nums = len(arr) # = 5
num_sum = 0
i = 0
while i < nums:
    num_sum += arr[i]
    i += 1

answer = num_sum/nums #average = sum/(number of numbers)
print(answer)


# for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print(" CONTINUE ")
for x in "orange":
    if x == "n" or x == "g":
        continue
    print(x)

print(" BREAK ")
for x in "orange":
    if x == "n" or x == "g":
        break
    print(x)

# range
for x in range(12,4, -1):
    print(x)


# exercise: using a for loop print all the vehicles in the list except for Bus
vehicles = ['Car', 'Cycle', 'Train', 'Bus', 'SkateBoard']
'''

# zip(): combines 2 lists into 1 list element by element

names = ["vallen", "ethan", "karan"]
numbers = [123,69420,17]

for (name, number) in enumerate(zip(names, numbers)):
    print(name, number)

# exercise: go through 2 lists at once
a1 = ['Python', 'Java', 'Scratch']
b1 = [1,2,3]

for i,j in zip(a1,b1):
    print(i,j)



# exercise print a triangle of stars using a for loop and range
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


n = 5
for i in range(0, n+1):
    alksjfljfdfadafdsfdfasdsadsad sd  asdsa dsad asd= cheeztoes dee 