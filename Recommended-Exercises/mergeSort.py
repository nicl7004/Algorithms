
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

a = [20,21,22]
b = [2,4,6,7,8,10,22]



def mergeBetter(a,b):
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        elif a[i] == b[j]:                      #part of assignment 1
            print("sucess!", a[i], "=", b[j])
            i+=1
        else:
            c.append(a[i])
            i+=1
    print("no matches")
    # while i<len(a):
    #     c.append(a[i])
    #     i+=1
    # while j < len(b):
    #     c.append(b[j])
    #     j+=1
    return c

def swap(a):
    x = a[0]
    a[0] = a[1]
    a[1] = x

    return a

def mergeFaster(a,b):
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

def baseCase(a,l,u):
    if a[l]>a[u]:
        return(swap(a))


def mergeSort(a,l,u):
    if (u-l +1)<=2:
        return baseCase(a,l,u)
    mid = int((l+u)/2)
    mergeSort(a,l,mid)
    mergeSort(a, mid+1, u)
    c = a[l:mid]
    d = a[(mid+1):u]
    mergeFaster(c,d)

a = [1,10,4,2,40,6]

print(mergeSort(a,0,5))