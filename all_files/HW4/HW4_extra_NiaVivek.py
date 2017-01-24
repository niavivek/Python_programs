"""
For extra credit, write an additional program to automatically generate the top 10 books catalog.txt from this web page (top 100 EBooks yesterday):  <a href="http://www.gutenberg.org/browse/scores/top" target="_blank">http://www.gutenberg.org/browse/scores/top</a>
"""
"""
http://docs.python-guide.org/en/latest/scenarios/scrape/
"""
from lxml import html
import requests

page = requests.get('http://www.gutenberg.org/browse/scores/top')
tree = html.fromstring(page.content)

#This will create a list of buyers:
top_list = tree.xpath('//*[text()="Top 100 EBooks yesterday"]/..//ol')[2].text_content()
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
#type(top_list)


all_list = top_list.split("\n")

with open('catalogtest.txt','w') as test_file:
	test_file.write(top_list)
	# for i in range(1,10):
	# 	test_file.write(all_list[i])
	# 	print('Book : ', i, all_list[i])
#print('Prices: ', prices)