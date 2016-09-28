# question 1
import unittest

def findMax(array):
    if (len(array) <= 2):
        return max(array)
    else:
        split = len(array)//2
        l = ((findMax(array[:(split)])))
        r = ((findMax(array[(split):])))
        maxim = max(l,r)
        return (maxim)

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(findMax(ar1),10))
        self.assertEqual(findMax(ar2), 6)
        self.assertEqual(findMax(ar2, 6))
        self.assertEqual(findMax(ar2, 6))
        self.assertEqual(findMax(ar2, 6))
ar1 = [9,6,8,5,7,4,1,3,2,10]
ar2 = [2,2,2,2,2,2,2,6]
ar3 = [1,2,3,4,5,6,7,8,9,10]
ar4 = [10,9,8,7,6,5,4,3,2,1]
ar5 = [1,20,2,19,3,18,4,17,5,18]
findMax(ar1)

if __name__ == '__main__':
    unittest.main()
# test(self.assert_(boolean expression, 'message'))
