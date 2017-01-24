
"""Program which reads a text file for rainfall data and computes 
the average and print the average rainfall"""
def read_file(filename):
	"""Function reads the file passed as a parameter and returns the lines"""
	#initialize list to store the values read from file
	all_values = []
	with open(filename, "r") as read_file:
		for lines in read_file:
			#split the lines and add it to list
			all_values += lines.splitlines()
	return all_values

def filter_values(all_values):
	"""Function takes the list of all values read from the file as a parameter and 
	determines the valid input and makes a list of valid values and returns it."""
	#initialize the list to contain only the valid numbers
	valid_numbers = []
	for values in all_values:
		#break the loop if -999 is hit
		if values == "-999":
			break
		else:
			#try casting the value to a float
			try:
				#splits the line containing multiple values based on space
				#and assigns the first value to a variable
				first_value = values.split(" ")[0]
				#cast it to a float - exception thrown if cannot be cast as a float
				valid_value = float(first_value)
				#add the value to the list if the value is +ve and a float
				if valid_value >= 0:
					valid_numbers.append(valid_value)
				#skip and continue if value is negative
				else:
					continue
			#continue if any exception occurs
			except:
				continue
	return valid_numbers

def print_avg(valid_numbers):
	"""Function takes a list of numbers as input and calculates the average and print
	the appropriate message or average rainfall"""
	#check the length of the list, if it is 0 - print custom message
	if len(valid_numbers) == 0:
		print("There are no valid rainfall inputs")
	else:
		#compute average
		avg_rainfall = sum(valid_numbers)/len(valid_numbers)
		#if value is an integer cast it to integer, else print it as float
		if (avg_rainfall.is_integer()):
			avg_rainfall = int(avg_rainfall)
		print("Average rainfall = {} inches".format(avg_rainfall))

def main():
	rain_values = read_file("rainfall.txt")
	print_avg(filter_values(rain_values))


if __name__ == '__main__':
	main()