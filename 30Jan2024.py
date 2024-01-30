from ast import List


class Solution:
    def f(self,b:int,a:int,t:chr) :
        if(t=='+') :
            return a+b
        elif(t=='-') :
            return a-b
        elif(t=='*') :
            return a*b
        else :
            return a/b
        
    def evalRPN(self, tokens: List[str]) -> int:
        st = ("-","+","*","/")
        stk = []
        for t in tokens :
            if(t in st) :
                stk.append(self.f(int(stk.pop()),int(stk.pop()),t[0]))
            else :
                stk.append(t)
        return int(stk[0])