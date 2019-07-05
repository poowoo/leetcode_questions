# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.left:
            root.left = self.pruneTree(root.left)                        
        if root.right:
            root.right = self.pruneTree(root.right)                         
        
        if root.right is None and root.left is None:
            if root.val is 0:
                return None
            else:
                return root
        return root

def main():
    
    input = [8,5,1,7,10,12]      
    ans = Solution().pruneTree(input)
    print(ans)
if __name__ == "__main__":
    main()