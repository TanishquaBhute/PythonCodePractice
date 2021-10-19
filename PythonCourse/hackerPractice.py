# if __name__ == '__main__':
#    # n = int(input())
#     arr = map(int, input().split())
#     lis = list(arr)
#     print(lis)
#     z = max(lis)
#     print(f"Winner : {z}")
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print(f"first runner up : {max(lis)}")
#
# y = max(lis)
# while max(lis) == y:
#     lis.remove(max(lis))
#
# print(f"Second Runner up : {max(lis)}")
#
# x = min(lis)
# print(x)

# store_item = dict()
# for _ in range(int(input())):
#    # key,_,value = input().rpartition(" ")
#     key,value = input().split(" ")
#     store_item[key] = store_item.get(key,0) + int(value)
# for k,v in store_item.items():
#     print(k,v)

# lis=[]
# for _ in range(int(input())):
#     command, *value = input().split()
#     if command == 'print':
#         print(lis)
#     else:
#         #getattr(lis,command)(*(map(int, value)))
#         exper = "lis.{}({})".format(command,','.join(value))
#         eval(exper)
#     # eval("lis.append(123)")

# import textwrap
#
#
# def wrap(string, max_width):
#     return "\n".join(textwrap.wrap(string, max_width))
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
#
# # number printing in decimal octal hex and binary
# def print_formatted(number):
#
#     width = len("{0:b}".format(number))
#     print(f"Width {width}")
#     for i in range(1, number+1):
#         print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))
#
# if __name__ == '__main__':
#     n = int(input())
#     print("{0:.2f}".format(10.234567))
#     print("{i:b}".format(i=18))
#     print_formatted(n)


import string


def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# n = int(input())
# for i in range(n):
#     a = int(input())
#     set1 = set(input().split())
#     b = int(input())
#     set2 = set(input().split())
#     print(set1.issubset(set2))
