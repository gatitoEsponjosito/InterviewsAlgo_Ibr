class Solution:
    def reverse(self,num:int):
        if num<=-(2**31) or num>(2**31):
            return 0;
        num=str(num);
        stacki=[];
        activadoMenos=False;
        for char in str(num):
            if char!='-':
                stacki.append(char);
            else:
                activadoMenos=True;
        nuevo=[];
        while stacki:
            nuevo.append(stacki.pop());
        if activadoMenos:
            num= -int(''.join(nuevo));
            if num<-(2**31) or num>(2**31):
                return 0;
            else: return num;
        num= int(''.join(nuevo));
        if num<-(2**31) or num>(2**31):
                return 0;
        else: return num;



def reverse(num:int):
    if num>=2**31 or num<-2**31:
        return 0;
    num=str(num);
    stacki=[];
    activadoMenos=False;
    for char in str(num):
        if char!='-':
            stacki.append(char);
        else:
            activadoMenos=True;
    nuevo=[];
    while stacki:
        nuevo.append(stacki.pop());
    if activadoMenos:
        return -int(''.join(nuevo));
    return int(''.join(nuevo));
if __name__=="__main__":
    num=-12345;
    print(reverse(num));