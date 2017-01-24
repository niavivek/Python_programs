###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/
"""
Output from the program - I have removed most of the punctuations and lowered the words to compare them.

["0KAHnPpVNCuRHvzUOFNOug", "TEGj5wEP6-GuWHfTJ2JogA"]	0.5
["0g8H0jBLrYuooQoE-OaJsQ", "8BLqnArclv8XQQqf9g5j0Q"]	0.5
["8J9OIwQa65O0IOQ3JCZOOw", "a3qD7KcSmCwFMNRhf4F72Q"]	1.0
["BezVqATpPz0-m2lhDiuoIg", "hNoxBirlv11CbXwRW2KxMw"]	0.5
["BezVqATpPz0-m2lhDiuoIg", "zFBaDziL_Axyhm5vTi6udw"]	0.5
["BezVqATpPz0-m2lhDiuoIg", "zUdy0v_GDYixyfQeQrjkZw"]	0.5
["CcliogrhUxUat49d8r22AQ", "zFBaDziL_Axyhm5vTi6udw"]	0.5
["CcliogrhUxUat49d8r22AQ", "zUdy0v_GDYixyfQeQrjkZw"]	0.5
["Jzla1XE7_BIgoEZgplPOpQ", "faOa5SUlRkkOo7xlKMoQVA"]	0.5
["QY09z2M_tno4Xa1rnPa9iQ", "TEGj5wEP6-GuWHfTJ2JogA"]	0.5
["TlwVBhhxgMOyV_eCKIsJ9w", "faOa5SUlRkkOo7xlKMoQVA"]	0.8
["TlwVBhhxgMOyV_eCKIsJ9w", "ngR8yV-bxC3li0pWsfFdMQ"]	0.5714285714285714
["WLhheThsskOoid5ayneuwg", "faOa5SUlRkkOo7xlKMoQVA"]	0.5
["Z5XmyfQZwTokErNr2YGltQ", "eIUtPdoj7CbqzBWEiHH38g"]	1.0
["faOa5SUlRkkOo7xlKMoQVA", "joLTvLmaIYW1z1MIAen2Gw"]	0.5
["faOa5SUlRkkOo7xlKMoQVA", "ngR8yV-bxC3li0pWsfFdMQ"]	0.6666666666666666
["faOa5SUlRkkOo7xlKMoQVA", "zFBaDziL_Axyhm5vTi6udw"]	0.5
["faOa5SUlRkkOo7xlKMoQVA", "zUdy0v_GDYixyfQeQrjkZw"]	0.5
["vG1WYPrttwyrhHlAmNnuzw", "yvGQ23bnYrb71d-LKubP_Q"]	0.6
["zFBaDziL_Axyhm5vTi6udw", "zUdy0v_GDYixyfQeQrjkZw"]	1.0
"""


from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class UserSimilarity(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	def mapper1_extract_user_review(self,_,record):
		"""Taken a record, yield <user_id, review>"""
		#remove punctuations from text
		all_words = [word.lower() for word in WORD_RE.findall(record['text'])]
		yield [record['user_id'], all_words]

	def reducer1_compile_review_under_user(self,user_id,word):
		###
		# TODO_1: compile reviews as a list of array under given user_id,after remove duplicate review, yield <user_id, [review]>
		##/
		all_reviews = []
		#for each user id, create a list of all reviews
		for items in word:
			all_reviews.append(items)
		#create a list from list of lists
		all_reviews = [item for sublist in all_reviews for item in sublist]
		yield [user_id, all_reviews]


	def mapper2_collect_review_under_user(self, user_id, words):
		###
		# TODO_2: collect all <user_id, review> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [review]]>
		##/
		all_words = list(set(words))
		#print(all_words)
		yield ['LIST', [user_id, all_words]]

	def reducer2_calculate_similarity(self,stat,user_id_word):
		def Jaccard_similarity(word_list1, word_list2):
			###
			# TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
			##/
			word_set1 = set(word_list1)
			word_set2 = set(word_list2)
			word_union = word_set1.union(word_set2)
			word_intersection = word_set1.intersection(word_set2)
			jaccard_sim = len(word_intersection)*1.0/len(word_union)
			return jaccard_sim

		###
		# TODO_4: Calulate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
		##/
		user_id_word = list(user_id_word)
		for i in list(range(0,len(user_id_word)-1)):
			for j in list(range(i+1,len(user_id_word))):
				similarity = Jaccard_similarity(user_id_word[i][1],user_id_word[j][1])
				if (similarity >= 0.5):
					yield [[user_id_word[i][0], user_id_word[j][0]], similarity]
		


	def steps(self):
		return [
			MRStep(mapper=self.mapper1_extract_user_review, reducer=self.reducer1_compile_review_under_user),
			MRStep(mapper=self.mapper2_collect_review_under_user, reducer= self.reducer2_calculate_similarity)
		]


if __name__ == '__main__':
	UserSimilarity.run()
