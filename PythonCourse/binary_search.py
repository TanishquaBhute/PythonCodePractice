lis = [9, 8, 7, 6, 5, 4, 3, 12, 23, 34, 45, 56, 67, 78, 89, 98, 87, 65, 54, 43, 32, 21]
search_element = int(input("Enter search element: "))
lis.sort()
start_element = lis[0]
end_element = lis[-1]
center_element = lis[int((lis.index(start_element)+lis.index(end_element))/2)]
print(f"sorted list is : {lis}")
while center_element != search_element :
    if center_element > search_element:
        end_element = center_element
    else:
        start_element = center_element

    center_element = lis[int((lis.index(start_element) + lis.index(end_element)) / 2)]

    if lis.index(end_element) - lis.index(start_element) == 1:
        break

# if center_element == search_element :
#     print("{} is at index {} in sorted list ".format(center_element,lis.index(center_element)))
# else:
#     print("Element not in list")
print("{} is at index {} in sorted list ".format(center_element,lis.index(center_element))) if center_element == search_element \
    else print("Element not in list")
