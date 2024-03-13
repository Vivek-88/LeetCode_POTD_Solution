class Solution:
    def pivotInteger(self, n: int) -> int:
        sum=0
        for i in range(1,n+1) :
            sum+=i
        s1=0
        for i in range(1,n+1) :
            s1+=i
            if(s1==sum) :
                return i
            sum-=i
        return -1