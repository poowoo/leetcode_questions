# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    sum_tmp = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = []        
        new_node = []
        tree_depth = 0
        max_depth = 0
        j = 0
        p = 0
        for i in range(len(root)):            
            node.append(TreeNode(root[i]))                            
            if i == p + 2 ** tree_depth:
                 tree_depth += 1
                 max_depth = tree_depth
                 p = i
        tree_depth = 0                
        p = 1
        for i in range(len(root) - 2 ** max_depth):
            node[i].left = node[p + j]
            j += 1
            node[i].right = node[p + j]
            j += 1
            if j == 2 ** (tree_depth + 1):
                tree_depth += 1
                j = 0
                p = i + (2 ** tree_depth) + 1        
        self.bstSearch(node[0])
        for n in node:
            new_node.append(n.val)
        return new_node
    
    def bstSearch(self,node):    
        if node.right is not None and node.right.val is not None:
            self.bstSearch(node.right)
        node.val += self.sum_tmp
        self.sum_tmp = node.val                          
        if node.left is not None and node.left.val is not None: 
            self.bstSearch(node.left)                                               
        
        


                
                                
        
        
def main():
    #        0  1  2  3  4  5  6  7    8    9    10 11   12   13   14
    input = [4, 1, 6, 0, 2, 5, 7, None,None,None, 3,None,None,None,8]
    #       [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    
    ans = Solution().bstToGst(input)
    print(ans)
if __name__ == "__main__":
    main()

""" leetcode answer
class Solution(object):
    sum_tmp = 0
    def bstToGst(self, root):
        
        #:type root: TreeNode
        #:rtype: TreeNode
        
        
        if root.right is not None:
            self.bstToGst(root.right)
                  
        root.val += self.sum_tmp
        self.sum_tmp = root.val
             
        if root.left is not None: 
            self.bstToGst(root.left)
        
        return root
"""