class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """                
        sum = 0
        while(n >= 1):
            if int(n) % 2 == 1:
                sum += 1
            n /= 2                
        return sum

def main():  
    
    input = int('11111111111111111111111111111101',2)
    ans = Solution().hammingWeight(input)
    print(ans)
if __name__ == "__main__":
    main()