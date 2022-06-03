import numpy as np;
def matMulSimple(a,b):
    aRows,aCols=a.shape;
    bRows,bCols=b.shape;
    
    if aCols!=bRows:
        return None;
    
    c=np.zeros((aRows,bCols));
    
    for i in range(aRows):
        for j in range(bCols):
            c[i,j]=0;
            for k in range(aCols):
                c[i,j]+=a[i,k]*b[k,j];
    
    return c;

a=np.random.randint(10,size=(3,4));
b=np.random.randint(10,size=(4,2));
c=matMulSimple(a,b);



print(a);
print(b);
print(c);


def mm1(a,b,c,rowi,rowf,coli,colf):
    n=len(a);
    if rowi==rowf:
        temp=0;
        for k in range(n):
            temp+=a[rowi,k]* b[k,coli];
        c[rowi,coli]=temp;
    else:
        rowmid=(rowi+rowf)//2;
        colmid=(coli+colf)//2;
        mm1(a,b,c,rowi,rowmid,coli,colmid);
        mm1(a,b,c,rowi,rowmid,colmid+1,colf);
        mm1(a,b,c,rowmid+1,rowf,coli,colmid);
        mm1(a,b,c,rowmid+1,rowf,colmid+1,colf);
    

c=mm1(a,b,c,0,len(b[0])-1,0,len(a[0])-1);


print(c);
    





