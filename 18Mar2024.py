from ast import List


class Solution:
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def custom_key(item):
            if item[0] == item[0]:
                return item[1]
            else:
                return item[0]
        points = sorted(points, key=custom_key)
        # print(arr)
        i=0
        ans=0
        cr = []
        while(i<len(points)) :
            if(len(cr)==0) :
                ans+=1
                cr.append(points[i][0])
                cr.append(points[i][1])
            else :
                # print(cr[1],points[i][1])
                if(cr[1]<=points[i][1] and cr[1]>=points[i][0]) :
                    cr[0] = max(cr[0],points[i][0])
                    cr[1] = min(cr[1],points[i][1])
                else :
                    cr[0]=points[i][0]
                    cr[1]=points[i][1]
                    ans+=1
            i+=1
        return ans