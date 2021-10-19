

def find_largest(list):

    for item in list:
        if item > max:
            max = item

    return max


def set_max(item):
    global max
    max = item
    return max


def find_largest2(list):

    max_list = [set_max(item) for item in list if item > max]
    if max_list == []:
        return max
    else:
        return max_list[-1]


if __name__ == '__main__':
    list = [80, 23, 5, 65, 2, 50, 10, 78, 34]
    max = list[0]
    print(f"Largest number is: {find_largest2(list)}")