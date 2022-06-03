#O(n) time
#O(1) space
def unique(arr:list()):
    n=len(arr);
    for i in range(n):
        x=arr[i]%n;
        arr[x]=arr[x]+n;
    print("The unique element is: ");
    for item in arr:
        if (arr[item%n]<n*2):
            print(item%n," ");
    print("The repeating element is: ");
    for item in range(n):
        if (arr[item]>=n*2):
            print(item%n," ");

if __name__=="__main__":
    arr=[2,3,4,5,2,3,1,1,5];
    unique(arr);