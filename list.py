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