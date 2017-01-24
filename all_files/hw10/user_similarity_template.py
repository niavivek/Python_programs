###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/


from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep


class UserSimilarity(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	def mapper1_extract_user_business(self,_,record):
		"""Taken a record, yield <user_id, business_id>"""
		yield [record['user_id'], record['business_id']]

	def reducer1_compile_businesses_under_user(self,user_id,business_ids):
		###
		# TODO_1: compile businesses as a list of array under given user_id,after remove duplicate business, yield <user_id, [business_ids]>
		##/
		unique_buss_ids = list(set(business_ids))
		yield [user_id, unique_buss_ids]


	def mapper2_collect_businesses_under_user(self, user_id, business_ids):
		###
		# TODO_2: collect all <user_id, business_ids> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [business_ids]]>
		##/
		yield ['LIST', [user_id, business_ids]]

	def reducer2_calculate_similarity(self,stat,user_business_ids):
		def Jaccard_similarity(business_list1, business_list2):
			###
			# TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
			##/
			business_set1 = set(business_list1)
			business_set2 = set(business_list2)
			jaccard_sim = len(business_set1.intersection(business_set2))*1.0/len(business_set1.union(business_set2))
			return jaccard_sim

		###
		# TODO_4: Calulate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
		##/
		user_business_ids = list(user_business_ids)
		for i in list(range(0,len(user_business_ids)-1)):
			for j in list(range(i+1,len(user_business_ids))):
				similarity = Jaccard_similarity(user_business_ids[i][1],user_business_ids[j][1])
				if (similarity >= 0.5):
					yield [[user_business_ids[i][0], user_business_ids[j][0]], similarity]
		


	def steps(self):
		return [
			MRStep(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
			MRStep(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)
		]


if __name__ == '__main__':
	UserSimilarity.run()
