#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #3
# September 21, 2014
# MapReduce - user similarity
#---------------------------------------------------------
# Author Info: 
# The code is originally created by Jim Blomo for his course:
# Data Mining and Analytics in Intelligent Business Services.
# The code is simplified and modified by Derek Kuo, TA for I206 Fall 14 Class.
#----------------------------------------------------------


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
        # TODO_1: compile businesses as a list under given user_id,after remove duplicate business, yield <user_id, [business_ids]>
        ##/
        
        business_ids = list(set(business_ids))
        yield [user_id, business_ids]
    
    def mapper2_collect_businesses_under_user(self, user_id, business_ids):
        yield ['LIST',[user_id, business_ids]]
        ###
        # TODO_2: collect all <user_id, business_ids> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [business_ids]]>
        ##/
    
    def reducer2_calculate_similarity(self,stat,user_business_ids):
        def Jaccard_similarity(business_list1, business_list2):
            ###
            # TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
            ##/
            business_list1 = set(business_list1)
            business_list2 = set(business_list2)
            intersection_bus = business_list1.intersection(business_list2)
            union_bus = business_list1.union(business_list2)
            return len(intersection_bus)*1.0/len(union_bus)

        ###
        # TODO_4: Calulate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
        ##/
        user_business_ids = list(user_business_ids)
        for i in range (0, len(user_business_ids)-1):
            for j in range(i+1, len(user_business_ids)):
                user1 = user_business_ids[i][0]
                user2 = user_business_ids[j][0]
                business_list1 = user_business_ids[i][1]
                business_list2 = user_business_ids[j][1]

                similarity = Jaccard_similarity(business_list1, business_list2)
                if similarity >= 0.5:
                    yield [[user1,user2], similarity]


    def steps(self):
        return [self.mr(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
                self.mr(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)]


if __name__ == '__main__':
    UserSimilarity.run()