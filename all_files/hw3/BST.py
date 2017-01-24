#---------------------------------------------------------
# Nia Vivekanandan
# niavivek@berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# ---------------------------------------------------------

class Node:
	#Constructor Node() creates node
	def __init__(self,word):
		self.word = word
		self.right = None
		self.left = None
		self.count = 1

class BSTree:
	#Constructor BSTree() creates empty tree
	def __init__(self, root=None):
		self.root = root
	
	#These are "external functions" that will be called by your main program - I have given these to you
	
	#Find word in tree
	def find(self, word):
		return _find(self.root, word)
	
	#Add node to tree with word
	def add(self, word):
		if not self.root:
			self.root = Node(word)
			return
		_add(self.root, word)
		#print("Word-here",word,"Size",self.size,"Depth",self.depth)

	#Print in order entire tree
	def in_order_print(self):
		_in_order_print(self.root)

	#print indented tree
	def print_indented(self):
		_print_indented(self.root)

	#get size of tree
	def size(self):
		return _size(self.root)

	#get height of tree
	def height(self):
		return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!
#Function to add node with word as word attribute
def _add(root, word):
	#if word is already present, increment count
	if root.word == word:
		root.count +=1
		return
	# if word is less than root, go left, if left child is empty, add it to left, else go left and check for precedence
	if root.word > word:
		if root.left == None:
			root.left = Node(word)
		else:
			_add(root.left, word)
	# if word is greater than root, go right, if right child is empty, add it to right, else go right and check for precedence
	else:
		if root.right == None:
			root.right = Node(word)
		else:
			_add(root.right, word)

#Function to find word in tree
def _find(root, word):
	#YOU FILL THIS IN
	# if root is none or word is not present, return word and count as 0
	if root == None:
		return word,0
	# if the root is equal to the word, return word and count
	if root.word == word:
		return root.word,root.count
	# if word is less than root, go left
	if root.word > word:
		return _find(root.left,word)
	# if word is greater than root, go right
	else:
		return _find(root.right,word)

#Get number of nodes in tree
def _size(root):
	#YOU FILL THIS IN
	#variables to store left and right tree size
	lsize = 0
	rsize = 0
	#if left child is present, get its size
	if(root.left != None):
	 	lsize = _size(root.left)
	 #if right child is present get its size
	if(root.right != None):
	 	rsize = _size(root.right)
	 # add left and right child size to 1 (size of root)
	return 1 + lsize + rsize

#Get height of tree
def _height(root):
	#YOU FILL THIS IN
	#height is 0 for tree without root
	height = 0
	if(root != None):
		# use recursive calls to find the height of left and right trees, take the max of the two and add it to 1 (height of root) 
		return 1 + max(_height(root.left),_height(root.right)) 
	return height
	
#Function to print tree in order
def _in_order_print(root):
	if not root:
		return
	_in_order_print(root.left)
	print(root.word)
	print(root.count)
	_in_order_print(root.right)
#function to print tree as an indented tree- helps in visualizing the tree as on a paper
def _print_indented(root,level = 1,indent = " "):
	#if no root is present - tree is empty
	if not root:
		return
	# add indentation is the level is not 1
	if level != 1:
		indent += "    "
	#first print the right children, then the root and then the left children through recursive calls
	_print_indented(root.right, level + 1, indent)
	#first indent, print level and then the word
	print(indent, level, ".",root.word)
	_print_indented(root.left, level + 1, indent)
