class Solution:
    def checkbox(self, tl_x, tl_y, board: List[List[str]]):
        #topleft x and topleft y
        track = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for x in range(tl_x, tl_x+3, 1):
            for y in range(tl_y, tl_y+3, 1):
                if (board[x][y] in track):
                    track.remove(board[x][y])
                elif (board[x][y] != "."):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #cols check
        for i in range(0, 9):
            track = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(0, 9):
                if (board[i][j] in track):
                    track.remove(board[i][j])
                elif (board[i][j] != "."):
                    return False
        for i in range(0, 9):
            track = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(0, 9):
                if (board[j][i] in track):
                    track.remove(board[j][i])
                elif (board[j][i] != "."):
                    return False
        #subboxes 0 0 to 2 2, 3 0 to 5 2, 6 0 8 2, 0 3 to 2 5, 3 3 to 5 5, 0 6 to 2 8, 6 3 to 8 5, 3 6 to 5 8, 6 6 to 8 8
        if (self.checkbox(0, 0, board) and self.checkbox(3, 0, board) and self.checkbox(6, 0, board) and self.checkbox(0, 3, board) and self.checkbox(3, 3, board) and self.checkbox(6, 3, board) and self.checkbox(0, 6, board) and self.checkbox(3, 6, board) and self.checkbox(6, 6, board)):
            return True
        else:
            return False