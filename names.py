#this will be an example of a string
# So here we are showing the print() + other commands within it
# name is the variable that represents ada so in the the print we want the name + title form so print(name.title()) this will give us the result of Ada Lovelace

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# full_name.py 
# here we are going over f strings. f stands for format, because Python formats the string by replacing the name of any variable in braces with its value. To insert a variable's value into a string, place the letter f immediately before the opening quotation mark. Put braces {} around the name or names of any variable you want to use inside the string
first_name = "lacy"
last_name = "ladylove"
full_name = f"{first_name} {last_name}"
print(full_name.title())

# now let's put some text before the full name and have it print out so we will take the text from above and change the name and the print value. In the print() we wanted it to say Hello, Jasmin Perry! for that function to run correctly in print(f"<some text>{the variables you created}")
first_name = "jasmin"
last_name = "perry"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


# now we're going to have the text above be a message variable then have print(message)

first_name = "kelli"
last_name = "perry"
full_name = f"{first_name} {last_name}"
message = (f"Hello, {full_name.title()}!")
print(message)