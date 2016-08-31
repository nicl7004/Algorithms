def recursiveFindMax(a, left, right):
    mid = int((right+left)/2)

    if (right-left)>=2:
        leftMax = recursiveFindMax(a, left, mid)
        rightMax = recursiveFindMax(a, mid, right)
        if(leftMax>rightMax):
            return leftMax
        else:
            return rightMax
    else:

        if a[right]>a[left]:

            return a[right]

        else:

            return a[left]

# def max22(L,left,right):
#
#     if left == right:
#         # handle size 1
#         return L[left]
#
#     if left + 1 == right:
#         # handle size 2
#         return max(L[left], L[right])
#
#     # split the lists (could be uneven lists!)
#     split_index = (left + right) / 2
#     # solve two easier problems
#     return max (max22(L, left, split_index), max22(L, split_index, right))

    # if leftMax>rightMax:
    #     return leftMax
    # else:
    #     return rightMax


        # if(recursiveFindMax(a,left,mid)> a[left] and recursiveFindMax[a,left,mid]> a[right]):
        #      return recursiveFindMax(a,left,mid)
        # elif(recursiveFindMax(a,mid,right)> a[left] and recursiveFindMax[a,mid,right]> a[right]):
        #     return recursiveFindMax(a,mid,right)
    # elif(left-right)
    # elif(a[left]> a[right]):
    #     return a[left]
    # elif(a[right]> a[left]):
    #     return a[right]



a = [1,2,50,12,19,15,20,10]
print(recursiveFindMax(a, 0, 7))

# print (max22(a,0,7))
