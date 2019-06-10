class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        ans = list()
        for num1 in nums:
            for num2 in nums:
                if target == num1 + num2:
                    if i != j:
                        ans.append(i)
                        ans.append(j)
                        return ans
                j += 1                
            i += 1
            j = 0 
    
if __name__ == '__main__':
    
    nums=[3,2,4]
    a = Solution()
    b = a.twoSum(nums,6)
    print (b[0],b[1])