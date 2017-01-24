"""

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

"""
def read_file(filename):
	"""Function to read the file"""
	#Ref: https://programmingpraxis.com/2014/07/22/maximum-sum-path/
	#get all the values in the triangle as rows
	rows = []
	try:
		with open(filename,'r') as tri_file:
			for lines in tri_file:
				rows.append([int(i) for i in lines.strip('\n').split(' ')])
			return rows
	except:
		print("Error reading file. Try again.")
		exit(0)

def triangle_sum(rows):
	#calls function to sum the rows and prints the result
	max_sum,path = sum_rows(rows)
	path = [str(i).strip() for i in path]
	string_path = ' + '.join(path)
	print("{} = {}".format(string_path,max_sum))

def sum_rows(row):
	#create a list containing the value and list of tuples containing the value and the path as a list
	row[-1][:] = [(v, [v]) for v in row[-1]]
	#continue till triangle is empty
	while len(row) > 1:
		#pop the last row
		last_row = row.pop()
		#enumerate the last-1 row (which is currently the last row)
		for i, v in enumerate(row[-1]):
			#get the maximum of the 2 values starting from index i from the popped row
			m = max(last_row[i:i+2])
			# m contains the value and the path as a list
			# replace last row with current value + max value of row below it at indices to left and right of it
			#and add to the path, the path of the max value
			row[-1][i] = (v + m[0], [v] + m[1])
	#once the top row is reached, the triangle is fully collapsed and contains only 1 element and its path
	# list of list of tuples, so index to get the value	
	return row[0][0]

def main():
	#continue prompting for file name, till a valid file with entries is entered
	while(True):
		print("Enter the file name to read:")
		#exception for any interruption
		try:
			#get input file name from user
			filename = input('> ')
		except:
			print("Program interrupted.")
			return
		#exception when reading file
		try:
			rows = read_file(filename)
			
		except IOError:
			print("Unable to find the file {}".format(filename))
		#if no exception - check if file is empty
		else:
			#if file is empty of has no words - prompt for another filename
			if(rows == None or len(rows) == 0):
				print("File is empty. Enter the name of another file to read.")
				continue
			#try finding the sum
			try:
				triangle_sum(rows)
				return
			#exception
			except:
				print("Error. Try again.")
				continue
	

if __name__ == '__main__':
	main()