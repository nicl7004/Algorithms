
a = [12,17,300,5,13]
x = 3
def findMin(a,x):
    i = 0
    min = a[i]
    while i <=(x-1):
        if a[i]<min:
            min = a[i]
        i+=1

    return min

print(findMin(a,x))


def makeArray(a,x):
    each = 1
    b = []
    while each <= x:
        b.append(findMin(a,each))

        each += 1
    return b
y = makeArray(a,x)
print(y)
