
class Connect4():


    def __init__(self):
        
        self.board = None

        self.initalize_board()
        self.board_max_row = 5
        self.board_max_col = 6

        self.round = 1
        self.player_color = 1
        self.has_winner = False
        self.tie = False


    def initalize_board(self):

        self.board = [
                       [0,0,0,0,0,0,0], 
                       [0,0,0,0,0,0,0], 
                       [0,0,0,0,0,0,0], 
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0]
                     ]

        self.round = 1
        self.player_color = 1
        self.has_winner = False
        self.tie = False
        
        return None


    def update_player_color(self):

        if (self.player_color == 1):  # player 1
            self.player_color = 2
        else:
            self.player_color = 1

        return self.player_color
            

    def place_piece(self,column):
        
        max_row = 5
        while (max_row >= 0 and self.board[max_row][column] != 0):
            print(max_row, column, self.board[max_row][column])
            max_row -= 1

        if (max_row < 0): # this column is full
            return -1

        self.board[max_row][column] = self.player_color


        self.is_winning_move(max_row, column)

        self.round+=1
        print(self.round)
        if (self.has_winner == False and (self.round > (self.board_max_row+1) * (self.board_max_col+1))):
            self.tie = True  # board is full, tie

        return max_row

    def is_winning_move(self, r, c):

        if (self.check_down(r,c)):
            self.has_winner = True
            return True
        
        if (self.check_horizontal(r,c)):
            self.has_winner = True
            return True

        if (self.check_diagonal_left_up(r,c)):
            self.has_winner = True
            return True

        if (self.check_diagonal_right_up(r,c)):
            self.has_winner = True
            return True

        return False
               
    def check_down(self,r,c):

        count = 1
        for i in range(3):
            if (r+1 <= self.board_max_row and self.board[r+1][c] == self.player_color):
                r+=1
                count+=1
            else:
                break

        return count >= 4

    def check_horizontal(self,r,c):

        count = 1 #this piece itself
        original_c = c

        #count left
        for i in range(3):
            if (c-1 >= 0 and self.board[r][c-1] == self.player_color):
                c-=1
                count+=1
            else:
                break
            
        c = original_c

        #count right
        for i in range(3):
            if (c+1 <= self.board_max_col and self.board[r][c+1] == self.player_color):
                c+=1
                count+=1
            else:
                break

        return count >= 4

    def check_diagonal_left_up(self,r,c):

        count = 1 #this piece itself
        original_c = c
        original_r = r

        #count left up
        for i in range(3):
            if (c-1 >= 0 and r-1 >= 0 and self.board[r-1][c-1] == self.player_color):
                c-=1
                r-=1
                count+=1
            else:
                break

        #reset c and r value
        c = original_c
        r = original_r

        #count right down
        for i in range(3):
            if (c+1 <= self.board_max_col and r+1 <= self.board_max_row and self.board[r+1][c+1] == self.player_color):
                c+=1
                r+=1
                count+=1
            else:
                break

        return count >= 4


    def check_diagonal_right_up(self,r,c):

        count = 1 #this piece itself
        original_c = c
        original_r = r

        #count right up
        for i in range(3):
            if (c+1 <= self.board_max_col and r-1 >= 0 and self.board[r-1][c+1] == self.player_color):
                c+=1
                r-=1
                count+=1
            else:
                break

        #reset c and r value
        c = original_c
        r = original_r

        #count left down
        for i in range(3):
            if (c-1 >= 0 and r+1 <= self.board_max_row and self.board[r+1][c-1] == self.player_color):
                c-=1
                r+=1
                count+=1
            else:
                break


        return count >= 4

