import heapq
from queue import PriorityQueue

class HeapDefinitivo:
    def __init__(self,comp):
        self.hp=[];
        self.size=0;
        self.comp=comp;
        
    def add(self, element):
        self.hp.append(element);
        self.size+=1;
        if self.size<=1:
            return;
        i =self.size-1;
        parent=(i-1)//2;
        while self.comp(self.hp[i],self.hp[parent]):
            self.hp[parent],self.hp[i]=self.hp[i],self.hp[parent];
            i=parent;
            if parent==0:
                break;
            parent=(i-1)//2;
            
    def pop(self):
        if self.size==0:
            return;
        removeElement=self.hp[0];
        self.hp[0]=self.hp[self.size-1];
        self.hp.pop();
        self.size-=1;
        i=0;
        while (i<(self.size-1)//2):
            left=i*2+1;
            right=i*2+2;
            if (self.comp(self.hp[i],self.hp[left])\
                or self.comp(self.hp[i],self.hp[right])):
                if self.comp(self.hp[right],self.hp[left]):
                    self.hp[left],self.hp[i]=\
                        self.hp[i],self.hp[left];
                    i=left;
                else:
                    self.hp[right],self.hp[i]=\
                        self.hp[i],self.hp[right];
                    i=right;
            else: break;
        right=i*2+2;
        left=i*2+1;
        if right<self.size and left<self.size:
            if (self.comp(self.hp[i],self.hp[left])\
                or self.comp(self.hp[i],self.hp[right])):
                if self.comp(self.hp[right],self.hp[left]):
                    self.hp[left],self.hp[i]=\
                        self.hp[i],self.hp[left];
                    i=left;
                else:
                    self.hp[right],self.hp[i]=\
                        self.hp[i],self.hp[right];
                    i=right;
        elif (right<self.size and self.comp(self.hp[i],self.hp[right])):
            self.hp[right],self.hp[i]=\
                self.hp[i],self.hp[right];
        elif (left<self.size and self.comp(self.hp[i],self.hp[left])):
            self.hp[left],self.hp[i]=\
                self.hp[i],self.hp[left];
        return removeElement;
    
    def _size(self):
        return self.size;
    def __str__(self):
        return str(self.hp[:self.size]);
    def top(self):
        return self.hp[0];
    

def solveReorganizeString(s:str()):
    dic=dict();
    result="";
    for c in s:
        dic.update({c:dic.get(c,0)+1});
    q=HeapDefinitivo(lambda a,b: a[0]>b[0]);
    [q.add((dic.get(key),key)) for key in dic.keys()];
    while q.size>1:
        count1,currentele=q.pop();
        count2,nextele=q.pop();
        result+=currentele;
        result+=nextele;
        dic.update({currentele:count1-1});
        dic.update({nextele:count2-1});
        if dic.get(currentele)>0:
            q.add((dic.get(currentele),currentele));
        if dic.get(nextele)>0:
            q.add((dic.get(nextele),nextele));
    
    if q.size:
        c,last=q.pop();
        if c>1:
            return "";
        result+=last;
    return result;

if __name__=="__main__":
    print(solveReorganizeString("aab"));