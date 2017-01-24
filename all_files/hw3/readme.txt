#---------------------------------------------------------
# Nia Vivekanandan
# niavivek@berkeley.edu
# Homework #3
# September 20, 2016
# README.txt
# README
#---------------------------------------------------------

(1)  For the file http://www.gutenberg.org/cache/epub/1342/pg1342.txt what is the depth of your tree?  What does that say about the number of operations to find a word?
For the file pg1342.txt,

Number of entries in the tree:  7016
Maximum depth of the tree:  29

Number of operations to find a word would be: O(log N) = 12.77 for this tree. But the maximum depth of the tree is 29, which is greater then 12, this is because the tree is unbalanced and could have instances where 1 parent would have only 1 child instead of the 2 children possible. This makes the number of operations to find a word greater then O(log N) and the worst case scenario could be O(N) for a tree with only 1 child at each node.

(2)  What would happen if the input to your program were sorted (as it was in HW 1)?

If the input was sorted, then all the words will be added to the right of the tree(for ascending sort). This would be a tree with children only to its right and the depth of the tree would be equal to the number of elements, in which case the number of operations to find a word would be O(N).

(3)  What are applications for binary search tree?  In what ways are they superior to lists?  In what ways are they inferior to lists?
Binary search tree is useful to solve arithmetic expressions, to store a path in a graph, file system in a computer (hierarchical system), router algorithms etc.,

They are superior to lists because the searching, insertion and deletion operations are much faster than lists. O(log N) for BST versus O(n) for a list.

They are inferior to lists, if the lists are implemented in the form of stack or queue, where the insertion, retrieval and deletion operations can be done in O(1) whereas in BST this might take O(log N). 

(4)  Did you implement the extra credit (listed below)?  If so please explain your testing strategy on the extra credit.
Extra credit was not implemented.


Test strategies used:

The program was tested using the following conditions

1. No file name entered —> prompts user again (this was there by default though)
2. File without any contents —> Prompts user for another file
	> text2.txt
File is empty. Enter the name of another file to read.
Enter the file name to read:

3. File which cannot be read —> Eg. png, pdf

	> popLandClass.png
Error reading file. Try again.
File is empty. Enter the name of another file to read.
Enter the file name to read:
>

4. When Ctrl-C is pressed. Program exits with the statement “Program interrupted”

5. Words which does not appear in the text, will give the following output

Query? hello
The word hello appears 0 times in the tree.

6. Multiple tabs as query

Query? 		
The word 		 appears 0 times in the tree.

7. Space as query

Query?  
The word   appears 0 times in the tree.

8. query with apostrophe

Query? what's
The word what's appears 0 times in the tree.

9. query with multiple words:

Query? my hello
The word my hello appears 0 times in the tree.

10. query with hyphen

Query? has- 
The word has- appears 0 times in the tree.

11. stats
Query? stats
Number of entries in the tree:  7016
Maximum depth of the tree:  29

12. Finally terminate

Query? terminate
exits the program

13. test.py file was used to test parts of the file, like find method, height and size of the tree for a tree which could be drawn easily by hand.

14. I also implemented a indented printing of the tree which gives the structure of the tree. The number before the word, gives the level of that word and it is indented to the right or left.

For the test case with 2 more words added to the tree, the indented tree is as follows:

          3 . summer
      2 . paul
          3 . indigo
  1 . hello
      2 . goodbye
          3 . all



also,

          3 . 6
      2 . 5
  1 . 4
          3 . 3
      2 . 2
          3 . 1