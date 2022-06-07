
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val;
        self.left=left;
        self.right=right;

def MinimumSum(node:object()):
    mini=0;
    def dfs(node:object(),suma):
        if not node:
            return suma;
        suma=(dfs(node.left,suma)+dfs(node.right,suma));
        suma+=node.val;
        return suma;
    return min(dfs(node.left,mini),dfs(node.right,mini));

if __name__=="__main__":
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)

    print(MinimumSum(node));