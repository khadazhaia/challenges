import math

# 1) Given this list, access the "hello" element using multi-dimension indices
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

# print(lst[3][1][2][0])

"""
2) You are driving a little too fast, and a police officer stops you. Write a
function to return one of 3 possible results: "No ticket", "Small ticket", or
"Big Ticket". If your speed is 60 or less, the result is "No Ticket".
If speed is between 61 and 80 inclusive, the result is "Small Ticket".
If speed is 81 or more, the result is  "Big Ticket". Unless it is your
birthday (encoded as a boolean value in the parameters of the function)
 -- on your birthday, your speed can be 5 higher in all cases.
"""


def caught_speeding(speed, is_birthday):
    if is_birthday == False:
       if speed <= 60:
           ticket = "No ticket"
       elif speed > 60 and speed <= 80:
           ticket = "Small ticket"
       else:
           ticket = "Big ticket"
    else:
        if speed <= 65:
           ticket = "No ticket"
        elif speed > 65 and speed <= 85:
           ticket = "Small ticket"
        else:
           ticket = "Big ticket"
    return ticket
           
# print(caught_speeding(81, True))
# print(caught_speeding(81, False))


# 3) Create a function called "emailer" which takes a string and concatenates "@gmail.com" to
# this string before returning it
def emailer(word):
    if word == " ":
         str = input("Please enter a string: ")
         email = "@gmail.com"
         return str + email
    else:
         return word

# print(emailer("test@gmail.com"))
# print(emailer("gmail@gmail.com"))
# print(emailer(" "))


# 4a) Create a function called "areacirc" that takes in a radius and
# calculates the area
def areaCirc(rad):
    return round(math.pi * (rad ** 2), 4)

# 4b) use this function to calc the area of a circle with a radius of 5
# (answer should be ~78.5398)
# print(areaCirc(5))

# 5a) Create a function that converts kilometers to miles
# there are roughly 1.61 km in one mile
def kilo_to_miles(kilo):
    return kilo * 1.61
    
# 5b) use this function to convert 10km to miles
print(kilo_to_miles(10))
