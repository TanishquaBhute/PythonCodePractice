fruits = ['Apple', 'Banana', 'Cherry', 'Strawberry']
new_list = [x for x in fruits if "a" in x]
print(new_list)
updated_list = [x if x != 'Banana' else 'Orange' for x in fruits]
print(updated_list)

###########
numbers = (1, 2, 3, 4, 5, 6)
print(type(numbers))

even_numbers = [x for x in range(2, 10, 2)]
print(f"Even Numbers : {even_numbers}")

#############
new_list = [x for x in range(10) if x < 5]
new_list = tuple(new_list)
print(f"List in Tuple form : {new_list}")

#############
letters = [letter for letter in "human"]
print(letters)

#############
num_list = [y for y in range(100) if (y % 2 == 0) and (y % 5 == 0)]
print(num_list)

#############
