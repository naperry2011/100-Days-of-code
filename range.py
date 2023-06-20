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
print(games[0:3])