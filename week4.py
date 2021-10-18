# Examples (do not show this file), code it out with students in separate file

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3, 5, 4]

# list with mixed data types
my_list = [1, "hi", 3.2]




# List indexing 
"""
Ask questions about what they think will be the output. This is a fun way to cover the material
Ask each student one by one. In a class this could be prticipation points, here it's just fun
"""

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list) # ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o

print(my_list[4]) # e


print(my_list[-1]) #e

print(my_list[-5]) #p

"""
#knowlege check
Now let's practice. Make each student make a list of different things (things they like) at least 3 elemebts
Print the the first, middle, last items
"""


"""
#knowlege check
What if you had a very long list? How woudl you find the length of the list? Make students google. 
Make it into a competetion, 
print(len(my_list))
"""

#how to index slice
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#index until the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


"""
#knowlege check
Let's have a real world example. You have an alphebet list and want to make rows and columns. Make first 9 letters and print them all in rows of 3.
"""

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])



# nested list
my_list = ["mouse", [8, 4, 6], ['a']]



"""
#knowlege check
Make a list of favorite items, let's print first letter of the list. Go over how you do it, but first
let students try to learn themselves on line as an internet challenge. 
Write an if else statement for the code to show the first letter of the word then try to guess what it is. repeat this three times. Explain how annoying it is to copy code, so next week we will learn while loops
"""

#check if apple is in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

"""
#knowledge check
make an activity list of fun events. write a loop to check if your favorite event is in the list. 
Swap lists with another person and see if your favorite event is in their list
"""

#changing items in a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""
google check
#have top code, 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
"""
