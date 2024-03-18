from ast import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx =0
        while(idx<len(intervals)) :
            if(newInterval[0]<=intervals[idx][1]) :
                break
            idx+=1
        jdx=idx
        while(jdx<len(intervals)) :
            if(newInterval[1]<=intervals[jdx][1]) :
                if(newInterval[1]<intervals[jdx][0]) :
                    jdx-=1
                break
            jdx+=1
        list = []
        print(idx,jdx)
        for i in range(0,idx) :
            list.append(intervals[i])
        
        
        
        if(jdx<len(intervals) and jdx>=0) :
            list.append([min(newInterval[0],intervals[idx][0]),max(newInterval[1],intervals[jdx][1])])
        elif(idx<len(intervals)) :
            list.append([min(newInterval[0],intervals[idx][0]),newInterval[1]])
        else :
            list.append(newInterval)
        for i in range(jdx+1,len(intervals)) :
            list.append(intervals[i])
        # print(idx,jdx)
        return list