# Name: Your Name Here
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.


# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.





# swag
class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        # TODO: write an insert function for the BST.
        # NOTE: If key_to_insert equals my_key,
        #       then the node need should NOT be inserted in the tree.

        # base case
        if (self.key == None):
            self.key = key_to_insert
        # if node is already present
        elif key_to_insert == self.key:
            return
        # if key is larger than currentnode
        elif key_to_insert > self.key:
            self.right = Node(key_to_insert)
            return(self.right.insert(key_to_insert)) #recurse
        elif key_to_insert < self.key:
            self.left = Node(key_to_insert)
            return(self.left.insert(key_to_insert))



    # def inorder_traversal(self, ret_list):

    def inorder_traversal(self, ret_list):
        # TODO: write an inorder traversal function for the BST.
        # REMOVE the assert below
        assert False, 'Function inorder_traversal not implemented yet'

    def get_depth(self):

        if (self.left == None) and (self.right == None):
            return 1
        else:
            left = self.left
            self.key = self.right
            depthRight = self.get_depth(self)
            self.key = left
            depthLeft = self.get_depth(self)
            depth = 1+max()
            depth = 1+max(self.get_depth(self.left), self.get_depth(self.right))
            print(self.get_depth(self.left), "left depth", self.get_depth(self.right), "right depth")
            return depth
    def key_exists(self, key_to_find):

    # base case
    if (self.key == None):
        self.key = key_to_insert
    # if node is already present
    elif key_to_insert == self.key:
        return
    # if key is larger than currentnode
    elif key_to_insert > self.key:
        self.right = Node(key_to_insert)
        return(self.right.insert(key_to_insert)) #recurse
    elif key_to_insert < self.key:
        self.left = Node(key_to_insert)
        return(self.left.insert(key_to_insert))



if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
