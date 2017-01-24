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

	def print_indented(self):
		_print_indented(self.root)

	def size(self):
		return _size(self.root)

	def height(self):
		return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!
#Function to add node with word as word attribute
def _add(root, word):
	if root.word == word:
		root.count +=1
		return
	ldepth = 0
	rdepth = 0
	lsize = 0
	rsize = 0
	if root.word > word:
		if root.left == None:
			root.left = Node(word)
		else:
			_add(root.left, word)
	else:
		if root.right == None:
			root.right = Node(word)
		else:
			_add(root.right, word)

#Function to find word in tree
def _find(root, word):
	#YOU FILL THIS IN
	if root == None:
		return word,0
	if root.word == word:
		return root.word,root.count
	if root.word > word:
		return _find(root.left,word)
	else:
		return _find(root.right,word)

#Get number of nodes in tree
def _size(root):
	#YOU FILL THIS IN
	lsize = 0
	rsize = 0
	if(root.left != None):
	 	lsize = _size(root.left)
	if(root.right != None):
	 	rsize = _size(root.right)
	return 1 + lsize + rsize

#Get height of tree
def _height(root):
	#YOU FILL THIS IN
	height = 0
	if(root != None):
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

def _print_indented(root,level = 1,indent = " "):
	if not root:
		return
	if level != 1:
		indent += "    "
	_print_indented(root.right, level + 1, indent)
	print(indent, level, ".",root.word)
	_print_indented(root.left, level + 1, indent)

def rotate_with_left(root):
	leftchild = root.left
	if leftchild != null:
		root.left = leftchild.right
		leftchild.right = root