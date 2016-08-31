
a = [12,17,300,5,13]
x = 5
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

def findProfit(big,small):
    x = 0
    profit = big[0]-small[0]
    while x<len(big):
        tmp = big[x]-findMin(big,x)
        if tmp>profit:
            profit = tmp
        x += 1
    return profit

profit = findProfit(a,y)
print (profit)
