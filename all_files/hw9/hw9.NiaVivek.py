"""
(1) A reversi number is a number that reads the same forwards and backwards, such as 303. The largest reversi number that is a product of two 2-digit numbers is 9009 = 91 x 99.

Write a Python program to find the largest reversi number that is a product of two 3-digit numbers.

Your output format should be "abc x def = ghiihg" (where the letters are replaced by digits).

(2) Convert script (1) so that it uses functional programming (e.g., list comprehension, map, reduce, and/or lambda), and has no if/while/for statements or recursion.

(3) Consider a triangle of numbers. By starting at the top of the triangle and moving to adjacent numbers below, we want to find the maximum total from top to bottom.

   2

  6 3

 1 3 5

7 4 8 2
In the triangle above, the maximum value is found by the sequence 2 + 6 + 3 + 8 = 19

Consider the triangle with a hundred rows in the file http://people.ischool.berkeley.edu/~tygar/for.i206/maxtriangle.txt

Find the path from top to bottom with maximum value. (Note that you will need to think of a good algorithm here -- if you try searching all possible paths, it will take in excess of 5 billion years.)

Your output format should list the chain, starting from the top and going to the bottom, as a sum. For the small example above, the output would be

"2 + 6 + 3 + 8 = 19"

(4) (Extra credit) Convert script (3) so that it uses functional programming (e.g., list comprehension, map, reduce, and/or lambda). Try to use as few if/while/for statements as possible (it is possible to do the problem with no if/while/for statements). Do not use recursion.
"""
