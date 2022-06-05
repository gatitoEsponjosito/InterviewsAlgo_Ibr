
def solveString(s1:str(),s2:str()):
    ns1=len(s1);
    ns2=len(s2);
    if (ns1!=ns2): return False;
    num=s1[0];
    i=0; j=0;
    encontrado=False;
    while (j<ns2):
        if (num==s2[j]): 
            encontrado=1;
            break;
        j+=1;
    if not encontrado:
        return False;
    
    while (i<ns1):
        if j>=ns2:
            j=0;
        if (s1[i]!=s2[j]):
            return False;
        i+=1; j+=1;
    return True;


if __name__=="__main__":
    print(solveString("abcde","cdeab"));
    print(solveString("abc","acb"));