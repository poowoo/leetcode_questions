#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = None
        for num in preorder:
            root = self.addnode(root,num)
        return root 
    def addnode(self, root, num):
        if root:
            if num < root.val:
                root.left = self.addnode(root.left,num) 
            if num > root.val:
                root.right = self.addnode(root.right,num)
            return root
        else:
            return TreeNode(num)        

def main():
    
    input = [8,5,1,7,10,12]
    
    
    ans = Solution().bstFromPreorder(input)
    print(ans)
if __name__ == "__main__":
    main()