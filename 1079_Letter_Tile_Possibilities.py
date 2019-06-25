
output = []
class Solution(object):   
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        output[:] = []
        
        link_list = list(tiles)
        visit = [False] * len(link_list)
        for i in range(len(link_list)):
            visit[i] = True            
            self.DFS(i,link_list[i],link_list,visit)
            visit[i] = False
        return len(set(output))
    def DFS(self,i,alpha,link_list,visit):        
        n_visit = visit.copy()        
        output.append(alpha)                
        
        for j in range(len(link_list)):
            if n_visit[j] is not True:
                
                n_visit[j] = True
                self.DFS(j,alpha + link_list[j],link_list,n_visit)
                n_visit[j] = False
    
    
def main():
    
    num = Solution().numTilePossibilities("LJBWSXL")#"LJBWSXL"
    print(num)
if __name__ == "__main__":
    main()