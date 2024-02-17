from ast import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        a = [[0]*2 for _ in range(n)]
        for i in range(n-1) :
            a[i][0]=max(0,heights[i+1]-heights[i])
            a[i][1]=i+1
        a.sort(key=lambda x: x[0])
        # Arrays.sort(a,(b,c) ->b[0]-c[0]);
        lo,hi=0,n-1
        ans=0
        while(lo<=hi) :
            mid = lo+(hi-lo)//2
            b,l=bricks,ladders
            for i in range(n) :
                if(a[i][1]<=mid) :
                    if(b>=a[i][0]) :
                        b-=a[i][0]
                    else :
                        l-=1
            
            if(b>=0 and l>=0) :
                ans=max(ans,mid)
                lo=mid+1
            else :
                hi=mid-1
        return ans