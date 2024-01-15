from ast import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for m in matches :
            d1[m[0]]+=1
            d2[m[1]]+=1
        
        # print(d1)
        # print(d2)
        
        ans = [[],[]]
        
        for key in d1.keys() :
            if(d2[key]==0) :
                ans[0].append(key)
        
        for key in d2.keys() :
            if(d2[key]==1) :
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans