class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val;
        self.next=next;
        self.prev=prev;
        
class node:
    def __init__(self,val,prev=None,next=None):
        self.val=val;
        self.prev=prev;
        self.next=next;

def reverse(node:object()):
    inicial=node.next;
    prev=None;
    curr=inicial;
    nextnode=curr.next;
    while curr:
        curr.next=prev;
        prev=curr;
        curr=nextnode;
        nextnode=curr.next if curr else None;
    return prev;

def isPalindromeSLL(node:object()):
    aux=node;
    n=0;
    while aux.next:
        aux=aux.next;
        n+=1;
    n+=1;
    middle=round(n/2);
    i=0;
    aux=node;
    while i<middle-1:
        aux=aux.next;
        i+=1;
    aux.next=reverse(aux);
    begin=node;
    begin2=aux.next;
    palindr=True;
    while begin2:
        if (begin2.val!=begin.val):
            palindr=False;
            break;
        begin2=begin2.next;
        begin=begin.next;
    return palindr;

def isPalindromeDLL(node:object()):
    begin=node;
    aux=begin;
    n=0;
    while aux.next:
        aux=aux.next;
        n+=1;
    n+=1;
    i=0; j=n-1;
    end=aux;
    palindr=True;
    while i<j:
        if (begin.val!=end.val):
            palindr=False;
            break;
        begin=begin.next;
        end=end.prev;
        i+=1;j-=1;
    return palindr;

def pruebaPalindrDLL():
    node = Node('a')
    node.next = Node('b')
    node.next.prev = node
    node.next.next = Node('b')
    node.next.next.prev = node.next
    node.next.next.next = Node('a')
    node.next.next.next.prev = node.next.next
    print(isPalindromeDLL(node));

def pruebaPalindrSLL():
    nodo=node('a');
    begin=nodo;
    nodo.next=node('b');
    nodo=nodo.next;
    nodo.next=node('a');
    print(isPalindromeSLL(begin));
if __name__=="__main__":
    #pruebaPalindrDLL();
    pruebaPalindrSLL();