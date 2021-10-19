lst = [1, 5, 3, 7, 9]
summ = 10
result = []
while lst:
    num = lst.pop()
    diff = summ - num
    if diff in lst:
        result.append((diff, num))
print(f"Pairs from the list with summation {summ} are :{result}")
