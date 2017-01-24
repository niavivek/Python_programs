"""
(4) (Extra credit) Convert script (3) so that it uses functional programming (e.g., list comprehension, map, reduce, and/or lambda). Try to use as few if/while/for statements as possible (it is possible to do the problem with no if/while/for statements). Do not use recursion.
"""
#Ref: #Ref: https://rosettacode.org/wiki/Maximum_triangle_path_sum
def reversi_num():
	with open('maxtriangle2.txt','r') as tri_file:
		rows = [lines for lines in tri_file]		
		rows = reversed([map(int, row.split()) for row in rows])

		rows[-1][:] = [(t, [t]) for t in rows[-1]]
	
		while len(rows) > 1:
			bottom = rows.pop()
			rows[-1][:] = [ value + max(bottom[i:i+2])[0]  for i,value in enumerate(rows[-1])]
		return rows[0][0]

def main():
	reversi_num()

if __name__ == '__main__':
	main()