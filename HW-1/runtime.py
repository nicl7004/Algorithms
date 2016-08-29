import time

start = time.time()

listA = [1] * 10000
i = 0
listB = [1] * 10000

while i < 10000:
    listA[i] = i
    i+= 1
i = 0
while i < 10000:
    listB[i] = (10000)-i
    i+= 1
print(listA)
print(listB)

def checkIfElement(A,B):
    numberComparisons = 0
    for i in A:

        for x in B:
            #print("i = ", i, "x =", x)
            numberComparisons += 1
            if A[i] == B[x-1]:

                return 1, numberComparisons
    return 0, numberComparisons

print("list a vs list a", checkIfElement(listA, listA))
print("list b vs list b", checkIfElement(listA, listB))