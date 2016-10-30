#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields

    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        lengthWord = 0
        for letter in w:

            if letter not in self.next:
                self.next[letter] = MyTrieNode(False); #call the init function to make a new node

            if lengthWord +1 == len(w):
                self.isWordEnd = True #update the end of the word after our for loop
                self.count +=1
            lengthWord +=1



        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        wordCount = 0
        for letter in w:
            if letter not in self.next:
                return (0)
            # if self.isWordEnd == True:
            #     wordCount +=1

        else:
            if self.isWordEnd == True:
                wordCount +=self.count
            else:
                return (wordCount)
        return(wordCount)



    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE

        return [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] #TODO: change this line, please




if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)
    print(t.next)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    # print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    # print('Completions for \"tes\" are : ')

    print(j3, "should return 2")
    print(lst4)
