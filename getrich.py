import random

print("What is your name?")
name = input()

print ("How old are you?")
age = int(input())

print(f"Hello {name.title()} your are {age} years old. Let's find find out when you will  be a millionaire.")

print("Calculating when you will become rich.")
print("......")
print("*......")
print("**......")
print("*****.......")
print("**************")

numRan =random.randint(0, 14)
richAge = numRan + age
ageDif = richAge - age

print(f"{name.title()} you will be a millionaire at the age of {richAge}. That is {ageDif} years away.")