# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val < val:
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val)                
        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                root.left = TreeNode(val)                
        return root
def main():
    node_val = [4,2,7,1,3,None,None]        
    root = TreeNode(node_val[0])
    root.left = TreeNode(node_val[1])
    root.right = TreeNode(node_val[2])
    root.left.left =  TreeNode(node_val[3])
    root.left.right =  TreeNode(node_val[4])
    num = Solution().insertIntoBST(root,8)#"LJBWSXL"
    print(num)
if __name__ == "__main__":
    main()