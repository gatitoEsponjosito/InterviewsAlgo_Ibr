
def largestNumber(arr):  
    if len(arr)==1: 
        return str(arr[0])
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    for i in range(len(arr)):
        for j in range(1+i,len(arr)):
            if arr[j]+arr[i]>arr[i]+arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    result=''.join(arr)
    if(result=='0'*len(result)):
        return '0'
    else:
        return result
    
if __name__=="__main__":
    arr=[17,78,2,45,79,80];
    print(2*10**9);
    print(2*10**300000);
    print(largestNumber(arr));