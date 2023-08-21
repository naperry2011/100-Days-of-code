# User inputs and While loops!!!

# parrot.py
message = input("Tell me something, and I will repeat it back toy you: ")
print(message)

# Even_or_Odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even. ")
else:
    print(f"The number {number} is odd. ") 
    
    
# Rental_Car.py
car = input("What type of car are you looking for? ")
print(f"{car.title()} that's an interesting car but I don't believe we have those, let's check to see if we have a Subaru.")

# Restaurant_Seats.py
name = input("Enter name: ")
seats = input(f"Good Evening {name.title()}, how many people will you have dinning with you this evening? ")
seats = int(seats)

if seats > 8:
    print(f"That will be a 10-15 min wait {name.title()} ")
else:
    print(f"Your table is now ready {name.title()}, please right this way ")
    
# Now let's practice while loops.
# The for loop takes a collection of items and executes a block of code once for each item in the collection. In contras, the while loop runs as a long as or while, a certain condition is true
# While loop in action: You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1-5
# counting.py

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# Letting the User choose when to quit
# This program will run as long as the user wants by putting most of the program inside a while loop. We'll define a quit value and then keep the program running as long as the user has not entered the quit value

# parrot2.py

prompt = "Tell me something, and I'll repeat it back to you: "
prompt += " Enter 'quit' to end the program. "

talk = ""
while talk != 'quit':
    talk = input(prompt)
    print(talk)
    
    
# Using a Flag
# cities.py
prompt = " \nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")