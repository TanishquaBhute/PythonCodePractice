opposite_directions = {'North': 'South', 'South': 'North', 'East': 'West', 'West': 'East'}


def remove_opposites(direction):
        result = []
        list_length = len(direction)
        i = 0
        while i != list_length:
            item = direction[i]
            if i == list_length-1:
                result.append(item)
                break
            else:
                next_item = direction[i+1]
                if next_item == opposite_directions[item]:
                     i += 2
                else:
                    result.append(item)
                    i = i+1
        return result


def check_opposites(list):
    for item in range(len(list)-1):
        first_item = list[item]
        next_item = list[item+1]
        if next_item == opposite_directions[first_item]:
            return True
    return False


directions = ['East', 'West', 'North', 'South', 'West', 'North', 'East', 'West']
result = directions
while check_opposites(result):
    result = remove_opposites(result)

print(result)


'''for item in range(list_length):
    if i == list_length-1:
      break
    else:
while i != list_length:
    zero_item = directions[i]
    if i == list_length-1:
        #final_directions.append(zero_item)
        break
    else:
     first_item = directions[i + 1]
     if first_item != opposite_directions[zero_item]:
       final_directions.append(zero_item)
       final_directions.append(first_item)
       i += 1
     else:
        i += 2

print(final_directions)'''
'''i = 0
j = 0
list_length = len(directions)
while j <= list_length:
    zero_item = directions[i]
    if zero_item == directions[list_length-1]:
        break

    else:
        first_item = directions[i+1]
        if first_item == opposite_directions[zero_item]:
           directions.remove(zero_item)
           directions.remove(first_item)
           i = 0
        else:
            i += 1
    j += 1
print(directions)'''

