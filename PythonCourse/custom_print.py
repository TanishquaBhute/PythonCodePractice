def print_ch(ch):
    global count
    if count == brk:
        count = 0
        print('\n', ch, end='')
    else:
        print(ch, end='')
        count += 1
    return ch, count


string = input("Enter any string:")
brk = 10
count = 0

[print_ch(ch) if count == brk else print_ch(ch) for ch in string]


# for ch in string:
#    # print(string.index(ch))
#     if count == brk:
#         count = 0
#         print("\n", end='')
#     else:
#         print(ch, end='')
#         count += 1
#


# def print_ch(ch):
#     if string.index(ch)%brk == 0:
#         print("")
#     print(ch, end='')
#     return ch


# [print("\n",ch, end='') if string.index(ch)%brk == 0 else print(ch,end='') for ch in string]
