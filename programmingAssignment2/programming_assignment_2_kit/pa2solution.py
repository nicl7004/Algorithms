from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random
sys.setrecursionlimit(50000)
# had to set the recusion depth to 50 times larger than normal
recur = sys.getrecursionlimit()

# NAME:Nicholas Clement
# STUDENT ID NUMBER: 103151912
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: __ Nicholas Clement__


# I no longer use my own implementation of quick sort, after changing the recursion depth to 50000(50 times larger than normal)
#i still recieved a seg fault, so I have used the standard python Sorted() function, it uses the timsort algorithm.
def partition(interval_lst, l, r):
    pivot = interval_lst[r][0]

    i, j = l-1, l
    for j in range (l,r):
        if interval_lst[j][0] <= pivot:
            interval_lst[i+1], interval_lst[j] = interval_lst[j], interval_lst[i+1]
            i +=1

    interval_lst[i+1], interval_lst[r] = interval_lst[r], interval_lst[i+1]
    return i +1


def quickSort(interval_lst, l, r):
    if l<r:
        part = partition(interval_lst, l, r)
        quickSort(interval_lst, l, part-1)
        quickSort(interval_lst, part+1, r)
    return interval_lst

def free_time_intervals(interval_lst, T):
    # First step is to sort the passed in list based on start times


    lengthList = len(interval_lst) -1
    sortedArr = quickSort(interval_lst, 0, lengthList)

    # print(sortedArr)
    x = []
    var = 0
    for each in sortedArr:

        if each[0] > T:
            continue

        if each[0] > var:
            if each[0] > T:
                x.append((var, T))
                continue
            else:
                x.append((var, each[0]))
        var = max(var, each[1])
    if var < T:
        x.append((var, T))
    # print("HERE",x)
    return x

def max_logged_in(interval_lst,T):
    # First design the algorithm on pen/paper and solve a few examples.
    sortedArr = sorted(interval_lst)
    # time = (1,2)
    # x, each, runningMax, minEnd = 0, 0, 0, 1000
    # var = sortedArr[0][1] #set to end time of first user to start things off
    # while each <= len(sortedArr)-1 :
    #     print("___________________________________")
    #     print("Each Currently =", each)
    #     print("Current values = ", sortedArr[each])
    #
    #     if (sortedArr[each][0]<=var):
    #         x +=1
    #         minEnd = min(sortedArr[each][1], minEnd)
    #     if (sortedArr[each][0] > minEnd):
    #         minEnd = sortedArr[each][1]
    #         x -=1
    #     if x > runningMax and y>x:
    #         time = (x,sortedArr[each][0])
    #         runningMax = x
    #
    #
    #     var = max(var, sortedArr[each][1])
    #     each +=1
    #     y = x
    #     print("x =", x)
    #     print("running Max =",runningMax)
    #     print("minimum ending point =", minEnd)
    #     print("var Currently =", var)
    #     print("recusion limit=",recur)
    #
    # print("---------------\n\n")
    #
    #
    # return(time)

    newList = []
    y =x=time= 0
    for each in sortedArr:
        if each[0] <=T:
            newList.append((each[0], 1))
        if each[1] <=T:
            newList.append((each[1], -1))

    newList = sorted(newList)
    # print(newList, "    herehehehehheheheh")
    for each in newList:
        x += each[1]
        if y < x:
            y = x
            time = each[0]

    return(y, time)





if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print("MAX LOGGED =", max_logged_in(lst2,30))

    lst3 = [(0, 23), (2, 6), (4, 17), (8, 13), (12, 19), (20, 21), (46, 57), (49, 53), (65, 71), (70, 79)]

    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))

    lst4 = [(0, 49), (2,49), (24,25)]
# expected was 3,26
    print('Input:', lst4)
    print(free_time_intervals(lst4,30))
    print(max_logged_in(lst4,30))
