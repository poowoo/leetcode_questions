# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    path = 0
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.path = 0
        
        
        self.backtrace(root)            
        
        return self.path    

    def backtrace(self, root):
        val = root.val
        nodes = 1
        if root.right:
            v,n = self.backtrace(root.right)
            val += v
            nodes += n
            self.path += abs(v - n)
        if root.left:
            v,n = self.backtrace(root.left)
            val += v
            nodes += n
            self.path += abs(v - n)
        return val,nodes
    
def main():  
    input = TreeNode(1)
    input.right = TreeNode(0)
    input.left = TreeNode(0)
    input.left.right = TreeNode(3)
    ans = Solution().distributeCoins(input)
    print(ans)
if __name__ == "__main__":
    main()