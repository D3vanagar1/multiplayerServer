'''
#example
#print all parts of list
ll = [1,2,3,4,5]
for i in ll:
    print(i)


# for loops
# add all parts of list with a for loop
ll = [5,4,6,9,-1,3]

c = 0
for i in ll:
    print(i)


# exercise:
# find the word "cheese" in the string (return index)
st = "my cheese fell on the ground"
print(st)
print(st.find("cheese"))


# list exercises

# 1. reverse a list
list1 = [100, 200, 300, 400, 500]

result = [500, 400, 300, 200, 100]
list1.reverse()
print(list1)



# 2. add two list by index
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = ['My', 'name', 'is', 'Kelly']


# 3. Turn every item in list into its square
numbers = [1,2,3,4,5,6,7,8] #result: [1,4,9,16,25,36,49,64]
#hint use for loop
for applebellybuttonjuicybiscuits in numbers:
    print(applebellybuttonjuicybiscuits*applebellybuttonjuicybiscuits)




# 4. remove empty string from list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"] # result: ["Mike", "Emma", "Kelly", "Brad"]
list1.remove("")
list1.remove("")
print(list1)
'''


# 5. replace item(20) with new value (250)
list1 = [5, 10, 15, 20, 25, 50, 80] #result: [5, 10, 15, 250, 25, 50, 20]
#hint: used index()