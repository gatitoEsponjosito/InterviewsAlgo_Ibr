
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val;
        self.left=left;
        self.right=right;

def solve(node:object()):
    if (node==None): return;
    print(node.val);
    solve(node.left);
    solve(node.right);

if __name__=="__main__":
    root=Node(1,Node(2),Node(3,Node(4),Node(5)));
    solve(root);