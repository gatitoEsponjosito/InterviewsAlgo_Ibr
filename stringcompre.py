
def solveStringCompression(arr:list(str())):
    resp="";
    passlettter="";
    cont=1;
    for i in range(len(arr)):
        if passlettter!=arr[i]:
            if i!=0:
                if cont>1:
                    resp+=str(cont);
                cont=1;
            resp+=str(arr[i]);
        else:
            cont+=1;
        passlettter=arr[i];
    if cont>1:
        resp+=str(cont);
    arr=str(resp);
    print(list(arr));
    return len(resp);

def stringcomre(chars:list(str())):
    index=0;
    i=0;
    while (i<len(chars)):
        j=i;
        while (j<len(chars) and chars[j]==chars[i]):
            j+=1;
        chars[index]=chars[i];
        index+=1;
        if (j-i)>1: 
            count=str(j-i)+"";
            for char in count:
                chars[index]=char;
                index+=1;
        i=j;
    for i in range(len(chars)-index):
        chars.pop();
    print(chars);
    return len(chars);

def solveStringCompreuwu(arr:list(str())):
    n=len(arr);
    i=0;
    index=0;
    while i<n:
        j=i;
        while (j<n and arr[j]==arr[i]):
            j+=1;
        arr[index]=arr[i];
        index+=1;
        if j-i>1:
            count=str(j-i);
            for ch in count:
                arr[index]=ch;
                index+=1;
        i=j;
    for i in range(n-index):
        arr.pop();
    return arr;

print(solveStringCompreuwu(["a","a","a"]))
