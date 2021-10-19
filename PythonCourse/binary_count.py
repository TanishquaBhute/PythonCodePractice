# str = input("Input any binary string :")
# count_list = []
# count = 0
# for i in range(0, len(str)):
#     if str[i] == '0':
#         count += 1
#     else:
#         count = 0
#     count_list.append(count)
#
# print(f"Maximum zeroes :{max(count_list)}")

# def count_zeros(str):
#     # count_list = []
#     # count = 0
#     # for i in range(0, len(str)):
#     #     if str[i] == '0':
#     #         count += 1
#     #     else:
#     #         count = 0
#     #     count_list.append(count)
#     #
#     # return max(count_list)
#
#     return len(max(str.split('1'), key=len))

find_longest = lambda str:len(max(str.split('1'), key=len)) #lambda oneline function without a name
str = input("Input any binary string :")
print(f"Maximum continuous '0's :{find_longest(str)}")

