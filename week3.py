#everyone print your own version of material you want to find out. Ask for ages of parents, year they were born in, etc.
age = int(input("How old are you? ")) #students struggle with this notation. Go over it a few times with different examples.
if age > 17:
	print("Do 10 jumping jacks")
elif age => 16 and age <= 17:
	print("Do 5 push ups")
else: 
	print("You're stil a baby. You can stay seated")


#in this example go over google and how to google. Make different studetns look up how to .upper, .lower, how to capitalize the whole world, etc. 
#this is a common software problem of a coding assignemnt not having enough explanation as to what types of code is desired. 
pet = print("Do you own a cat, dog, or neither")
if pet == "dog":
	print("Woof!")
	name = input("What is your dog's name")
elif pet == "cat":
	print("Meow")
	name = input("What is your cat's name")
else:
	print("You're missing out")
if pet == "dog" or pet == "cat":
	print("Say hi to" + pet + "for me") #this command goes over strings
	
