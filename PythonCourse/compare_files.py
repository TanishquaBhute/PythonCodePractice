from difflib import Differ

with open('file1.txt') as file_1, open('file2.txt') as file_2:
    differ = Differ()
    data1 = file_1.read()
    data2 = file_2.read()
    for word in differ.compare(data1.split(' '), data2.split(' ')):
       # print(word)
       pass
    same = set(file_1).intersection(file_2)
    for word in same:
        print(word)
