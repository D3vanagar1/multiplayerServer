# Overview of everything

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
c = a + " " + b #concatination
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