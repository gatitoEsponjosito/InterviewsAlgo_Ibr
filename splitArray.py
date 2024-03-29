class Solution:
    def splitArray_DynamicProgramming(self,nums: list[int],m:int):
        dp={};
        
        def dfs(i,m):
            if m==1:
                return sum(nums[i:]);
            
            if (i,m) in dp:
                return dp[(i,m)];
            
            res,curSum= float('inf'),0;
            for j in range(i,len(nums)-m+1):
                curSum+=nums[j];
                maxSum=max(curSum,dfs(j+1,m-1));
                res=min(res,maxSum);
                if curSum> res:
                    break;
            
            dp[(i,m)]=res;
            return res;
        return dfs(0,m);
    
    def SplitArray_BinarySearch(self, nums:list[int],m:int):
        def canSplit(largest):
            subarray=0;
            curSum=0;
            for n in nums:
                curSum+=n;
                if curSum>largest:
                    subarray+=1;
                    curSum=n;
            return subarray+1<=m;
        l,r=max(nums),sum(nums);
        res=r;
        while l<=r:
            mid= l+(r-l)//2;
            if canSplit(mid):
                res=mid;
                r=mid-1;
            else:
                l=mid+1;
        return res;