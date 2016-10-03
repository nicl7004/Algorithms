# Name: Your Name Here
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.
# swag
class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None



    def insert(self, key_to_insert):
        # TODO: write an insert function for the BST.
        # NOTE: If key_to_insert equals my_key,
        # base case
        if key_to_insert == self.key:
            return
        elif key_to_insert > self.key:
            if self.right == None:
                self.right = Node(key_to_insert)
            else:
                return(self.right.insert(key_to_insert)) #recurse
        elif key_to_insert < self.key:
            if self.left == None:
                self.left = Node(key_to_insert)
            else:
                return(self.left.insert(key_to_insert))
    # def inorder_traversal(self, ret_list):

    def inorder_traversal(self, ret_list):
        # TODO: write an inorder traversal function for the BST.
        # REMOVE the assert below
        assert False, 'Function inorder_traversal not implemented yet'

    def get_depth(self):
        if self.key == None:
            return 0
        else:
            lefty = self.left
            self.key = self.right
            rightDep = self.get_depth()
            self.key = lefty
            leftDep = self.get_depth()

            if (leftDep > rightDep):
                return leftDep +1
            else:
                return rightDep+1

            # right = self.right
            # self.key = self.left
            # left = self.get_depth()
            # self.key = right
            # right = self.get_depth()
            # right = self.right.get_depth()
            # return(max(left, right))

        # else:
        #     left = self.left
        #     self.key = self.rightl
        #     depthRight = self.get_depth(self)
        #     self.key = left
        #     depthLeft = self.get_depth(self)
        #     depth = 1+max()
        #     depth = 1+max(self.get_depth(self.left), self.get_depth(self.right))
        #     print(self.get_depth(self.left), "left depth", self.get_depth(self.right), "right depth")
        #     return depth



    def key_exists(self, key_to_find):

        if key_to_find == self.key:
            return True
        elif key_to_find > self.key:
            if self.right == None:
                return(False)
            else:
                return(self.right.key_exists(key_to_find)) #recurse
        elif key_to_find < self.key:
            if self.left == None:
                return (False)
            else:
                return(self.left.key_exists(key_to_find))

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
