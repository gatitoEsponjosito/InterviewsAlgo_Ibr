
class Node:
    def __init__(self,val):
        self.val=val;
        self.left=None;
        self.right=None;
    
    def __repr__(self):
        return self.val;
    

def deepest(node):
    if node==None:
        return None;
    max=0;
    maxn=0;
    def dfs(at,cont):
        if at==None:
            return;
        nonlocal max;
        nonlocal maxn;
        if cont>=max:
            max=cont;
            maxn=at.val;
        dfs(at.left,cont+1);
        dfs(at.right,cont+1);
    cont=1;
    dfs(node,cont)
    return maxn,max;

root =Node('a');
root.left=Node('b');
root.left.left=Node('d');
root.right=Node('c');

print(deepest(root));