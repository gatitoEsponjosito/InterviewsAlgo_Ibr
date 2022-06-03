def deCode(s:str()):
    stack=[];
    ns=len(s);
    
    for i in range(ns):
        if s[i]!="]":
            stack.append(s[i]);
        else:
            substr="";
            while stack[-1] !="[":
                substr=stack.pop() + substr;
            stack.pop();
            
            k="";
            while stack and stack[-1].isdigit():
                k=stack.pop()+k;
            stack.append(int(k)*substr);
    return "".join(stack);

if __name__=="__main__":
    print(deCode("2[a2[b]c]"));