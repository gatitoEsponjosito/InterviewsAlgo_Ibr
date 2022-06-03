from random import randint
class Solution:
    def QuickSort(self,arr):
        n=len(arr);
        def quicksort(arr,left,right):
            def partition(arr,left,right,pivot):
                while left<=right:
                    while arr[left]<pivot:
                        left+=1;
                    while arr[right]>pivot:
                        right-=1;
                    if left<=right:
                        arr[left],arr[right]=arr[right],arr[left];
                        left+=1;
                        right-=1;
                return left;
            if left<right:
                pivot=arr[left+(right-left)//2];
                pivot=partition(arr,left,right,pivot);
                quicksort(arr,left,pivot-1);
                quicksort(arr,pivot,right);
            return arr;
        return quicksort(arr,0,n-1);
    
    def BinarySearch(self,arr:list()):
        n=len(arr);
        left=0;
        right=n-1;
        maxi=0;
        while left<=right:
            m=left+(right-left)//2;
            remainderElements=n-m;
            if remainderElements<arr[m]:
                right=m-1;
            elif remainderElements>arr[m]:
                left=m+1;
            else:
                return arr[m];
        return n-left;
    
    def hIndex(self,arr:list()):
        self.QuickSort(arr); #O(NlogN)
        return self.BinarySearch(arr); #O(logN)
        
