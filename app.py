from flask import Flask, render_template, request, jsonify
from connect4 import Connect4
app = Flask(__name__)

game = Connect4()

@app.route("/", methods=['GET', 'POST'])
def index():
    game.initalize_board();
    return render_template('board.html')

@app.route("/_game_status", methods=['GET', 'POST'])
def game_status():

    game_on = True
    
    if (game.has_winner):
        game_on = False
        
    return jsonify(game_status = str(game_on))

@app.route("/_restart_game", methods=['GET', 'POST'])
def restart_game():
    
    game.initalize_board();
    
    return render_template('board.html')


@app.route("/_player_move", methods=['GET', 'POST'])
def player_move():

    column = request.args.get('column',0, type=int)
    row = game.place_piece(column)
    print("Placed a piece at column: " + str(column) + " row: " + str(row))

    if (row == -1):
        return jsonify(row=-1)

    player_color = game.player_color
    game.update_player_color()

    return jsonify(row=row, color = player_color, win=str(game.has_winner), tie=str(game.tie))

if __name__ == "__main__":
    app.run(debug=True)
