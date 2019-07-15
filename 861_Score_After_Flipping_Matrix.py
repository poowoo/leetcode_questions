class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    if A[i][j] is 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0      
                
        for i in range(len(A[0])):
            zero_num = 0
            for j in range(len(A)):
                if A[j][i] == 0:
                    zero_num += 1
            if zero_num > len(A) - zero_num:
                for j in range(len(A)):
                    if A[j][i] == 0:
                        A[j][i] = 1
                    else:
                        A[j][i] = 0
            for j in range(len(A)):
                if A[j][i] == 1:
                    ans += pow(2,len(A[0]) - i - 1)
        
        
            
        return ans

def main():  
    input = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]    
    ans = Solution().matrixScore(input)
    print(ans)
if __name__ == "__main__":
    main()