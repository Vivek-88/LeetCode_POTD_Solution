from ast import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = {}
        for a in arr :
            mp[a]=mp.get(a,0)+1
        list = []
        for fre in mp.values() :
            list.append(fre)
        ans=0
        list.sort()
        for i in range(len(list)) :
            if(k>=list[i]) :
                k-=list[i]
            else :
                ans+=1
        return ans