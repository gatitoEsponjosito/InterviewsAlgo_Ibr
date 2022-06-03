def solveStringCompression(arr:list()):
    n=len(arr);
    letraanterior=str();
    cont=0;
    for i in range(n):
        if letraanterior!=arr[i]:
            print(cont,end="") if cont>1 else None;
            cont=1;
            print(arr[i],end="");
        else:
            cont+=1;
        letraanterior=arr[i];
    if cont>1:
        print(cont,end="");

def solveStringCompression(arr:list()):
    n=len(arr);
    letraanterior=str();
    cont=0;
    for i in range(n):
        if letraanterior!=arr[i]:
            arr[i-1]=str(cont) if cont>1 else letraanterior;
            cont=1;
        else:
            cont+=1;
        letraanterior=arr[i];
    if cont>1:
        arr[n-cont+1]=str(cont);
    arr=arr[:n-cont+2];
    print(arr);

def solveLenghtStringCompression(arr:list()):
    n=len(arr);
    letraanterior=str();
    cont=0;
    lenght=0;
    for i in range(n):
        if letraanterior!=arr[i]:
            lenght+=1 if cont>1 else None;
            cont=1;
            lenght+=1
        else:
            cont+=1;
        letraanterior=arr[i];
    if cont>1:
        lenght+=1
    return lenght;

if __name__=="__main__":
    solveStringCompression(["a"]);

if __name__=="__main__":
    solveStringCompression(["a"]);