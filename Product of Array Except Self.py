from numpy import fix


def productExceptSelf_Eficiente(arr:list()):
    pre=1;
    n=len(arr);
    output=[1 for item in arr];
    for i in range(1,n):
        pre*=arr[i-1];
        output[i]=pre;
    pre=1;
    for i in range(n-2,-1,-1):
        pre*=arr[i+1];
        output[i]=output[i]*pre;
    return output;

def productExceptSelf_Eficency(arr:list()):
    n=len(arr);
    pre=1;
    output=[1 for i in range(n)];
    for i in range(1,n):
        pre*=arr[i-1];
        output[i]=pre;
        
    pre=1;
    for i in range(n-2,-1,-1):
        pre*=arr[i+1];
        output[i]=pre*output[i];
    return output;
def productExceptSelf_Ineficiente(arr:list()):
    n=len(arr);
    arrtemp=[1]*n;
    memo={};
    memonumeros={};
    def dp(i,j):
        if j<0: return 1;
        if i>n-1: return 1;
        if i+1==j:
            if not (arr[i],arr[j]) in memonumeros:
                memonumeros[(arr[i],arr[i+1])]=arr[i]*arr[j];
            return memonumeros[(arr[i],arr[i+1])];
        if i==j:
            return arr[i];
        if not (i,j) in memo:
            m=(j+i)//2;
            memo[(i,j)]=dp(i,m)*dp(m+1,j);
        return memo[(i,j)];
    left=0;
    right=n-1;
    for i in range(n):
        arrtemp[i]*=dp(left,i-1)*dp(i+1,right);
    return arrtemp;

if __name__=="__main__":
    arr=[1,2,3,4];
    print(productExceptSelf_Eficency(arr));