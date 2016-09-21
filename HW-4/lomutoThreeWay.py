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
            i += 1
            k += 1
            swap(a,i,j)
        elif(a[j] == pivot):
            k+=1
            swap(a,k,j)
    # print("Pivot", n-1, "i+1", i+1)
    swap(a,i+1,n-1)

    return (a, "Pivot x=", pivot)
 # todo : fill in the code for this part ..
        # elif (a[j] == pivot ):
 # todo : fill in the code for this part ..
 # todo : move the pivot element back to the correct place .
 # ...

def test(a):
    print("Orig array\n", a, "\n\n")
    print("Partitioned array\n",lomutoThreeWayPartition(a), "\n\n")

# arrayLength = int(input("Enter the length of the array you want to create."))
# array = [0]*arrayLength
# y = 0
# while y < arrayLength:
#     array[y] = randint(1,100)
#     y+=1
array = [20, 12, 17, 18, 9, 5, 4, 12, 8, 12]
test(array)
