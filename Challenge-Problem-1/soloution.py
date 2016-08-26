x = list(input("input your array please.").replace(" ", ""))
x = [6,2,5,1]
print(x)
#warm up to find smallest number in list
def findSmallest(x):
    y = 0
    smallest = x[y]
    while y < len(x):

        if smallest > x[y]:
            smallest = x[y]
        y+=1
    return smallest

# print(findSmallest(x))
# Actual problem
# make an complete array to test numbers against
testArray = list(range(1,len(x),1))
i = 0
y=0
for i in testArray:
    print(testArray[i])
    for y in x:
        if testArray[i] == x[y]:
            break
        else:
            print(testArray[i], 'This One')


