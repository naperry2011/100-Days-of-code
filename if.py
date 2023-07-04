# Today we will be working on if statements 
# Python symbols (less than or equal <=) (greater than or equal >=) (equals ==) (Not equal !=)
# Modulo Operator (addition +) (subtraction -) (Multiplication *) (Division /)(Modulus %)(Exponent **) (// Floor Division)


# message = input("Tell me something, and I will repeat it back to you: ")
# print( f"Now I will respond with what you put in the input when asked. {message.upper()}")

# Example
# car.py

# List of cars
cars = ['audi', 'bmw', 'subaru', 'toyota'] 
# Prompt for user for favorite car
car_message = input("What's your favorite car? ")

if car_message in cars:
    print(f"{car_message.title()} is a really nice car. I'm happy to assist you with finding that vehicle for you.")
else:
    print("Unfortunately, we can't assist you with you car decision")
        



# input() function pauses our program and waits for the user to enter some text. Once python receives the user's input, it assigns that input to a variable to make it convenient for you to work with 

# message = input("Tell me something, and I will repeat it back to you: ")
# print( f"Now I will respond with what you put in the input when asked. {message.upper()}")

# this will be a practice of mixing if() input()
# games.py
games = ['Final Fantasy 16', 'Zelda', 'Hogwarts','Red Fall'] #list
message = input("What's your favorite game of the year? ") #input
if message in games: #if statement
    print("That's a phenomenal game! I'm glad you enjoyed it!!!")
else:
    print("You need to make better decisions in your life!")
    
    

# Now we will work with if() input() & for()
# BannedNames.py

# list of names
banned_names = ['Lisa', 'Joe', 'David', 'Sara']

# Prompt to ask for name
name_input = input("Enter name for access please:")

# Iterate through each name in the list 
for name in banned_names:
    # check if the name matches the input
    if name == name_input:
        print(f"{name.title()} you are on the banned list. No access for you.")
        break
else: #remember to make sure that the else: isn't indented like the if or elsif because if it is it will continue to loop through the list!
        print(f"{name_input.title()}, your name is not on the banned list, you may proceed.")
        
        
# Voting.py

voter_age = int(input("How old are you? "))
if voter_age <= 18:
    print("You are not eligible to vote, please wait until next year. Please step to the side")
else:
    print("Go right ahead sir/ma'am you may proceed to vote. ")
    
# price.py
buyer_age = int(input("Depending on your age will depend on how much I will charge you, now what's your age?"))
if buyer_age < 4:
    price = 0
elif buyer_age < 18:
    price = 15
else:
    price = 30
print(f"Your total cost is ${price}. Now will that be cash or card? ")


#Using Multiple List
available_toppings = ['mushrooms', 'onions', 'chicken' 'olives', 'green onions', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"When don't have that {requested_topping}")