import copy
import pprint

# currently working on logic
# example
# piece = {"name": "pawn", "location": "A2", "team": "white"}


def piece(name, team):
    return {"name": name, "team": team, "moved": 0}


def make_board():
    board = {
        "A1": piece("Rook", "White"),
        "B1": piece("Knight", "White"),
        "C1": piece("Bishop", "White"),
        "D1": piece("Queen", "White"),
        "E1": piece("King", "White"),
        "F1": piece("Bishop", "White"),
        "G1": piece("Knight", "White"),
        "H1": piece("Rook", "White"),
        "A8": piece("Rook", "Black"),
        "B8": piece("Knight", "Black"),
        "C8": piece("Bishop", "Black"),
        "D8": piece("Queen", "Black"),
        "E8": piece("King", "Black"),
        "F8": piece("Bishop", "Black"),
        "G8": piece("Knight", "Black"),
        "H8": piece("Rook", "Black"),
    }
    for i in range(8):
        board[str(chr(ord("A") + i)) + "2"] = piece("Pawn", "White")
    for i in range(8):
        board[str(chr(ord("A") + i)) + "7"] = piece("Pawn", "Black")
    for y in range(4):
        for i in range(8):
            board[str(chr(ord("A") + i)) + str(y + 3)] = 0
    return board


def print_board():
    def return_appropriate(location):
        piece = board.get(location)
        if piece != 0:
            return piece.get("name") + "-" + piece.get("team")
        else:
            return "0"

    board_print = ""
    for i in range(8):
        line = ""
        for j in range(8):
            location = str(chr(ord("A") + j)) + str(i + 1)
            line += return_appropriate(location) + " "
        board_print += line + "\n"

    print(board_print)


def move_piece(current_location, desired_location):
    if board[desired_location].get("team") == board[current_location].get("team"):
        print("no") # make fail or something
    else:
        new = copy.copy(board.get(current_location))
        new["moved"] += 1
        board[desired_location] = new
        board[current_location] = 0

if __name__ == "__main__":
    # test = copy.copy(piece)
    # print(test)
    # print("\n")
    # pprint.pprint(board)
    board = make_board()
    print_board()
    while True:
        move_piece(
            input("What is the location of the piece you want to move?: "),
            input("Where do you want to move it to?: "),
        )
        print_board()
