l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

#print(l)
print(','.join(l))

#Factorial Program


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input("\nEnter any positive no.:"))
print(f"Factorial of {x}  is: {fact(x)}")

##################
d = dict()
for i in range(0, 4):
    d[i] = i*i
print(d)

