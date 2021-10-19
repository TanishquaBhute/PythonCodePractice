
list = [10, 22, 28, 29, 30, 40]
taregt_sum = 54
dictionary = {}
for i in range(len(list)):
    for j in range(i+1, len(list)):
        sum = list[i]+list[j]
        diff = taregt_sum-sum
        dictionary[diff] = [list[i], list[j]]

#print(dictionary)
sorted_dictionary = dict(sorted(dictionary.items())) #dictionary sorted in descending order
#print(sorted_dictionary)

sorted_dictionary_keys = [*sorted_dictionary.keys()]
#print(sorted_dictionary_keys)
positive_sorted_dictionary_keys = [item for item in sorted_dictionary_keys if item >= 0]
#print(positive_sorted_dictionary_keys)
#positive_sorted_dictionary_keys[0]
print(f"{dictionary[positive_sorted_dictionary_keys[0]]} is the pair and its addition is closest to {taregt_sum}" )






#print(dictionary.keys())
#print(dictionary.values())
# list_keys = [*dictionary.keys()]  #list form of keys in dictionary
# print(list_keys)
# sorted_keys = list_keys.sort(reverse=True)
# print(sorted_keys) # not working
