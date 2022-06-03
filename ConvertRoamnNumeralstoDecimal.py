
def convertND(s:str()):
    convert=dict();
    #convert llave: (reemplazo,pos)
    convert.update({"I":(1,0)});
    convert.update({"V":(5,1)});
    convert.update({"X":(10,2)});
    convert.update({"L":(50,3)});
    convert.update({"C":(100,4)});
    convert.update({"D":(500,5)});
    convert.update({"M":(1000,6)});
    n=len(s);
    number=0;
    number+=convert[s[-1]][0];
    for i in range(n-2,-1,-1):
        if (convert[s[i]][1]>=convert[s[i+1]][1]):
            number+=convert[s[i]][0];
        else: number-=convert[s[i]][0];
    return number;

if __name__=="__main__":
    print(convertND("MCMIV"));