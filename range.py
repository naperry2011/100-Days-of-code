# Making numerical lists

for value in range(1,15): #for range() you must add a colon after and the print must be indented
    print(value) #this print value will print the numbers 1-14 but not 15. 
    
even_numbers = list(range(2, 11, 2)) # the first 2 is the start of the range, the 11 is the end of the range and the 2 is what we are going to add each time from the range 2-11. This will give us our even numbers
print(even_numbers)

# Now we're going to do a square [] range
squares = []
for value in range(1, 11): #here we are giving the value in the range which is 1-11
    square = value ** 2 # here the value(1-11) will be squared 
    squares.append(square) 
print(squares)

square_two = [value**2 for value in range(1,30)] #this does what the top does but just compressed into simple terms
print(square_two)

# slicing a list. 

games = ['fable', 'starfield', 'persona 3', 'spider-man 2', 'metal gear solid remake', 'phantom blade 0']
print(games[0:3]) #this will show 0-2 but not the 3 option which is spider-man 2 


games2 = ['person 5 royal', 'persona 4 golden', 'final fantasy 14 online', 'pokemon sword & shield', 'zelda', 'metro prime 4']
print(games2[:3]) # without putting a starting point python will automatically start at the beginning of the list

# Looping Through a Slice
# So here we will create a list then we will have it loop and when will then print the player with a title name
players = ['Joel', 'Mario', 'Batman', 'Master Chef', 'Kratos', 'Zeus', 'Crash']
for player in players[:3]: # Like I've stated in the slicing a list if we don't have a statement in front of the : python will automatically read the list from the beginning
    print(player.title())
    
# copying slice list
my_foods = ['chicken tacos', 'chicken burritos', 'cookies', 'sushi']
friends_food = my_foods[:]

# Now let's add some extra food to each list. Reminder to code runs in order. If you want to add an item to the list make sure it's done prior to the print statement 
my_foods.append('pb&j')
friends_food.append('ribs')

print("My favorite foods are:")
print(my_foods)

print("My friends favorite foods are:")
print(friends_food)

