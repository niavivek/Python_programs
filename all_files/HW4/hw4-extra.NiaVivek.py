# Import required modules
import requests
from bs4 import BeautifulSoup
import re

#global variables
url = 'http://www.gutenberg.org/browse/scores/top'
url_syntax = "http://www.gutenberg.org/cache/epub/"
url_tag = "/pg"

def parse_data():
# Create a variable with the url
	global url

	# Use requests to get the contents
	r = requests.get(url)

	# Get the text of the contents
	html_content = r.text

	# Convert the html content into a beautiful soup object
	soup = BeautifulSoup(html_content, 'lxml')

	#find the pattern "li" which is where the list of interest begins and get the 10 items
	top_10 = str(soup.find_all('li')[0:10])
	#strip the values of interest
	strip_data(top_10)

def strip_data(top_10):
	#remove everything except url and name
	#here url has to be build based on the number using url_syntax and url_tag - since there is a pattern
	pattern1 = r"(<li><a href=\"\/ebooks\/)"
	pattern2 = r"(<\/a><\/li>,)"
	pattern3 = r"(\">)"
	pattern4 = r"(<\/a><\/li>)"
	pattern5 = r"(\[\t)"
	pattern6 = r"(])"
	#update values in top_10 by creating substrings
	top_10 = re.sub(pattern1,'\t',top_10)
	top_10 = re.sub(pattern2,'',top_10)
	top_10 = re.sub(pattern3,'\t',top_10)
	top_10 = re.sub(pattern4,'',top_10)
	top_10 = re.sub(pattern5,'',top_10)
	top_10 = re.sub(pattern6,'',top_10)
	#print(top_10)
	#convert values to a sring and split of tab
	top_10 = str(top_10)
	top_10 = top_10.split("\t")
	#write data to a file
	write_file('catalogtest.txt',top_10)

def write_file(filename,data):
	global url_tag,url_syntax
	with open(filename,'w') as test_file:
		#write data one by one - using the syntax
		for i in range(1,len(data),2):
			test_file.write(data[i]+",")	
			test_file.write(url_syntax + data[i-1] + url_tag + data[i-1]+".txt\n")
			
def main():
	parse_data()

if __name__ == '__main__':
				main()			
