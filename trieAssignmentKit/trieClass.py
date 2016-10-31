#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import itertools
from itertools import chain
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
        for letter in w:

            if letter not in self.next:
                self.next[letter] = MyTrieNode(False); #call the init function to make a new node

            self = self.next[letter] #step to the next letter


        self.isWordEnd = True #update the end of the word after our for loop
        self.count +=1



        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        for letter in w:
            if letter in self.next: #move to the next letter
                self = self.next[letter]

        if self.isWordEnd == True: #check if the current letter is the end of a word
            return self.count #return the frequency of this word

        return(0)

    def depthSearch(self, given):
        '''depth search first traversal to search after our prefix is exhausted. '''
        x = []

        for letter in self.next.keys():
            print("letter=", letter)
            if self.next[letter].isWordEnd == True:
                y = (given+letter, self.next[letter].count)
                x.append(y)

            x.append(self.next[letter].depthSearch(given+letter)) #iterate through each key and recurse to find the ends of that list

        return list(itertools.chain.from_iterable(x))
        # return x
    def autoComplete(self,w):
    
        x = []


        for letter in w:
            if letter not in self.next:
                return #we know that if all the prefix letters dont exist there is no larger word that will
            if self.isWordEnd:
                x.append((w, self.count)) #for the off chance that we are passed a word
            self = self.next[letter] #move to the next letter of the prefix



        x.append(self.depthSearch(w))

        print("autoComplete for word",w, "came out to be", x)

        #flatten the list
        final = list(chain(*x))

        return(final)




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
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')

    print(j3, "should return 2")
    print(lst4)
