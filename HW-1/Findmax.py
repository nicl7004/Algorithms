def findMax(a,left,right):
    if(a[left] > a[right]):
        return a[left]
    else:

        return findMax(a,left+1,right-1)

a = [1,2,5,17,19,15,12,10,9,8,1]
print(findMax(a,0,10))
