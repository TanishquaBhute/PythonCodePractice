info = [1, 2, 'Tanishqua', 0.98, 7823]
'''print(info.index('Tanishqua'))
#print(info.pop(2))
#print(info)
#info.sort(reverse=True)
#print(info)'''
print(len(info))
info.insert(2,"Bhute")
print(info)
info1 = info[0:2].copy() #  refrence by address
print(info1)
'''info.append('asdf')
print(info)'''
#print(info.count('Tanishqua'))
info.extend(info1)
print(info)
info.remove(1)
print(info)
#nested list
NewList = ["Name", [9, 7, 11, 'Tanishqua'], 345]
element = NewList[1][0]
print(element)
list=[1,2,3,2,4]
list.remove(2)
print(list)
list.sort(reverse=True)
print(list)