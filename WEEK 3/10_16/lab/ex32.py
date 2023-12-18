# 1a) Write a Python function to find the maximum of three numbers
# NOTE: do not utilize built-in functions to accomplish this
# instead, opt for conditionals
def max(a,b,c):
    maximum=0
    if(a>b):
        if(a>c):
            maximum = a


# 1b) use this function to find the max of the 3 vars below
a = float("inf")
b = float("-inf")
c = 100000000
max(a,b,c)


# 2a) Write a Python program to reverse a string
#Confused about this one, ask 

# 2b) Use this function to reverse the string saved in the name below
word = "racecar"
...


# 3a) Write a Python function to multiply all the numbers in a list.
def func3(lst):
    newlist = [x*x for x in lst ]
    return newlist
    
# 3b) Use this function to find the product of the list below
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
func3(nums)


# 4a) Write a Python function that finds the maximum value of a list
# NOTE: do not use built-in Python functions. Instead use a for-loop and
# a conditional
def MaxinList(lst):
    for x in lst:


# 4b) Use this function to find the product of the list below
nums = [100, 491, 592, 58, 3, 59, -100]
MaxinList(nums)