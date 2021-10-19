age = 10
name = "My name is\tTanishqua"
cf = name.casefold()
print(cf)
c = name.center(50, '#')
# print(c)

# name = ['My','name','is','Tanishqua']
newName = ' '.join(name)
# print(newName)

#print(name.count('My'))
#print(name.split('name'))
#print(name.endswith('Tanishqua'))
#print(name.expandtabs(10))
#print(name.expandtabs(10))
name = ' Tanishqua'
course = 'Python'
#print("Hello {} Welcome to {} course".format(name,course))
#print(name.istitle())
str="Tanishqua"
for ch in str :
    index= str.index(ch)
    print(f"index of {ch} is {index}")

new_str = str.replace('a','x')
print(new_str)

string = "Tanishqua Bhute 29"
new = ''
for ch in string:
    if ch == ch.upper():
        new += ch.lower()
    else:
        new += ch.upper()
print(f"Swapcase string::{new}")
#HACKER_PRACTICE SUBSTRING COUNT
str1 = "ASDFGHQWERTASDFBHASDF"
substr = "ASDF"
count = 0
print(len(substr))
print(str1[11:11+len(substr)])
for i in range(len(str1)):
    # if str1[i:].startswith(substr):
    #     count += 1
    if str1[i:i+len(substr)] == substr:
        count += 1
print(f"{substr} occurance in {str1} : {count}")

#HackerPractice

s = 'Asdf29'
print(any([ch.isalnum() for ch in s]))
print(any([ch.isalpha() for ch in s]))
print(any([ch.isdigit() for ch in s]))
print(any([ch.islower() for ch in s]))
print(any([ch.isupper() for ch in s]))
