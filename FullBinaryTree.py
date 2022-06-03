from collections import deque

class Node(object):
    def __init__(self,value,left=None,right=None):
        self.left=left;
        self.right=right;
        self.value=value;
    
    def __str__(self):
        q=deque();
        q.append(self);
        result='';
        while q:
            num=len(q);
            while num>0:
                n=q.popleft();
                result+=str(n.value);
                if n.left:
                    q.append(n.left);
                if n.right:
                    q.append(n.right);
                num=num-1;
            if q:
                result+="\n";
        return result;

def fullBinaryTree(node:object()):
    if node==None:
        return None;
    left=fullBinaryTree(node.left);
    right=fullBinaryTree(node.right);
    node.left=left; node.right=right;
    if left==None and right==None:
        return node;
    elif right==None:
        return left;
    elif left==None:
        return right;
    return node;

if __name__=="__main__":
    tree=Node(1);
    tree.left=Node(2);
    tree.right=Node(3);
    tree.right.right=Node(4);
    tree.right.left=Node(9);
    tree.left.left=Node(0);
    print(fullBinaryTree(tree));