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
    for i in A:
        for j in B:
            if A[i] == B[j]:
                return true
    return false

