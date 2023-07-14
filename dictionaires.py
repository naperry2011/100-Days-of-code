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

language = favorite_language['Sara'].title()
print(f"Sara's favorite language is {language}")

# Favorite_food.py
# Looping through key pairs.
# The code tells python to loop through each key-value pair in the dictionary. 
favorite_food = {
    'Sarah': 'tacos',
    'Derrick': 'pizza',
    'Nick': 'sushi',
    'Olivia': 'crackers'
}
food = favorite_food
for name, food in favorite_food.items():
    print(f"{name.title()}'s favorite food is {food.title()}.")
    
    
# A list of dictionaries 
# Make an empty list for storing aliens

monsters = [] # this is setting up the empty dictionary for monsters

# Make 30 blue monsters.
for monster_number in range(30): # here we will set a the range for how many we want to make 
    new_monster = {'color': 'blue', 'points': 20, 'speed': 'medium'} #this will make the the set of monsters to have the same set blue color/ speed medium/20 points
    monsters.append(new_monster) #add a new monster


# Let's change the first 3 monsters
# we are going to change the monster 0-2 to be green worth 10 points that are fast.
for monster in monsters[:3]: #setting the for statement
    if monster['color'] == 'blue': # the if statement is pointing to any monster == green to change them in the first 3 sections
        monster['color'] = 'green'
        monster['points'] = 10
        monster['speed'] = 'fast'


# Show the first 7 monsters.
for monster in monsters[:7]:
    print(monster)
print("...")

# Show how many monsters have been created
print(f"total number of monsters: {len(monsters)}")


# A dictionary in a dictionary 
# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do. 
# many_users.py

users = {
    'dmason':{
        'first': 'derrick',
        'last': 'mason',
        'location': 'indianapolis',
        },
    'jperry':{
        'first': 'jordan',
        'last': 'perry',
        'location': 'atlanta',
    },
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"Full name: {full_name.title()}")
    print(f"location: {location.title()}")
    
# In Python's for loop syntax, the loop variable on the left side of the in keyword (in this case, username) represents the individual keys of the dictionary users during each iteration of the loop. The loop variable takes the value of each key in the dictionary, one by one, as the loop iterates over the items in the dictionary.

# So, in the line for username, user_info in users.items():, the loop variable username is created automatically and assigned the current key (username) from the users dictionary. It allows you to access and use the username within the loop block, such as when it is printed in the subsequent line print(f"Username: {username}").
