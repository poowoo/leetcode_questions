class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        while "()" in S:
            print(S)
            S = S.replace("()","")
        return len(S)

def main():
    
    input = ")))"    
    ans = Solution().minAddToMakeValid(input)
    print(ans)
if __name__ == "__main__":
    main()