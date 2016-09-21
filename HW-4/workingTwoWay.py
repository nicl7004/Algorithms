from random import randint

def swap (a,i,j):
    (a[i], a[j]) = (a[j], a[i])

def lomutoThreeWayPartition (a):
    n = len (a)
    pivot = a[n -1]
    i = -1 # todo : modify
    j =0 # todo : modify
    for j in range (0 ,n -1) :
        if (a [j] < pivot ):
            swap(a,i+1,j)
            i += 1

    swap(a,i+1,n-1)

    return (a, "Pivot x=", pivot)

def test(a):
    print()
    print("Orig array\n", a, "n")
    print("Partitioned array\n",lomutoThreeWayPartition(a), "\n")




arrayLength = int(input("Enter the length of the array you want to create."))
array = [0]*arrayLength
y = 0
while y < arrayLength:
    array[y] = randint(1,100)
    y+=1
array[arrayLength-1] = 94
test(array)
