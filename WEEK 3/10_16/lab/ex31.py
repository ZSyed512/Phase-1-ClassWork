import math

# 1a) Create a function which takes a string and concatenates
# "@gmail.com" to this string before returning it
def emailer(word):
    word.concat("@gmail.com")
    return word


# 1b) call and print this function on your name
emailer("Zaigham")

# 2a) Fix the function below. It should take in a radius and calculate
# the area of a circle (pi * radius ^ 2)
def areaCirc(rad)
    area = math.pi * (rad ** 2)
    return area

# 2b) use this function to calc the area of a circle with a radius of 5
# (answer should be ~78.5398)
areaCirc(5)


# 3a) Create a function that converts kilometers to miles
# there are roughly 1.61 km in one mile
def KmToMiles(km):
    Miles = km/1.61
    return Miles

# 3b) use this function to convert 10km to miles
KmToMiles(10)
