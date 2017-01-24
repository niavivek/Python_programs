"""
(2) Convert script (1) so that it uses functional programming (e.g., list comprehension, map, reduce, and/or lambda), and has no if/while/for statements or recursion.
"""

"""
Ref: http://stackoverflow.com/questions/2655956/filtering-elements-from-list-of-lists-in-python
http://www.krishnabharadwaj.info/python-and-projecteuler/
"""
def reversi_num():
	#create a list of lists containing the product and i, j values
	multiples = [[i*j,i,j] for i in range(100,1000) for j in range(100,1000)]
	#filter out the reversi numbers using filter and get the maximum value
	values = max(filter( lambda x : str(x[0]) == str(x[0])[::-1], multiples))
	print('{} x {} = {}'.format(values[1],values[2],values[0]))


def main():
	reversi_num()

if __name__ == '__main__':
	main()