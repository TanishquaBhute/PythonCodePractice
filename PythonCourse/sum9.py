print("How many 4-digit numbers have a sum of digits of 9?" )
list4d9 =[]
for num in range(1000,10000):
    sn = str(num)
    listsn = []
    for k in range(4):
        listsn += [int(sn[k])]
    if sum(listsn) == 9:
        list4d9 += [num]
print( "" )
print ("Here is the list:")
print (list4d9)