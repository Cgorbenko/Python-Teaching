#Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

#What if we want to exit the loop if i is 3?

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

"""
Learning check:	Make a loop that will loop the amount of times a person wants it to
Terminate the loop if that number is more than 20
"""

#What if I want it to print all the numbers except for 3. How do we do that?


i = 1
while i < 6:
  if i != 3:
    print(i)
  i += 1

#there is another way to do that which is a little more legible and nice to understand
#Let's learn the continue 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


"""
Let's code a program together
"""
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

#############################OUTPUT###################
#Enter a number: 10
##The sum is 55


"""
Let's build a project: write a guessing game. Make a program randomly pick a number. Google how to do that. That play lower or higher until the person guesses the number
"""

"""
Write a program to guess the word. Make a list of your favorite sports, toys, games, etc
Then make the person guess what it is by letter. the word must not have repeats of any letters
ex: tag, game
not allowed: soccer 
"""


word = "tag"
guesses = 20
print(len(word))
while guess < 20:
	letter = input("Guess a letter")
	if letter == word:
		print("You win! You guessed the word")
		break
	if letter in word:
		print("letter" + letter "is in word")
	else:
		print("letter is not in word")
print("you lose. Better luck next time.")
