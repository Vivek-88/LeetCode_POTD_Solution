from ast import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = defaultdict(int)
        for a in arr :
            dict[a]+=1
        st = set()
        for key in dict.keys() :
            if dict[key] in st :
                return False
            st.add(dict[key])
        return True