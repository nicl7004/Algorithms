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

a = [1,2,50,12,19,15,20,51]
print(recursiveFindMax(a, 0, 7))
