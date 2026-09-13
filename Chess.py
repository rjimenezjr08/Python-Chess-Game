from tkinter import *
from PIL import Image, ImageTk

selected_piece = {
    "type": None,
    "name": None,
    "index": None,
    "color": None
}

previous_piece = {
    "type": None,
    "name": None,
    "index": None,
    "color": None
}

second_pn_ep = {
    "White": {"pawn1": False, "pawn2": False, "pawn3": False, "pawn4": False, "pawn5": False, "pawn6": False, "pawn7": False, "pawn8": False},
    "Black": {"pawn1b": False, "pawn2b": False, "pawn3b": False, "pawn4b": False, "pawn5b": False, "pawn6b": False, "pawn7b": False, "pawn8b": False}
}

first_move_cst= {
    "king1": True,
    "king1b": True,
    "rook1": True,
    "rook1b": True
}

global click_tracker
global first_move_pn
global pawn_selection
global rook_selection
global bishop_selection
global queen_selection
global knight_selection
global king_selectionf
global white_move

white_move = True

pawn_selection = False
rook_selection = False
queen_selection = False
knight_selection = False
king_selection = False

first_move_pn = [True, True, True, True, True, True, True, True]
first_move_pnb = [True, True, True, True, True, True, True, True]

click_tracker = False

pieces = {
    "pawn1": {"type": "pawn", "position": "a2", "color": "White"},
    "pawn2": {"type": "pawn", "position": "b2", "color": "White"},
    "pawn3": {"type": "pawn", "position": "c2", "color": "White"},
    "pawn4": {"type": "pawn", "position": "d2", "color": "White"},
    "pawn5": {"type": "pawn", "position": "e2", "color": "White"},
    "pawn6": {"type": "pawn", "position": "f2", "color": "White"},
    "pawn7": {"type": "pawn", "position": "g2", "color": "White"},
    "pawn8": {"type": "pawn", "position": "h2", "color": "White"},

    "rook1": {"type": "rook", "position": "a1", "color": "White"},
    "rook2": {"type": "rook", "position": "h1", "color": "White"},

    "knight1": {"type": "knight", "position": "b1", "color": "White"},
    "knight2": {"type": "knight", "position": "g1", "color": "White"},

    "bishop1": {"type": "bishop", "position": "c1", "color": "White"},
    "bishop2": {"type": "bishop", "position": "f1", "color": "White"},

    "queen1": {"type": "queen", "position": "d1", "color": "white"},
    "king1": {"type": "king", "position": "e1", "color": "White"},

    "pawn1b": {"type": "pawn", "position": "a7", "color": "Black"},
    "pawn2b": {"type": "pawn", "position": "b7", "color": "Black"},
    "pawn3b": {"type": "pawn", "position": "c7", "color": "Black"},
    "pawn4b": {"type": "pawn", "position": "d7", "color": "Black"},
    "pawn5b": {"type": "pawn", "position": "e7", "color": "Black"},
    "pawn6b": {"type": "pawn", "position": "f7", "color": "Black"},
    "pawn7b": {"type": "pawn", "position": "g7", "color": "Black"},
    "pawn8b": {"type": "pawn", "position": "h7", "color": "Black"},
    
    "rook1b": {"type": "rook", "position": "a8", "color": "Black"},
    "rook2b": {"type": "rook", "position": "h8", "color": "Black"},
    
    "knight1b": {"type": "knight", "position": "b8", "color": "Black"},
    "knight2b": {"type": "knight", "position": "g8", "color": "Black"},
    
    "bishop1b": {"type": "bishop", "position": "c8", "color": "Black"},
    "bishop2b": {"type": "bishop", "position": "f8", "color": "Black"},
    
    "queen1b": {"type": "queen", "position": "d8", "color": "Black"},
    "king1b": {"type": "king", "position": "e8", "color": "Black"}
}
root = Tk()

window_dimension = 640
box_length = 640/8

chessboard = Canvas(root, width=window_dimension, height=window_dimension)
chessboard.pack()

pil_pawn_raw = Image.open("white-pawn.png")
pil_pawn = pil_pawn_raw.resize((60,60))
tk_pawn = ImageTk.PhotoImage(pil_pawn)

pil_rook_raw = Image.open("white-rook.png")
pil_rook = pil_rook_raw.resize((60,60))
tk_rook = ImageTk.PhotoImage(pil_rook)

pil_knight_raw = Image.open("white-knight.png")
pil_knight = pil_knight_raw.resize((60,60))
tk_knight = ImageTk.PhotoImage(pil_knight)

pil_bishop_raw = Image.open("white-bishop.png")
pil_bishop = pil_bishop_raw.resize((60,60))
tk_bishop = ImageTk.PhotoImage(pil_bishop)

pil_queen_raw = Image.open("white-queen.png")
pil_queen = pil_queen_raw.resize((60,60))
tk_queen = ImageTk.PhotoImage(pil_queen)

pil_king_raw = Image.open("white-king.png")
pil_king = pil_king_raw.resize((60,60))
tk_king = ImageTk.PhotoImage(pil_king)

pil_pawnb_raw = Image.open("black-pawn.png")
pil_pawnb = pil_pawnb_raw.resize((60,60))
tk_pawnb = ImageTk.PhotoImage(pil_pawnb)

pil_rookb_raw = Image.open("black-rook.png")
pil_rookb = pil_rookb_raw.resize((60,60))
tk_rookb = ImageTk.PhotoImage(pil_rookb)

pil_knightb_raw = Image.open("black-knight.png")
pil_knightb = pil_knightb_raw.resize((60,60))
tk_knightb = ImageTk.PhotoImage(pil_knightb)

pil_bishopb_raw = Image.open("black-bishop.png")
pil_bishopb = pil_bishopb_raw.resize((60,60))
tk_bishopb = ImageTk.PhotoImage(pil_bishopb)

pil_queenb_raw = Image.open("black-queen.png")
pil_queenb = pil_queenb_raw.resize((60,60))
tk_queenb = ImageTk.PhotoImage(pil_queenb)

pil_kingb_raw = Image.open("black-king.png")
pil_kingb = pil_kingb_raw.resize((60,60))
tk_kingb = ImageTk.PhotoImage(pil_kingb)

box_centers = {}
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

bishop_selection = False
piece_name_bishop = None
selected_piece_bs = None

for row in range(8):
    for column in range(8):
        file_letter = letters[column]
        rank_number = 8 - row

        square_name = file_letter + str(rank_number)

        center_x = column * box_length + box_length / 2
        center_y = row * box_length + box_length / 2
        box_centers[square_name] = (int(center_x), int(center_y))


def white_box(pos_x, pos_y):
    rec_w = chessboard.create_rectangle(pos_x, pos_y, pos_x + box_length, pos_y + box_length, fill='#ffffff', tags="board")

def black_box(pos_x, pos_y):
    rec_w = chessboard.create_rectangle(pos_x, pos_y, pos_x + box_length, pos_y + box_length, fill='#000000', tags="board")

def square_occupied(square, pieces):
    for piece_name in pieces:
        if pieces[piece_name]["position"] == square:
            return True
    return False

def ep_check (selected_piece):
    agr_color = selected_piece["color"]
    agr_pos = pieces[selected_piece["name"]]["position"]
    side_check = []

    if letters.index(agr_pos[0]) + 1 <= 7:
        side_check.append(letters[letters.index(agr_pos[0]) + 1] + agr_pos[1])
    if letters.index(agr_pos[0]) - 1 >= 0:  
        side_check.append(letters[letters.index(agr_pos[0]) - 1] + agr_pos[1])
    for piece_name in pieces:
        if pieces[piece_name]["position"] in side_check and selected_piece["color"] != pieces[piece_name]["color"]:
            if piece_name.startswith("pawn") and selected_piece["type"] == "pawn":
                return True
            else:
                return False
def square_ep_name (selected_piece):
    agr_color = selected_piece["color"]
    agr_pos = pieces[selected_piece["name"]]["position"]
    side_check= []
    if letters.index(agr_pos[0]) + 1 <= 7:
        side_check.append(letters[letters.index(agr_pos[0]) + 1] + agr_pos[1])
    if letters.index(agr_pos[0]) - 1 >= 0:  
        side_check.append(letters[letters.index(agr_pos[0]) - 1] + agr_pos[1])

    for piece_name in pieces:
        if pieces[piece_name]["position"] in side_check and selected_piece["color"] != pieces[piece_name]["color"]:
            if piece_name.startswith("pawn"):
                return piece_name

def removing_piece(removing_piece):
    piece_type = removing_piece["type"]
    piece_index = removing_piece["index"]
    piece_color = removing_piece["color"].lower()
    piece_name = removing_piece["name"]

    canvas_id = piece_canvas[piece_color][piece_type][piece_index]

    chessboard.delete(canvas_id)
    del pieces[piece_name]

def reset_ep(color):
    for pawn in second_pn_ep[color]:
        second_pn_ep[color][pawn] = False


def valid_rook_move(current_position, move_position):
    valid_pos1 = []
    valid_pos2 = []
    valid_pos3 = []
    valid_pos4 = []
    col1 = letters.index(move_position[0])
    row1 = int(move_position[1])

    col = letters.index(current_position[0])
    row = int(current_position[1])
    if col1 - col > 0:
        
        for i in range(col+1,col1+1):
            valid_pos1.append(letters[i] + str(row))
            if square_occupied(letters[i] + str(row), pieces):
                break
            
            
    if col1-col < 0:

        for i in range(col-1,col1-1,-1):

            valid_pos2.append(letters[i] + str(row))
            if square_occupied(letters[i] + str(row), pieces):
                break

    if row1-row > 0:
        for i in range(row+1, row1+1):

            valid_pos3.append(letters[col]+str(i))
            if square_occupied(letters[col] + str(i), pieces):
                break
    if row1-row < 0:
        for i in range(row - 1, row1 - 1, -1):

            valid_pos4.append(letters[col]+str(i))
            if square_occupied(letters[col] + str(i), pieces):
                break
    if (move_position in valid_pos1 or move_position in valid_pos2 or move_position in valid_pos3 or move_position in valid_pos4):
        return True

    return False

def valid_pawn_move(selected_piece, current_pawn, move_coords_i):

    global first_move_pn
    valid_row_2 = None

    col_pawn = current_pawn[0]
    row_pawn = current_pawn[1]

    move_x = move_coords_i[0]
    move_yi = move_coords_i[1]

    valid_row = int(row_pawn) + 1

    if first_move_pn[int(selected_piece)] == True:
        valid_row_2 = int(row_pawn) + 2

    pn_name = "pawn" + str(int(selected_piece) + 1)
    if move_x == col_pawn and str(move_yi) == str(valid_row):
        
        second_pn_ep["White"][pn_name] = False
        return True
    elif str(move_yi) == str(valid_row_2):
        
        second_pn_ep["White"][pn_name] = True
        return True
    else:
        return False
    

def valid_pawnb_move(selected_piece, current_pawn, move_coords_i):

    global first_move_pnb
    valid_row_2 = None

    col_pawn = current_pawn[0]
    row_pawn = current_pawn[1]

    move_x = move_coords_i[0]
    move_yi = move_coords_i[1]

    valid_row = int(row_pawn) - 1

    if first_move_pnb[int(selected_piece)] == True:
        valid_row_2 = int(row_pawn) - 2

    pn_name = "pawn" + str(int(selected_piece) + 1) + "b"
        
    if move_x == col_pawn and str(move_yi) == str(valid_row):
        
        second_pn_ep["Black"][pn_name] = False
        return True
    elif str(move_yi) == str(valid_row_2):
        
        second_pn_ep["Black"][pn_name] = True
        return True
    else:
        return False

def valid_bishop_move(current_position, move_position):

    valid_bpos1 = []
    valid_bpos2 = []
    valid_bpos3 = []
    valid_bpos4 = []

    col_bs = current_position[0]
    row_bs = int(current_position[1])

    # up-right
    int_id = letters.index(col_bs) + 1

    for b in range(1, 8):

        if int_id > 7:
            break

        new_row = row_bs + b

        if new_row > 8:
            break

        col = letters[int_id]
        square = col + str(new_row)

        valid_bpos1.append(square)

        if square_occupied(square, pieces):
            break

        int_id += 1


    # up-left
    int_id = letters.index(col_bs) - 1

    for b in range(1, 8):

        if int_id < 0:
            break

        new_row = row_bs + b

        if new_row > 8:
            break

        col = letters[int_id]
        square = col + str(new_row)

        valid_bpos2.append(square)

        if square_occupied(square, pieces):
            break

        int_id -= 1


    # down-right
    int_id = letters.index(col_bs) + 1

    for b in range(1, 8):

        if int_id > 7:
            break

        new_row = row_bs - b

        if new_row < 1:
            break

        col = letters[int_id]
        square = col + str(new_row)

        valid_bpos3.append(square)

        if square_occupied(square, pieces):
            break

        int_id += 1


    # down-left
    int_id = letters.index(col_bs) - 1

    for b in range(1, 8):

        if int_id < 0:
            break

        new_row = row_bs - b

        if new_row < 1:
            break

        col = letters[int_id]
        square = col + str(new_row)

        valid_bpos4.append(square)

        if square_occupied(square, pieces):
            break

        int_id -= 1


    if (
        move_position in valid_bpos1
        or move_position in valid_bpos2
        or move_position in valid_bpos3
        or move_position in valid_bpos4
    ):
        return True

    return False

def valid_queen_move(current_position, move_position):

    return (
        valid_rook_move(current_position, move_position)
        or
        valid_bishop_move(current_position, move_position)
    )

def valid_knight_move(current_position, move_position):
    col_kn = current_position[0]
    row_kn = current_position[1] 
    
    x_add = [2,2,1,1,-2,-2,-1,-1]
    y_add = [1,-1,2,-2,1,-1,2,-2]
    valid_x = [0,0,0,0,0,0,0,0]
    valid_y = [0,0,0,0,0,0,0,0]
    valid_knmove = [0,0,0,0,0,0,0,0]

    for kn in range(8):
       
        if letters.index(col_kn) + x_add[kn] > 7 or letters.index(col_kn) + x_add[kn] < 0:
            continue
    
        else: valid_x[kn] = letters[letters.index(col_kn) + x_add[kn]]
                    
    for kn2 in range(8):
                       
        if int(row_kn) + y_add[kn2] > 8 or int(row_kn) + y_add[kn2] < 1:
            continue
        else: valid_y[kn2] = int(row_kn) + y_add[kn2]
    for kn3 in range(8):
        if valid_x[kn3] == 0 or valid_y[kn3] == 0:
            continue
        else: valid_knmove[kn3] = str(valid_x[kn3]) + str(valid_y[kn3])
    
    if move_position in valid_knmove:
        return True
            
    return False

def valid_king_move(current_position, move_position):
    col_ki = current_position[0]
    row_ki = current_position[1]
                    
    valid_ki = []
    add_col = [0,0,0,-1,-1,-1,1,1,1]
    add_row = [-1,0,1,-1,0,1,-1,0,1]
                                        
    for ki1 in range(9):
        if letters.index(col_ki) + add_col[ki1] > 7 or letters.index(col_ki) + add_col[ki1] < 0:
            continue
        if int(row_ki) + int(add_row[ki1]) > 8 or int(row_ki) + int(add_row[ki1]) < 1:
            continue
        c = letters[letters.index(col_ki) + add_col[ki1]]
        r = int(row_ki) + int(add_row[ki1])
        valid_ki.append(str(c) + str(r))
    if move_position in valid_ki:
        return True
    return False


piece_name_rook = None


def click(event):

    global click_tracker
    global first_move_pn
    global pawn_selection
    global rook_selection
    global bishop_selection
    global queen_selection
    global knight_selection
    global king_selection
    global white_move


    previous_piece["type"] = selected_piece["type"]
    previous_piece["name"] = selected_piece["name"]
    previous_piece["index"] = selected_piece["index"]
    previous_piece["color"] = selected_piece["color"]
    
    
    piece_id = chessboard.find_withtag('current')

    if piece_id:
        tags = chessboard.gettags(piece_id)
        piece_name = tags[0]

        if piece_name != "board":

            if piece_name.startswith("pawn"):
                selected_piece["type"] = "pawn"

            elif piece_name.startswith("rook"):
                selected_piece["type"] = "rook"

            elif piece_name.startswith("bishop"):
                selected_piece["type"] = "bishop"

            elif piece_name.startswith("queen"):
                selected_piece["type"] = "queen"

            elif piece_name.startswith("knight"):
                selected_piece["type"] = "knight"

            elif piece_name.startswith("king"):
                selected_piece["type"] = "king"


            selected_piece["name"] = piece_name

            piece_type = selected_piece["type"]

            if piece_name.endswith("b"):
                selected_piece["color"] = "Black"
                piece_number = piece_name.replace(piece_type, "").replace("b", "")

            
            else:
                selected_piece["color"] = "White"
                piece_number = piece_name.replace(piece_type, "")
            selected_piece["index"] = int(piece_number) - 1

            click_tracker = True

            if previous_piece["color"] != selected_piece["color"]:
                move_coords = box_centers[pieces[selected_piece["name"]]["position"]]
                move_coords_i = pieces[selected_piece["name"]]["position"]

                agressor = previous_piece["color"]
                victim = selected_piece["color"]
                if previous_piece["type"] == "pawn":

                    if white_move == True and agressor == "White":

                        current_pawn = pieces[previous_piece["name"]]["position"]

                        if valid_pawn_move(selected_piece["index"], current_pawn, move_coords_i):
                        
                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(pawns_2[previous_piece["index"]], move_coords)
                            removing_piece(selected_piece)
                            pawn_selection = False
                            click_tracker = False
                
                            first_move_pn[previous_piece["index"]] = False
                            white_move = False
                            reset_ep("White")
                    
                    elif white_move == False and agressor == "Black":
                        current_pawn = pieces[previous_piece["name"]]["position"]

                        if valid_pawnb_move(selected_piece["index"], current_pawn, move_coords_i):
                        
                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(pawns_2b[previous_piece["index"]], move_coords)
                            removing_piece(selected_piece)
                            pawn_selection = False
                            click_tracker = False
                
                            first_move_pnb[previous_piece["index"]] = False
                            white_move = True
                            reset_ep("Black")
                    
                    

                elif previous_piece["type"] == "rook":

                    if white_move == True and agressor == "White":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_rook_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                rooks_2[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)

                            click_tracker = False
                            white_move = False
                            reset_ep("White")


                    elif white_move == False and agressor == "Black":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_rook_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                rooks_2b[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)

                            click_tracker = False
                            white_move = True
                            reset_ep("Black")


                elif previous_piece["type"] == "bishop":

                    if white_move == True and agressor == "White":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_bishop_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                bishops_2[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = False
                            reset_ep("White")


                    elif white_move == False and agressor == "Black":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_bishop_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                bishops_2b[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = True
                            reset_ep("Black")


                elif previous_piece["type"] == "queen":

                    if white_move == True and agressor == "White":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_queen_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                queen_2,
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = False
                            reset_ep("White")


                    elif white_move == False and agressor == "Black":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_queen_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                            queen_2b,
                            move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = True
                            reset_ep("Black")


                elif previous_piece["type"] == "knight":

                    if white_move == True and agressor == "White":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_knight_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                knights_2[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = False
                            reset_ep("White")


                    elif white_move == False and agressor == "Black":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_knight_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                knights_2b[previous_piece["index"]],
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = True
                            reset_ep("Black")


                elif previous_piece["type"] == "king":

                    if white_move == True and agressor == "White":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_king_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                king_2,
                                move_coords
                            )
                            removing_piece(selected_piece)

                            click_tracker = False
                            white_move = False
                            reset_ep("White")


                    elif white_move == False and agressor == "Black":

                        current_position = pieces[previous_piece["name"]]["position"]

                        if valid_king_move(current_position, move_coords_i):

                            pieces[previous_piece["name"]]["position"] = move_coords_i

                            chessboard.coords(
                                king_2b,
                                move_coords
                            )
                            removing_piece(selected_piece)
                            click_tracker = False
                            white_move = True
                            reset_ep("Black")
                    
            
        elif piece_name == "board" and click_tracker == True:

            move_xi = int(event.x // box_length)
            move_yi = 8 - int(event.y // box_length)

            move_x = letters[move_xi]
            move_coords_i = move_x + str(move_yi)
            move_coords = box_centers[move_coords_i]

            if selected_piece["type"] == "pawn":

                if white_move == True and selected_piece["color"] == "White":

                    current_pawn = pieces[selected_piece["name"]]["position"]

                    if valid_pawn_move(
                        selected_piece["index"],
                        current_pawn,
                        move_coords_i
                    ):

                        pawn_name = selected_piece["name"]

                        moved_two = second_pn_ep["White"][pawn_name]

                        reset_ep("White")

                        second_pn_ep["White"][pawn_name] = moved_two

                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            pawns_2[selected_piece["index"]],
                            move_coords
                        )

                        first_move_pn[selected_piece["index"]] = False
                        click_tracker = False
                        white_move = False                        

                    elif ep_check(selected_piece):
                        
                        victim_piece_nm = square_ep_name(selected_piece)

                        if second_pn_ep["Black"][victim_piece_nm]:
                            victim_pos = pieces[victim_piece_nm]["position"]
                            ep_dest = victim_pos[0] + str(int(victim_pos[1]) + 1)
                            
                            if ep_dest == move_coords_i:
                                reset_ep("White")
                                victim_id = int(victim_piece_nm.replace("pawn", "").replace("b", "")) - 1
                                chessboard.coords(pawns_2[selected_piece["index"]], move_coords)
                                chessboard.delete(pawns_2b[victim_id])
                                del pieces[victim_piece_nm]
                                pieces[selected_piece["name"]]["position"] = move_coords_i
                                click_tracker = False
                                white_move = False
                
                elif white_move == False and selected_piece["color"] == "Black":

                    current_pawn = pieces[selected_piece["name"]]["position"]

                    if valid_pawnb_move(
                        selected_piece["index"],
                        current_pawn,
                        move_coords_i
                    ):

                        pawn_name = selected_piece["name"]

                        moved_two = second_pn_ep["Black"][pawn_name]

                        reset_ep("Black")

                        second_pn_ep["Black"][pawn_name] = moved_two

                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            pawns_2b[selected_piece["index"]],
                            move_coords
                        )

                        first_move_pnb[selected_piece["index"]] = False
                        click_tracker = False
                        white_move = True

                    elif ep_check(selected_piece):
                        
                        victim_piece_nm = square_ep_name(selected_piece)

                        if second_pn_ep["White"][victim_piece_nm]:
                            victim_pos = pieces[victim_piece_nm]["position"]
                            ep_dest = victim_pos[0] + str(int(victim_pos[1]) - 1)
                            if ep_dest == move_coords_i:
                                reset_ep("Black")
                                victim_id = int(victim_piece_nm.replace("pawn", "")) - 1
                                chessboard.coords(pawns_2b[selected_piece["index"]], move_coords)
                                chessboard.delete(pawns_2[victim_id])
                                del pieces[victim_piece_nm]
                                pieces[selected_piece["name"]]["position"] = move_coords_i
                                click_tracker = False
                                white_move = True

                
                

            elif selected_piece["type"] == "rook":

                if white_move == True and selected_piece["color"] == "White":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_rook_move(current_position, move_coords_i):
                        reset_ep("White")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            rooks_2[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = False


                elif white_move == False and selected_piece["color"] == "Black":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_rook_move(current_position, move_coords_i):
                        reset_ep("Black")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            rooks_2b[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = True


            elif selected_piece["type"] == "bishop":

                if white_move == True and selected_piece["color"] == "White":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_bishop_move(current_position, move_coords_i):
                        reset_ep("White")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            bishops_2[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = False


                elif white_move == False and selected_piece["color"] == "Black":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_bishop_move(current_position, move_coords_i):
                        reset_ep("Black")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            bishops_2b[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = True


            elif selected_piece["type"] == "queen":

                if white_move == True and selected_piece["color"] == "White":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_queen_move(current_position, move_coords_i):
                        reset_ep("White")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            queen_2[0],
                            move_coords
                        )

                        click_tracker = False
                        white_move = False


                elif white_move == False and selected_piece["color"] == "Black":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_queen_move(current_position, move_coords_i):
                        reset_ep("Black")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                        queen_2b,
                        move_coords
                        )

                        click_tracker = False
                        white_move = True


            elif selected_piece["type"] == "knight":

                if white_move == True and selected_piece["color"] == "White":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_knight_move(current_position, move_coords_i):
                        reset_ep("White")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            knights_2[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = False


                elif white_move == False and selected_piece["color"] == "Black":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_knight_move(current_position, move_coords_i):
                        reset_ep("Black")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            knights_2b[selected_piece["index"]],
                            move_coords
                        )

                        click_tracker = False
                        white_move = True


            elif selected_piece["type"] == "king":

                if white_move == True and selected_piece["color"] == "White":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_king_move(current_position, move_coords_i):
                        reset_ep("White")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            king_2[0],
                            move_coords
                        )

                        click_tracker = False
                        white_move = False


                elif white_move == False and selected_piece["color"] == "Black":
                    

                    current_position = pieces[selected_piece["name"]]["position"]

                    if valid_king_move(current_position, move_coords_i):
                        reset_ep("Black")
                        pieces[selected_piece["name"]]["position"] = move_coords_i

                        chessboard.coords(
                            king_2b,
                            move_coords
                        )

                        click_tracker = False
                        white_move = True


y = 0

for row in range(0,8):

    if row % 2 == 0:
        x0_w = 0

        for column in range(1,5):
            
            white_box(x0_w, y)
            x0_w = x0_w + 2*box_length

        x0_b = box_length

        for column in range(1,5):
            
            black_box(x0_b, y)
            x0_b = x0_b + 2*box_length

    if row % 2 != 0:
        x0_w = 0

        for column in range(1,5):
            
            black_box(x0_w,y)
            x0_w = x0_w + 2*box_length

        x0_b = box_length
        for column in range(1,5):

            white_box(x0_b,y)
            x0_b = x0_b + 2*box_length

    y = y + box_length

pawns = {}
pawns_2 = [0,0,0,0,0,0,0,0]

rooks = {"rook1": "a1", "rook2": "h1"}
rooks_2 = [0,0]

bishops = {"bishop1": "c1", "bishop2": "f1"}
bishops_2 = [0,0]

knights = {"knight1": "b1", "knight2": "g1"}
knights_2 = [0,0]

pawns_2b = []
rooks_2b = []
bishops_2b = []
knights_2b = []

for column in range(8):
    pawn_introw = 2
    pawn_intletter = letters[column]

    pawn_intsquare = pawn_intletter + str(pawn_introw)
    pawn_x, pawn_y = box_centers[pawn_intsquare]

    pawn_name = "pawn" + str(column + 1)
    pawns[pawn_name] = (pawn_intsquare)

    pawns_2[column] = chessboard.create_image(pawn_x, pawn_y, image=tk_pawn, tags=(pawn_name, "pieces"))

for columnb in range(8):
    id = columnb + 1
    pawn_nm = "pawn" + str(id) + "b"
    pawn_x, pawn_y = box_centers[pieces[pawn_nm]["position"]]
    pawns_2b.append(chessboard.create_image(pawn_x, pawn_y, image =tk_pawnb, tags = ("pawn" + str(id) + "b", "pieces")))

for columnb in range(2):
    id = columnb + 1
    rook_nm = "rook" + str(id) + "b"
    rook_x, rook_y = box_centers[pieces[rook_nm]["position"]]
    rooks_2b.append(chessboard.create_image(rook_x, rook_y, image =tk_rookb, tags = ("rook" + str(id) + "b", "pieces")))
for columnb in range(2):
    id = columnb + 1
    bishop_nm = "bishop" + str(id) + "b"
    bishop_x, bishop_y = box_centers[pieces[bishop_nm]["position"]]
    bishops_2b.append(chessboard.create_image(bishop_x, bishop_y, image =tk_bishopb, tags = ("bishop" + str(id) + "b", "pieces")))
for columnb in range(2):
    id = columnb + 1
    knight_nm = "knight" + str(id) + "b"
    knight_x, knight_y = box_centers[pieces[knight_nm]["position"]]
    knights_2b.append(chessboard.create_image(knight_x, knight_y, image =tk_knightb, tags = ("knight" + str(id) + "b", "pieces")))

king_2b = [0]
queen_2b = [0]

king_x, king_y = box_centers[pieces["king1b"]["position"]]
king_2b[0] = chessboard.create_image(king_x, king_y, image =tk_kingb, tags = ("king1b", "pieces"))


queen_x, queen_y = box_centers[pieces["queen1b"]["position"]]
queen_2b[0] = chessboard.create_image(queen_x, queen_y, image =tk_queenb, tags = ("queen1b", "pieces"))

rook1_x, rook1_y = box_centers[rooks["rook1"]]
rooks_2[0] = chessboard.create_image(rook1_x, rook1_y, image=tk_rook, tags=("rook1", "pieces"))

rook2_x, rook2_y = box_centers[rooks["rook2"]]
rooks_2[1] = chessboard.create_image(rook2_x, rook2_y, image=tk_rook, tags=("rook2", "pieces"))

bishop1_x, bishop1_y = box_centers[bishops["bishop1"]]
bishops_2[0] = chessboard.create_image(bishop1_x, bishop1_y, image=tk_bishop, tags=("bishop1", "pieces"))

bishop2_x, bishop2_y = box_centers[bishops["bishop2"]]
bishops_2[1] = chessboard.create_image(bishop2_x, bishop2_y, image=tk_bishop, tags=("bishop2", "pieces"))

knight1_x, knight1_y = box_centers[knights["knight1"]]
knights_2[0] = chessboard.create_image(knight1_x, knight1_y, image=tk_knight, tags=("knight1", "pieces"))

knight2_x, knight2_y = box_centers[knights["knight2"]]
knights_2[1] = chessboard.create_image(knight2_x, knight2_y, image=tk_knight, tags=("knight2", "pieces"))

queen = {"queen1": "d1"}
queen_2 = [0]

queen_x, queen_y = box_centers[queen["queen1"]]
queen_2[0] = chessboard.create_image(queen_x, queen_y, image=tk_queen, tags=("queen1", "pieces"))


king = {"king1": "e1"}
king_2 = [0]

king_x, king_y = box_centers[king["king1"]]
king_2[0] = chessboard.create_image(king_x, king_y, image=tk_king, tags=("king1", "pieces"))

piece_canvas = {
    "white": {
        "pawn": pawns_2,
        "rook": rooks_2,
        "bishop": bishops_2,
        "knight": knights_2,
        "queen": queen_2,
        "king": king_2
    },
    "black": {
        "pawn": pawns_2b,
        "rook": rooks_2b,
        "bishop": bishops_2b,
        "knight": knights_2b,
        "queen": queen_2b,
        "king": king_2b
    }
}


chessboard.bind("<Button-1>", click)

root.mainloop()