"""
This week we will be learning about functions. Functions are a set of instructions bundled together to achieve a specific outcome.
"""

#here is an example of a function
def my_function():
  print("Hello from a function")

#the way to call a function is
my_function()


#One can also place arguments into a function
def my_function(name):
  print(name + " hello")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


#we can also have multiple arguments. in the following example we have two
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#sometimes the amount of variables is not known. In these cases you can add a *
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#in order to make code more legible you can state what each is equal to
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#you can also have a predifined argument
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

#E.g. if you send a List as an argument, it will still be a List when it reaches the function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#many functions have return statements instead of prints
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
