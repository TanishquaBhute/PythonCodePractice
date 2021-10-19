def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function (child1 = "Suhas", child2 = "Harshad", child3 = "Manoj")

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname = "Manoj", lname = "Godbole")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple","banana","cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)