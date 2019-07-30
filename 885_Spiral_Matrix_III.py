class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        index = 0
        ans = []
        move_way = [1,0,0,0]
        move_s = 0
        move_len = 2       
        time = 0     
        while index < R * C:
            node = [r0,c0]            
            ans.append(node)                 
            if index == R * C - 1:
                break
            while 1:
                move_s += 1
                if move_way[0] is 1:
                    c0 += 1                    
                    if move_s == (move_len/2):
                        move_way[0] = 0
                        move_way[1] = 1
                        move_s = 0
                        time += 1
                elif move_way[1] is 1:
                    r0 += 1                    
                    if move_s == (move_len/2):
                        move_way[1] = 0
                        move_way[2] = 1
                        move_s = 0
                        time += 1
                elif move_way[2] is 1:
                    c0 -= 1                    
                    if move_s == (move_len/2):
                        move_way[2] = 0
                        move_way[3] = 1
                        move_s = 0
                        time += 1
                elif move_way[3] is 1:
                    r0 -= 1                    
                    if move_s == (move_len/2):
                        move_way[3] = 0
                        move_way[0] = 1
                        move_s = 0
                        time += 1
                if time == 2:
                    move_len = 2 * ((move_len/2) + 1)
                    time = 0
                if 0 <= r0 and r0 < R and 0 <= c0 and c0 < C:
                    break
            index += 1
        return ans

    


def main():  
    
    input = [5, 6, 1, 4]
    ans = Solution().spiralMatrixIII(5,6,1,4)
    print(ans)
if __name__ == "__main__":
    main()