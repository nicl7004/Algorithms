
#attempt to merge in a single while loop
def merge(a,b):
    i = j = 0
    c = []
    while len(c)<=(len(a)+len(b)):

        if (i) >= (len(a)):
            c.append(b[j])
            if (i) > (len(a)-1) and (j) > (len(b)-1):
                print("return")
                print(i,"i",j,"j")
            return c
            j+=1
        elif (j) >= (len(b)):
            c.append(a[i])
            if (i) > (len(a) - 1) and (j) > (len(b) - 1):
                print("return")
                print(i, "i", j, "j")
                return c
            i+=1
        print("i =", i, "j =", j)
        if a[i]<b[j]:
            c.append(a[i])
            i += 1
            print("a[i]<b[j]")
        else:
            c.append(b[j])
            j+= 1
            print("b[j]<a[i]")

        print('all the way')
    return c

a = [1,3,5,7]
b = [2,4,6,8,10,12]

print(merge(a,b))

def mergeBetter(a,b):
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j < len(b):
        c.append(b[j])
        j+=1
    return c

print (mergeBetter(a,b))
