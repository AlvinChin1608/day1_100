# Write your code below this line 👇
print("Hello World")
print('She said: "Hello" and then left.')
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

print("Hello World!\nHello World!\nHello World!")
print("Hello" + " " + "Alvin")

# the computer will process the input before the print function
print("Hello " + input("what is your name?"))

numOfLetters = len("Angela")
print(numOfLetters)

name = len(input())
print(name)

# Exercise to switch these around
# There are two variables, a and b from input
a = input()
b = input()
# switch the values of a and b
temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be "+ city + " "+ pet)
#5. Make sure the input cursor shows on a new line:
