# Chapter 04
# Starting out with python 5th edition
# By: Hossam Hamdy

#----------------------------------------------------------------#
x = 10
while x > 0:
    print(x)
    x -= 1
print("the end")

for i in range(1, 11):
    print(i)
#----------------------------------------------------------------#

#----------------------------------------------------------------#
# students_number is sentinel
students_number = int(input("Number of students: "))

# example 1
while students_number >= 0:
    pass # do some code

# example 2
for i in range(0, students_number):
    pass # do some code
#----------------------------------------------------------------#

#----------------------------------------------------------------#
print("""
Choose your Book:
-----------------
1- Starting out with python 5th edition
2- Clean code
3- Clean code in Python
4- System design and requirements analysis

""")

user_choice = int(input("Enter your choice: "))
while user_choice > 4 or user_choice < 1:
    print("Invalid choice number :)")
    user_choice = int(input("Enter your choice: "))

print(f"\nWe get a valid choice now {user_choice} :)\n")
#----------------------------------------------------------------#

#----------------------------------------------------------------#
for i in range(5):
   for j in range(i + 1):
      print(j + 1, end="")
   print("")
   
# out put
# 1
# 12
# 123
# 1234
# 12345
#----------------------------------------------------------------#