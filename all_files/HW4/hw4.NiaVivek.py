import urllib.request as re
import urllib.error as er
import string

#global variable to store dictionary of words, links, list of titles and count of books
word_count = dict()
count_books = 0
titles = list()
books = dict()
#use these default values if file is not readable, file is not in valid format
default_books = {0:"http://people.ischool.berkeley.edu/~tygar/for.i206/pg1342.txt",1:"http://people.ischool.berkeley.edu/~tygar/for.i206/pg11.txt",2:"http://people.ischool.berkeley.edu/~tygar/for.i206/pg1952.txt"}
default_titles = ["Pride and Prejudice","Alice's Adventures in Wonderland","The Yellow Wallpaper"]

def read_catalog(catalogfile):
	"""Method to read the catalog file to create dictionary of URL and list of title"""
	#dictionary to store the url and key
	global books
	global default_books
	global default_titles
	global count_books
	#list to store the titles
	global titles
	#counter for dictionary key
	i = 0
	try:
	#open file
		with open(catalogfile,'r') as catalog:
			#read and strip lines
			for lines in catalog.readlines():
				lines_stripped = lines.strip()
				#split the lines by using the tag http
				values = lines_stripped.split(",http://")
				#if values is not empty and has length 2 and title and url is not empty
				if values != [''] and len(values) == 2 and values[0] != "" and values[1] != "":
					#add title to the list
					titles.append(values[0])
					#add url to the dictionary
					books[i] = "http://" + values[1]
					#increase counter
					i += 1
		#get count of book
		count_books = len(books)

		#if no books was read - terminate program
		if (count_books == 0):
			print("File is not readable. Using default values.")
			#use default values
			books = default_books
			titles = default_titles
			count_books = len(books)
	#if error in reading file - terminate
	except:
		print("Exception occured while reading file. Using default values")
		#use default values
		books = default_books
		titles = default_titles
		count_books = len(books)
	while True:
	#read all the books
		all_data = list()
		b_count = range(0,count_books)
		#for each book in the dictionary - read data
		for book_num in b_count:
		#print(titles)
			contents = read_book(books[book_num],book_num)
			# add contents to a list
			all_data.append(contents)
		#if all the URL are not readable
		empty_data = list()
		for x in range(0,count_books):
			empty_data.append([])

		if all_data == empty_data:
			#use default values
			print("No contents were read. Using default values.")
			books = default_books
			titles = default_titles
			count_books = len(books)
			continue
		#create a dictionary of words in the data
		for values in range(0,count_books):
			update_words(all_data[values],values)
		#ask user for search term
		prompt_user()
		break

def open_url(url):
	"""Methdd to open the URL"""
	global books
	global count_books
	global titles
	#global word_count
	try:
		#open url
		response = re.urlopen(url)
		#get data
		content = response.read().decode('utf8')
		#close connection
		response.close()
		
	except(er.URLError):
		#if url is not functional
		content = ""
		print("The URL is not functional : ",url)
		return None
		# #remove the url from the books dictionary
		# for key,val in books.items():
		# 	if val == url:
		# 		del books[key]
		# 		#pop the last
		# 		titles.pop()
		# 		break
		# #update count for number of books
		# count_books = len(books)
		# return
	return content

def read_book(url,book_num):
	"""Method to read the URL, clean data and call update_words"""
	#calls open_url function to open the url
	book_contents = open_url(url)
	if book_contents != None:
		#calls filter data function to clean the data
		clean_data = filter_data(book_contents)
		#create dictionary for all the words in this book with 0's filling for count in all the books
		create_dict(clean_data)
		return clean_data
	else:
		return []


def filter_data(text):
	"""Method to filter the data from non-alphabets"""
	list_of_words = text.split()
	#remove non-alphabetical characters and convert to lower case
	list_of_words = [''.join([char for char in word if char in string.ascii_letters]).lower() for word in list_of_words]
	#remove empty spaces
	list_of_words = [word for word in list_of_words if word.isalpha()]
	#print(list_of_words)
	return list_of_words

def create_dict(data):
	#first create a dictionary with 0's for all the books for all the words
	global word_count
	global count_books

	for vals in data:
		word_count[vals] = [0]*count_books

def update_words(data, book_num):
	"""Method to modify the words dictionary"""
	global word_count
	#find count of each word in the book and update the dictionary
	for words in data:
		word_count[words][book_num] = (word_count.get(words,0)[book_num] + 1)
	#print(word_count)

def prompt_user():
	global titles
	global books
	#continue till false
	while True:
		try:
			#get user input
			user_input = input("Search term? ")
			if user_input == "<terminate>":
				print("Program terminated.")
				break
			#display catalog
			elif user_input == "<catalog>":
				i = 0
				for key in books.keys():
					print("'{}' : [{}, '{}']".format(titles[i],key,books[key]))
					i += 1
				continue
			#display titles
			elif user_input == "<titles>":
				for x in range(0,len(titles)):
					print(titles[x])
				continue
			#else search for word
			else:
				search(user_input)
		except:
			print("Invalid input. Try again.")

def search(words):
	"""Function to print count of words and handles commands"""
	global books
	global word_count
	global titles

	try:
		#index for titles and dictionary of books
		i = 0
		#condition for word not found
		if word_count.get(words) == None:
			print("The word {} does not appear in any books in the library.".format(words))
			return

		for vals in word_count[words]:
			# #if book index was empty - case where url was not active - index was removed - increase index
			# while(books.get(j) == None):
			# 	j += 1
			#print the count
			if(vals == 1):
				print("The word {} appears {} time in {} (link: {})".format(words,vals,titles[i],books[i]))
			elif(vals == 0):
				continue
			else:
				print("The word {} appears {} times in {} (link: {})".format(words,vals,titles[i],books[i]))
			#increase index values
			i += 1
	except:
		print("Error while searching for word.")


def main():
	#catalogfile = "simplecatalog.txt"
	catalogfile = "simplecatalog.txt"
	read_catalog(catalogfile)


if __name__ == '__main__':
	main()