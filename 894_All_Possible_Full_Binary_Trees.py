# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        N -= 1
        if N == 0: return [TreeNode(0)]
        ret = []
        for l in range(1, min(20, N), 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        return ret
            
    
            

"""
class Solution(object):
    def allPossibleFBT(self, N):
        
        #:type N: int
        #:rtype: List[TreeNode]
        
        if N % 2 == 0:
            return []
        tree_list = []
        found = False
        tree_tmp = self.initFBT(N)
        tree_list.append(copy.copy(tree_tmp))
        i = 0        
        while found is False:            
            tree_tmp,test = self.getFBT(tree_tmp, N - 1)            
            tree_list.append(copy.copy(tree_tmp))            
            
            if self.checkFBT(N,tree_tmp) is True:
                found = True
            i += 1          
            
        return tree_list
    def copytree(self, new, root):
        if root.right:
            new.right = TreeNode(0)
            copyright(new.right, root.right)
        if root.left:
            new.left = TreeNode(0)
            copyright(new.left, root.left)
    def getFBT(self, root, n):
        change = False
         
        # four case to change tree node
        if root.right:
            if n is 4 and root.right.right is not None:
                root.right.right = None
                root.right.left = None
                root.left.right = TreeNode(0)
                root.left.left = TreeNode(0)                
                return root,True            
            if n is 4 and root.left.right is not None:
                root.left.right = None
                root.left.left = None
                return root,False
            if n > 4:
                root.right,change = self.getFBT(root.right, n-2)
            if change is True:
                return root,True
        if n is 6 and root.right and root.left:
            if root.right.right and root.left.right is None:                
                root.left.right = TreeNode(0)
                root.left.left = TreeNode(0)                
                return root,True
        if n is 6 and root.right and root.left:
            if root.right.right and root.left.right:
                if root.right.right.right is None and root.left.right.right is None:
                    root.right.right = None
                    root.right.left = None
                    root.left.right.right = TreeNode(0)
                    root.left.right.left = TreeNode(0)                    
                    return root,True
        if root.left:
            if n > 4:
                root.left,change = self.getFBT(root.left, n-2)
                if change is True:
                    return root,True        
        return root,change
                            
    def initFBT(self,N):
        child_level = (N-3) / 2 + 1
        level = 0
        root = TreeNode(0)
        tmp = root
        while level < child_level:            
            tmp.left = TreeNode(0)            
            tmp.right = TreeNode(0)
            tmp = tmp.right
            level += 1                    
        return root

    def checkFBT(self, N, root):
        child_level = (N-3) / 2 + 1
        level = 0
        while level < child_level:
            if root.left is not None:
                root = root.left
                level += 1
            else:
                return False
        return True
"""
def main():
    
    input = 7    
    ans = Solution().allPossibleFBT(input)
    print(ans)
if __name__ == "__main__":
    main()