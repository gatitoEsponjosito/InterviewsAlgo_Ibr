
from collections import deque


def noRepeatingChrs(s:str()):
    stack=deque();
    dic=dict();
    for ch in s:
        if not ch in dic:
            dic.update({ch:1});
        else:
            dic.update({ch:dic.get(ch)+1});
    for key in dic.keys():
        stack.append((key,dic.get(key)));
    s="";
    while stack:
        key,frec=stack.popleft();
        s+=key;
        stack.append((key,frec-1)) if frec>0 else None;
    return s;
# ta mal unu
if __name__=="__main__":
    print(noRepeatingChrs("abbccc"));