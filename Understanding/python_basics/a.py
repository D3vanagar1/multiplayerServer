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