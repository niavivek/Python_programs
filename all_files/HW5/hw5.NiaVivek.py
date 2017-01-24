
import sys
import urllib.request
import operator
from bs4 import BeautifulSoup

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code
def get_restaurant():
	#URL of the 4 pages
	url1 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0#'
	url2 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=10&sortby=rating'
	url3 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=20&sortby=rating'
	url4 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=30&sortby=rating'
	list_url = (url1,url2,url3,url4)
	dict_rest = dict()
	try:
		#for each URL - open the URL and process information
		for items in list_url:
			content = urllib.request.urlopen(items).read().decode('utf8')
			content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
			soup = BeautifulSoup(content,'lxml')
			#get tags corresponding to restaurant names and review counts
			faces = soup.find_all('span', {'class': 'indexed-biz-name'})
			ratings = soup.find_all('span', {'class':'review-count rating-qualifier'})
			num_items = len(ratings)
			list_rest = list()
			list_rating = list()
			#find the tag to get the text within it
			for val in faces:
				list_rest.append(val.find('span').string)
			for rating in ratings:
				list_rating.append(''.join(word for word in rating.string if word.isdigit()))
				#print(len(list_rating))
			for i in range(0,len(list_rating)):
				#print(i)
				dict_rest[list_rest[i]] = int(list_rating[i])
			#sort the restautants by reviews
			sorted_rest = sorted(dict_rest.items(), key=operator.itemgetter(1), reverse = True)
	except (urllib.request.URLError):
		print('Error opening URL')
		return
	except:
		print('Error finding the top 40 restaurants')
		return
	write_file(sorted_rest)

def write_file(sorted_list):
	"""Function to write the sorted list of restaurants"""
	try:
		with open('restaurants.NiaVivek.txt','w') as write_file:
			for k,v in sorted_list:
				write_file.write(k + ", " + str(v) +"\n")
	except:
		print('Error writing file')

# Your code goes here
def main():
   get_restaurant()

if __name__ == '__main__':
    main()

