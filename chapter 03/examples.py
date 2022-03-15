# Chapter 03
# Starting out with python 5th edition
# By: Hossam Hamdy
#----------------------------------------------------------------#
# single alternative decision structure. 
x = 50
if x % 2 == 0:
    print("Is even number")
print("the end") # main path


# A dual alternative decision structure
x = 50
if x % 2 == 0:
    print("Is even number") # first alternative path
else:
    print("Is odd number") # second alternative path
print("the end") # main path
#----------------------------------------------------------------#

#check toxic girls name
name = input("Enter the name: ")
if "Enjy ahmed" == name:
    print("She is toxic")
else:
    if "Gehad essam" == name:
        print("She is toxic")
    else:
        if "Takwa ahmed" == name:
            print("She is toxic")
        else:
            print("She is good")


# Better what using if-elif-else
name = input("Enter the name: ")
if name == "Enjy ahmed":
    print("She is toxic")
elif name == "Gehad essam":
    print("She is toxic")
elif name == "Takwa ahmed":
    print("She is toxic")
else:
    print("She is good")

# most better?
name = input("Enter the name: ")
toxic_names = ["Gehad essam", "Enjy ahmed", "Takwa ahmed"]
if name in toxic_names:
    print("She is toxic")
else:
    print("She is good")

# if-elif-elss is better than nested if else :)

# 1-The code can grow complex and become difficult to understand.
# 2- Because of the required indentation,
# a long series of nested if-else statements can become too long to
# be displayed on the computer screen without horizontal scrolling.

#----------------------------------------------------------------#

# Comparing Strings
# Based on ASCII value for each character :)
# "Mary" > "Mark"
# >>> True



#----------------------------------------------------------------#
#
## Boolean variable
#

dark_mode = True # flag variable

if dark_mode:
    print("Light mode is on :)")
    dark_mode = False
else:
    print("Dark mode is on :)")
    dark_mode = True
#----------------------------------------------------------------#