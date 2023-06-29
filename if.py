# Today we will be working on if statements 
# Python symbols (less than or equal <=) (greater than or equal >=) (equals ==) (Not equal !=)
# Modulo Operator (addition +) (subtraction -) (Multiplication *) (Division /)(Modulus %)(Exponent **) (// Floor Division)

# Example
# car.py
cars = ['audi', 'bmw', 'subaru', 'toyota'] #list of cars
for car in cars: # our for() loop
    if car == 'bmw': # here we are stating if the car is == to bmw then we will have the give the print() statement below
        print(f"Damn an individual who loves {car.upper()} and has class has stepped in the building") 
    else: #if the the answer or the car isn't bmw then we will provide the print statement below
        print(f"Well I guess a {car.title()} is alright but you can do better")
        

# toppings.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the damn anchovies!!!")
    

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


