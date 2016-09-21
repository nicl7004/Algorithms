from random import randint

def swap (a,i,j):
    (a[i], a[j]) = (a[j], a[i])

def lomutoThreeWayPartition (a):
    n = len (a)
    pivot = a[n -1]
    # print(pivot)
    i = -1 # todo : modify
    j =0 # todo : modify
    k = -1
    for j in range (0 ,n -1) :
        if (a [j] < pivot ):
            swap(a,i+1,j)
            if(k != i):
                swap(a,k+1,j)
            i += 1
            k += 1
        elif(a[j] == pivot):
            swap(a,k+1,j)
            k+=1
    # print("Pivot", n-1, "i+1", i+1)
    if(i != k):
        swap(a,k+1,n-1)
    elif(a[n-1]< a[0]):
        swap(a, n-1, 0)

    return (a, "Pivot x=", pivot, "i =", i, "j =", j, "n-1 =", n-1)

def test(a):
    print("------------------------------------------------------------------------")
    print("Orig array\n", a, "\n\n")
    print("Partitioned array\n",lomutoThreeWayPartition(a), "\n\n")


# arrayLength = int(input("Enter the length of the array you want to create."))
# array = [0]*arrayLength
# y = 0
# while y < arrayLength:
#     array[y] = randint(1,100)
#     y+=1
array = [20, 12, 17, 18, 9, 5, 4, 12, 8, 12]
newarray = [1,6,3,5,4,9,5]
decending = [25,24,23,22,20,16,14,10,10,10,12,8,2,3,4,10]
anotherOne = [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,7,8,4,5,6,5]
bad = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
doubBad = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
fives = [1,5,5,5,5,5,5,5,5,5,5,5]
badFives = [5,5,5,5,5,5,5,5,5,1]
test(newarray)
test(array)
test(decending)
test(anotherOne)
test(bad)
test (doubBad)
test(fives)
test(badFives)
