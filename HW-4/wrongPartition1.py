a = [1,12,15,2,6,9,10,13]

def swap(a,i,j):
    (a[i], a[j]) = (a[j], a[i])

def wrongPartition(a):
    # Implement Lomuto partition algorithm
    n = len(a)
    pivot=a[n-1] # choose pivot at the very end
    i=0      # start with i = 0 and j = 0
    j=0
    for j in range(0,n-1):
        # Invariant: a[0] to a[i] are <= pivot, whereas
        #            a[i+1] to a[j-1] are > pivot,
        #            everything else is to be processed
        if (a[j] <= pivot): #If a[j+1] is smaller than pivot
            swap(a,i,j)  # move the new to be processed
                             # element into the correct place
            i = i +1
    # end for loop
    swap(a,i+1,n-1)        # Final step: restore the pivot back to place

def test(a):
    print('Input',a, 'Pivot:',a[len(a) -1])
    wrongPartition(a)
    print('Output',a)
test(a)


# algorithm partition(A, lo, hi) is
#     pivot := A[lo]
#     i := lo – 1
#     j := hi + 1
#     loop forever
#         do
#             i := i + 1
#         while A[i] < pivot
#
#         do
#             j := j – 1
#         while A[j] > pivot
#
#         if i >= j then
#             return j
#
#         swap A[i] with A[j]
