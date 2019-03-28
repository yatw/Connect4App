from flask import Flask, render_template, request, jsonify
from connect4 import Connect4
app = Flask(__name__)

game = Connect4()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('board.html')

@app.route("/_game_status", methods=['GET', 'POST'])
def game_status():

    game_on = True
    
    if (game.has_winner):
        game_on = False
        
    return jsonify(game_status = str(game_on))


@app.route("/_player_move", methods=['GET', 'POST'])
def player_move():

    column = request.args.get('column',0, type=int)
    row = game.place_piece(column)
    print("Placed a piece at column: " + str(column) + " row: " + str(row))

    if (row < 0):
        return jsonify(row=-1)

    player_color = game.player_color
    game.update_player_color()

    return jsonify(row=row, color = player_color, win=str(game.has_winner))

'''
@app.route('/_add_numbers')
def add_numbers():
    print("I m stupid so i choose to run this instead")
    a = request.args.get('a', 5, type=int)
    b = request.args.get('b', 5, type=int)
    return jsonify(result=a + b)



turn = 1
gameover = False;
while not gameover:
print('enter the column')
column = int(input()) - 1  #3
row = 5
print(column, type(column))
print(row, type(row))

while (board[row][column] != 0):
    row = row - 1
if turn % 2 == 0:    #0 = Player 1
    board[row][column] = 1
else:
    board[row][column] = 2

turn = turn + 1

if turn % 2 == 0 and board[row][column] == 1 and board[row + 1][column] == 1 and board[row + 2][column] == 1 and board[row + 3][column] == 1: #down
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row][column - 1] == 1 and board[row][column - 2] == 1 and board[row][column - 3] == 1: #left
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row][column + 1] == 1 and board[row][column + 2] == 1 and board[row][column + 3] == 1: #right
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row + 1][column - 1] == 1 and board[row + 2][column - 2] == 1 and board[row + 3][column - 3] == 1: #left diagonal down
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row + 1][column + 1] == 1 and board[row + 2][column + 2] == 1 and board[row + 3][column + 3] == 1: #right diagonal down
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row - 1][column - 1] == 1 and board[row - 2][column - 2] == 1 and board[row - 3][column - 3] == 1: #left diagonal up
    gameover = True
elif turn % 2 == 0 and board[row][column] == 1 and board[row - 1][column + 1] == 1 and board[row - 2][column + 2] == 1 and board[row - 3][column + 3] == 1: #right diagonal up
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row + 1][column] == 1 and board[row + 2][column] == 1 and board[row + 3][column] == 1: #down
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row][column - 1] == 1 and board[row][column - 2] == 1 and board[row][column - 3] == 1: #left
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row][column + 1] == 1 and board[row][column + 2] == 1 and board[row][column + 3] == 1: #right
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row + 1][column - 1] == 1 and board[row + 2][column - 2] == 1 and board[row + 3][column - 3] == 1: #left diagonal down
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row + 1][column + 1] == 1 and board[row + 2][column + 2] == 1 and board[row + 3][column + 3] == 1: #right diagonal down
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row - 1][column - 1] == 1 and board[row - 2][column - 2] == 1 and board[row - 3][column - 3] == 1: #left diagonal up
    gameover = True
elif turn % 2 == 1 and board[row][column] == 1 and board[row - 1][column + 1] == 1 and board[row - 2][column + 2] == 1 and board[row - 3][column + 3] == 1: #right diagonal up
    gameover = True

''' 

if __name__ == "__main__":
    app.run(debug=True)
