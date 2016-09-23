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
            self.key = self.right
            return(self.insert(key_to_insert)) #recurse
        elif key_to_insert < self.key:
            self.key = self.left
            return(self.insert(key_to_insert))



    # def inorder_traversal(self, ret_list):
    def get_depth(self):

        if (self.left == None) and (self.right == None):
            return 1
        else:

            depth = 1+max(self.get_depth(self.left), self.get_depth(self.right))
            return depth

    def key_exists(self, key_to_find):
        # return True if the key_to_find is already in the tree,
        #   otherwise return False
        # REMOVE the assert below
        assert False, ' Function find not implemented yet'

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
