class Solution:
    def numRookCaptures(self, board) -> int:
        px = 0 
        py = 0
        num = 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    px=i
                    py=j
                    break
            if (px+py)!=0:
                break

        if px!=0:
            for i in range(px-1,-1,-1):
                if board[i][py] == '.':
                    continue
                if board[i][py] == 'B':
                    break
                if board[i][py] == 'p':
                    num +=1
                    break
        if px!=7:
            for i in range(px+1,8):
                if board[i][py] == '.':
                    continue
                if board[i][py] == 'B':
                    break
                if board[i][py] == 'p':
                    num +=1
                    break
        if py!=0:
            for i in range(py-1,-1,-1):
                if board[px][i] == '.':
                    continue
                if board[px][i] == 'B':
                    break
                if board[px][i] == 'p':
                    num +=1
                    break
        if py!=7:
            for i in range(py+1,8):
                if board[px][i] == '.':
                    continue
                if board[px][i] == 'B':
                    break
                if board[px][i] == 'p':
                    num +=1
                    break
        return num
        
ls1=[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

s=Solution()
print(s.numRookCaptures(ls1))






