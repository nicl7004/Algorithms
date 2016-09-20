def swap (a,i,j):
    (a[i], a[j]) = (a[j], a[i])

def lomutoThreeWayPartition (a):
    n = len (a )
    pivot = a[n -1]
    i = 0 # todo : modify
    j =0 # todo : modify
    for j in range (0 ,n -1) :
        if (a [j] < pivot ):
            swap(a,i,j)
            i += 1
 # todo : fill in the code for this part ..
        elif (a[j] == pivot ):
 # todo : fill in the code for this part ..
 # todo : move the pivot element back to the correct place .
 # ...
