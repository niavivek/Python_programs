#---------------------------------------------------------
# Nia Vivekanandan
# niavivek@berkeley.edu
# Homework #3
# September 20, 2016
# hw3test.py
# Test
#---------------------------------------------------------

from BST import *
from hw3 import *

#initialize a tree
T = BSTree()
# T.add("4")
# T.add("2")
# T.add("3")
# T.add("5")
# T.add("1")
# T.add("6")
# T.print_indented()

#add words or nodes to the tree
T.add("hello")
T.add("goodbye")
T.add("paul")
T.add("summer")
T.add("paul")
T.add("all")
T.add("goodbye")
T.add("indigo")

#find the words in the tree
print(T.find("hello"))
print(T.find("goodbye"))
print(T.find("paul"))
print(T.find("summer"))
print(T.find("all"))
print(T.find("indigo"))
#print height and size
print("Height of the tree is",T.height())
print("Size of the tree is",T.size())
#print indented tree
T.print_indented()