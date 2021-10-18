#Class, do you remember last week we learned while loops? We are now going to learn what a for loop is. This is similar to a while loop, and does bsaically what a while loop does, but it is structurally a little different and can be used for different things. 

# let's print out each fruit in a list
###### GO THROUGH EVERY LINE TO MAKE SURE STUDENTS UNDERSTAND EACH LOOP

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#now with a while loop we would've had to use list indexing. With for loops it's much more simple and we don't have to do that! 

#Here is another example. We can loop through all the letters in the word candy. 

# does anyone have any guesses of how to do that?
###### GO THROUGH EVERY LINE TO MAKE SURE STUDENTS UNDERSTAND EACH LOOP

for x in "candy":
  print(x)


#Knowledge check: Let's make sure we still remember while loops. Print all letters in your name using a while loop. Now lets do it with a for loop. Which was faster/easier?


#Do you remember we learned break statements?  Give an example using a while loop. 
#Now lets break whem x is banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Kowledge check: Let's do the same but with continue. Can you code a while loop and skip banana? Looking at your code can you code a for loop using continue?

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Remember in while loops we had a counter? You can do that in a for loop too! 

#Using the range() function:

for x in range(6):
  print(x)
###### GO THROUGH EVERY LINE TO MAKE SURE STUDENTS UNDERSTAND EACH LOOP

#We can also do different ranges
for x in range(4, 20):
  print(x)

#the Range function actually has a hidden parameter in it.
for x in range(2, 30, 3):
  print(x)

#here is another great way to use loops. ####GOES THROUG EVERY LINE!!!!!
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#can you think of another example we might need a double for loop? Let's code it out together!

#For debugging purposes, or if you're not sure what will go in the section yet, you can always use a pass
for x in [0, 1, 2]:
	pass


