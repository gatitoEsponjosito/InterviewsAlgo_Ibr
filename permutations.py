
def permute(arr:list()):
    allpermute=[];
    currentpermutation=[];
    elementsTopermute=arr;
    def dfs(elementsTopermute,currepermutation):
        if elementsTopermute:
            for item in elementsTopermute:
                nextpermute=currepermutation.copy();
                nextpermute.append(item);
                remaining=elementsTopermute.copy();
                remaining.remove(item);
                dfs(remaining,nextpermute);
        else:
            allpermute.append(currepermutation);
    dfs(elementsTopermute,currentpermutation);
    return allpermute;
if __name__=="__main__":
    arr=[1,2,5];
    print(permute(arr))