# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max_num)
        right_list = nums[max_index + 1:]
        left_list = nums[:max_index]
        if len(right_list) > 0:
            if len(right_list) == 1:
                root.right = TreeNode(right_list[0])
            else:
                root.right = self.constructMaximumBinaryTree(right_list)                    
        if len(left_list) > 0:
            if len(left_list) == 1:
                root.left = TreeNode(left_list[0])
            else:                
                root.left =self.constructMaximumBinaryTree(left_list)
        return root

def main():
    
    input = [3,2,1,6,0,5]
    
    
    ans = Solution().constructMaximumBinaryTree(input)
    print(ans)
if __name__ == "__main__":
    main()