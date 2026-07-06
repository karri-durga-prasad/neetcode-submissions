class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rd={}
        cd={}
        bd={}
        for i in range (9):
            rd={}
            for j in board[i]:
                if j in rd and j!='.':
                    return False
                else:
                    rd[j]=1
        for l in range(9):
            cd={}
            for m in range(9):
                if board[m][l] in cd and board[m][l]!='.' :
                    return False
                else:
                    cd[board[m][l]]=1

        p=0
        z=0
        while p<9:
            bd={}
            for x in range(p,p+3):
                for y in range(z,z+3):
                    if board[x][y] in bd and board[x][y] != '.':
                        return False
                    else:
                        bd[board[x][y]] = 1
            
            z=y+1
            if z>=8:
                p+=3
                z=0
        return True
                
                

                    
                    
                


        