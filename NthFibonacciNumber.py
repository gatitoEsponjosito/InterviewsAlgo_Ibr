
def NthFibonacciNumber(num:int):
    memo={}
    memo[0]=0; 
    memo[1]=1;
    for i in range(2,num+1):
        memo[i]=memo[i-1]+memo[i-2];
    return memo[num];
    

if __name__=="__main__":
    print(NthFibonacciNumber(4));
    print(NthFibonacciNumber(9));
    print(NthFibonacciNumber(10));
    print(NthFibonacciNumber(13));