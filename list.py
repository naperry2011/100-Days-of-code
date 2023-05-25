# Here we're going to learn about list. Lists allow you to store set of information in one place, whether you have just a few items or millions of items. List are one of python's most powerful features readily accessible to new programmers like myself

# bicycles.py 
# how the items are numbered in list is that they start off at 0. so in the text below it goes: 0,1,2,3 which = 4 items
bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles)

# now let's print off one of those bicycles by itself by the number it's represented by
bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[2])
# as you can see that 2 is represent by the 3 item you see because in python listed items start off with 0.

# now we will create an grocery list. We will print off the 2nd item in the grocery list and we will also print off the 4th item on the list but it will be in title form and the last item will be the 9th item that will be in all capital letters.
groceries = ['apples', 'oranges', 'pears', 'turkey', 'bread', 'milk', 'eggs', 'spinach', 'rice', 'yogurt', 'olive oil', 'cheese', 'chicken breast']
print(groceries[2])
print(groceries[4].title())
print(groceries[9].upper())

# now in this section will will create a message that will greet a person then we will have them grab a specific item

first_name = "nicholas"
last_name = "wilson"
full_name = f"{first_name} {last_name}"

movies = ['spirited away', 'your name', 'samurai x']
games = ['god of war', 'spider-man', 'destiny 2']

print(f"Hey, {first_name.title()} can you please grab {movies[0].title()} and can you please remember to grab {games[2].title()}. I am so serious please do not forget to grab {movies[0].upper()} and {games[2].upper()}!!! ")

# the text above is my own code that I wanted to try and create and it worked!!!! Proud of me lol. But yes we made 5 variables with 2 of that variables having a list in them. In the text I made sure to not only pick up those specific items I also informed the person to make sure he grabs those same items with some extra love to it

# Changing,Adding and Removing Elements in a List
# here we're going to replace the first item with another. So when changing an element in a list you post the variable.[the location of element] = 'the changed element'
rappers = ['Twista', 'Snoop', 'Tupac']

rappers[0] = 'Biggie'
print(rappers[0])

# Next we will be adding an element to the list
# To add an item to an list you have to put the variable.append. append('new item') is the trigger to add an element to your list. 
# you can also add an item in any position you want so the code for that will be <variable>.append (position, new variable)
footballTeams = ['Eagles', 'Titans', 'Colts']
footballTeams.insert(0, 'Patriots') #here we added an item and then put it at the beginning of the list
footballTeams.append('Raiders') #here we added an item which would automatically be added to the end of the list
print(footballTeams)
print(f"Hey, {first_name.title()} didn't you tell me that your favorite team was the {footballTeams[0].title()}? Also don't you like listening to {rappers[2].title()}?")


# Removing items using the del Statement
# Here we deleted the element in the 1 position and added a new item to it. To remove an item you put del<variable>
superheros = ['batman', 'flash', 'superman']
del superheros[1] #deleted the superhero in the list in position 
superheros.append('wonder woman') #added another item to the list that will be added towards the end. 
print(superheros)

# Removing an Item Using the pop() method