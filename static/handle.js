

$(document).ready(function() {
	var game_on = true;
	$.getJSON($SCRIPT_ROOT + '/_game_status', {}, function(data) {
		game_on = data.game_status;
	});

				
	$("#gameresult").hide();
	
	
	$('td').click(function(){
		var col = $(this).parent().children().index($(this));
		var row = $(this).parent().parent().children().index($(this).parent());
	  
		if (game_on){
			console.log('Column: ' + col);
			
			$.getJSON($SCRIPT_ROOT + '/_player_move', {
				column: col
			}, function(data) {
				
				if (data.row >= 0){		
					var t = document.getElementById('gamegrid');
					t.rows[data.row+1].cells[col].innerHTML = data.color;

					if (data.color == "1"){
						t.rows[data.row+1].cells[col].setAttribute("style", "background:#F47983;");
						$("#whowin").html("<strong>Red Win!!</strong>")
					}else{
						t.rows[data.row+1].cells[col].setAttribute("style", "background:#f4ce42;");
						$("#whowin").html("<strong>Yellow Win!!</strong>")
					}

					if (data.win == "True"){
						game_on = false;
						$("#gameresult").show();
					}
				}
			});
			return false;
		}else{
			console.log("Game not on")
		}

	});
});
