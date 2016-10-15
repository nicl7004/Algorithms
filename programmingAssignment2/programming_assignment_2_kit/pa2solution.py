from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME:Nicholas Clement
# STUDENT ID NUMBER: 103151912
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: __ Nicholas Clement__

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

      if each[0] > var:
        x.append((var, each[0]))
      var = max(var, each[1])

    if var < T:
        x.append((var, T))
    return x

def max_logged_in(interval_lst,T):
    # First design the algorithm on pen/paper and solve a few examples.

    sortedArr = quickSort(interval_lst, 0, len(interval_lst)-1)

    y = []
    x = 0
    var = sortedArr[0][1] #set to end time of first user to start things off

    for each in sortedArr:
        if each[0]<=var:
            x +=1
        else:
            # print("appending ", x)
            y.append(x)
            x = 1
        var = max(var, each[1])
    print (sortedArr)

    # z = max(y)
    print(y)    # return x


if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
