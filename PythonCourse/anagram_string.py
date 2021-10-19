str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
# count = 0
# if len(str1) == len(str2):
#     for ch in str1:
#         if ch in str2:
#             count += 1
#         else:
#             break
#     if count == len(str1):
#         print("Strings are Anagram")
#     else:
#         print("Strings are not Anagram")
# else:
#     print("Strings are not Anagram")


# print("Strings are Anagram") if len([ch for ch in str1 if ch in str2]) == len(str2) else print("Strings are not Anagram")


# check_anagram = lambda str1, str2 : len([ch for ch in str1 if ch in str2]) == len(str2)
# print(check_anagram(str1, str2))


check_anagram = lambda str1, str2: sorted(str1) == sorted(str2)
print(check_anagram(str1, str2))




