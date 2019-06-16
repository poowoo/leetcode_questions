class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        i = 0
        j = 0
        count = 0
        tmp = 0
        print(board[0].count("X"))
        list_len = len(board[0])
        for i in range(len(board)):
        	for j in range(list_len):
        		if board[i][j] == 'X':
        			count += 1
        			if i + 1 < len(board):
        				if board[i+1][j] == 'X':
        					tmp += 1
        			if i - 1 >= 0:
        				if board[i-1][j] == 'X':
        					tmp += 1
        			if j + 1 < len(board[0]):
        				if board[i][j+1] == 'X':
        					tmp += 1
        			if j - 1 >= 0:
        				if board[i][j-1] == 'X':
        					tmp += 1

        return int(count - (tmp/2))
        
if __name__ == '__main__':
    board=["X..X",".X.X","X.XX"]
    a = Solution()
    b = a.countBattleships(board)
    print(b)
    #X..X"
    #.X.X"
    #X.XX