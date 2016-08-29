

def merge(a,b):
    i = j = 0
    c = []
    while len(c)<(len(a)+len(b)):
        if (i) >= (len(a)-1) and (j) >= (len(b)-1):
            return c
        elif (i) >= (len(a)-1):
            c.append(b[j])
            j+=1
        elif (j) >= (len(b)-1):
            c.append(a[i])
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


    return c

a = [1,3,5,7]
b = [2,4,6,8]

print(merge(a,b))