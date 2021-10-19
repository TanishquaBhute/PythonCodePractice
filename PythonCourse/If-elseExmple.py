''' Program to check number is positive, zero or negative
num = int(input("Enter any number :"))

if num > 0:
    print(" Number is positive")
elif num == 0:
    print("Number is Zero")
else:
    print(" Number is negative")'''

'''Compare two different numbers
num1 = float(input("Enter any number:"))
num2 = float(input("Enter another number"))
if num1 > num2 :
    print("{} is greater than {}".format(num1, num2))
elif num1 == num2:
    print("Numbers are equal")
else:
    print("{} is greater than {}".format(num2, num1))'''

'''#Print the message once condition is false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")'''
# Print list if condition is true
fruits = ["apple", "banana", "cherry"]
i=0
while i < len(fruits):
    print(f"{i} : {fruits[i]}")
    i += 1



