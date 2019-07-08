class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partion = []
        i = 0
        while i < len(S):
            l = self.getsize(S[i:]) + 1
            partion.append(l)
            i += l
        return partion

    def getsize(self,S):
        begin_c = S[0]
        tmp_last = S.rindex(begin_c)        
        i = 0
        while i < tmp_last:
            if S[i] != begin_c and S.rindex(S[i]) > tmp_last:
                tmp_last = S.rindex(S[i])
            i += 1
        return tmp_last
        
        
        
            

    

def main():
    
    input = "ababcbacdefaegdiehijhklij"
    
    ans = Solution().partitionLabels(input)
    print(ans)
if __name__ == "__main__":
    main()