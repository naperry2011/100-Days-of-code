# This section we are going to go over loops. This is the point where I usually give this up stop putting in work for tech but not this time!!! I WILL KEEP MOVING FORWARD!!!!

# for loop
magicians = ['alice', 'david', 'carolina']
for magicians in magicians: #this is a for loop. This line tells Python to retrieve the first value from the list magicians and associate it with the variable magician. this first value is 'alice'. Python then reads it and post the first variable in the list which is 'alice' and since there are more variables in the list python will go through the entire list until it is finished. 
    print(magicians)
# The concept of looping is important because it's one of the most common ways a computer automates repetitive tasks

# Now let's create our own loops. Doing more with our loops! You made this Perry be proud of it!!!
dogs = ['german shepherd', 'bulldog', 'poodle', 'french bulldog', 'south african mastiff', 'rottweiler']
cats = ['siamese cat', 'bombay cat', 'devon rex', 'russian blue', 'scottish fold', 'egyptian mau']

for cats in cats:
    print(f"I truly hate {cats.title()} but they are good for people who love any breed of cats")
for dogs in dogs:
    print(f"{dogs.title()} are great family dogs.")