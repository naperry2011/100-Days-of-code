# this will be my testing ground for do it yourself
# Python symbols (less than or equal <=) (greater than or equal >=) (equals ==) (Not equal !=)
# Modulo Operator (addition +) (subtraction -) (Multiplication *) (Division /)(Modulus %)(Exponent **) (// Floor Division)

# alien.py
# imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of green,  yellow, & red. 
# Write an if statement to test whether the alien's color is green. If it is print a message that the player just earned 5 points
# If the alien is yellow print a message that the player earned 10 points
# If the alien is red print a message that the player earned 15 points
alien_color = ['green', 'yellow', 'red']
color = input("What color do you want? ")
if color == 'green':
    print("You have receive 5 points")
elif color == 'yellow':
    print("You receive 10 points!")
elif color == 'red':
    print("You receive 15 points!")
else:
    print("You receive 0 points")
    
    
# StageOfLife.py
# Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is a baby
age = int(input("How old are you? "))
if age < 2:
    print("You're just a baby.")
elif age >= 2 and age <= 3:
    print("You're a toddler!")
elif age >= 4 and age <= 12:
    print("You're a kid")
elif age >= 13 and age <= 19 :
    print("You're a teenager")
elif age >= 20 and age <=64:
    print("You're an adult")
else:
    print("You're an elder")
    
# Hello_Admin.py
# Make a list of five or more usernames, including the names 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website Loop through the list, and print a greeting to each user:
# step 1 If the username is 'admin' print a special greeting, such as Hello admin, would you like to see a status report? Otherwise print a generic greeting such as Hello Jaden, thank you for logging in again. 

# usernames = ['admin', 'Jason', 'Jackie', 'Jordan', 'Dirk']
# user = input("Welcome, can you please enter your name?")

# if user == 'admin':
#     print("Hello admin, would you like to see status report?")
# elif user in usernames