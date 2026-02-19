
      
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BFS(root):
    if not root:
        return
    
    queue = []
    queue.append(root)
    
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.val, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))


print("BFS Level-Order Traversal:")
BFS(root)