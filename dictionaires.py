# Dictionaries will be the focus of this section. We learn how to access the information once it's in a dictionary and how to modify that information
# A dictionary is Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A dictionary can be a number, a string, a list, or even another dictionary 
# alien.py
alien_0 = {'color': 'green', 'points': 5} #here we are giving alien0 a description of green as it's color and points 5. Each key value is made with '' and a colon to have more than one. 
new_points = alien_0['points'] #here we are creating the value new points to point to the points value in alien_0
print(alien_0['color'])
print(alien_0['points'])
print(f"You just earned {new_points} points!!!")


# Alien1 will be begin by giving it the colors and points and then we will add to it. 
alien_1 = {'color': 'blue', 'points': 10}
print(alien_1)
# this will print everything in alien_1 that we first put together
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)
# this will print the add ons to it

# Alien2 will begin with nothing and we will add to it along the way
alien_2 = {}
alien_2['color'] = 'yellow'
alien_2['points'] = 15
print(alien_2)
print(f"The favorite color of Alien 2 is {alien_2['color']} and the favorite color of Alien 1 is {alien_1['color']} and that is worth {alien_1['points']} points!!")

# Let's remove Alien 0 point value
del alien_0['points']
print(alien_0)

# Dictionary with similar Objects
# We're going to make a dictionary for storing results of a simple poll
# favorite_language.py

favorite_language = {
    'Jason': 'python',
    'Sara': 'c',
    'Jasmine': 'ruby',
    'Edward': 'JavaScript'
}

language = favorite_language['Jasmine'].title()
print(f"Jasmine's favorite language is {language}")