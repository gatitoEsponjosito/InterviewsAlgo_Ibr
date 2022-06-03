class Solution:
    def buddyStrings(self,A:str,B:str):
        l1=len(A);
        l2=len(B);
        if l1!=l2:
            return False;
        if A==B:
            return True;
        temp=0;
        valor=True;
        cont=0;
        for i in range(l1):
            if A[i]!=B[i]:
                if cont+1==3:
                    return False;
                cont+=1;
                if valor:
                    temp=A[i];
                    valor=False;
                elif temp==B[i]:
                    return True;

print(Solution().buddyStrings('aaaaaaabc','aaaaaaacb'));
print(Solution().buddyStrings('aaaaaabbc','aaaaaaacb'));