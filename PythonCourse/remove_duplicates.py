list = [1, "45", 2, 34, 8, 78, 2, 45, 34, 6, 5, 8, 5]
# duplicate_count = {}
# for item in list:
#     duplicate_count[item] = list.count(item)

#print([*duplicate_count]) # print keys of duplicate_count dictionary in list form

#duplicate_count = {item: list.count(item) for item in list}
print([*{item: list.count(item) for item in list}])