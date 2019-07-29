
class Solution(object):
    all_nodes = []
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for n in graph[0]:            
            t = [0]
            self.backtrace(n, graph, t)
        return self.all_nodes

    def backtrace(self, i, graph, l):     
        
        if len(graph[i]) > 0:
            l.append(i)
            len_l = len(l)
            for n in graph[i]:                
                self.backtrace(n, graph, l)
                l = l[:len_l]                
        else:
            l.append(i)
            self.all_nodes.append(l)
    



        
def main():  
    input = [[4,3,1],[3,2,4],[3],[4],[]] 
    #[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    #input = [[1,2], [3], [3], [] ]
    ans = Solution().allPathsSourceTarget(input)
    print(ans)
if __name__ == "__main__":
    main()