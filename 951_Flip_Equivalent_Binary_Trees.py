# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        check = True
        if root1 is None:
            if root2 is None:
                return True
            else:
                return False
        else:
            if root2 is None:
                return False
            if root1.val != root2.val:
                return False
        #root1 != None and root2 != None
        #                         
        check = self.flipEquiv(root1.right,root2.right)
        if check is False:
            check = self.flipEquiv(root1.right,root2.left)
            if check is True:
                check = self.flipEquiv(root1.left,root2.right)
            else:
                return False
        else:
            check = self.flipEquiv(root1.left,root2.left)
        return check

def main():  
    
    input = TreeNode(0)
    ans = Solution().flipEquiv(input)
    print(ans)
if __name__ == "__main__":
    main()