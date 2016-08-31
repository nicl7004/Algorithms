
a = [12,17,300,5,13,2,80,1]
x = 3
def findMin(a,x):
    i = 0
    min = a[i]
    while i < (x):
        if a[i]<min:
            min = a[i]
        i+=1
    return min

print(findMin(a,x))
