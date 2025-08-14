from random import choice

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            movimiento = int(input("Ingrese su movimiento (1-9): "))
            for fila in range(3):
                for col in range(3):
                    if board[fila][col] == movimiento:
                        board[fila][col] = "O"   
                        return   
            print("Movimiento inválido, intenta otra vez.")
        except ValueError:
            print("Por favor ingrese un número válido.")


def make_list_of_free_fields(board):
    libres = []
    for fila in range(3):
        for col in range(3):
            if board[fila][col] not in ["X", "O"]:
                libres.append((fila, col))
    return libres


def victory_for(board, sign):
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


def draw_move(board):
    libres = make_list_of_free_fields(board)
    for fila, col in libres:
        copia = [row[:] for row in board]
        copia[fila][col] = "X"
        if victory_for(copia, "X"):
            board[fila][col] = "X"
            return
    for fila, col in libres:
        copia = [row[:] for row in board]
        copia[fila][col] = "O"
        if victory_for(copia, "O"):
            board[fila][col] = "X"
            return
    if (1, 1) in libres:
        board[1][1] = "X"
        return
    esquinas = [(0,0), (0,2), (2,0), (2,2)]
    esquinas_libres = []
    for pos in esquinas:
        if pos in libres:
            esquinas_libres.append(pos)
    if esquinas_libres:
        fila, col = choice(esquinas_libres)
        board[fila][col] = "X"
        return
    fila, col = choice(libres)
    board[fila][col] = "X"


board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("¡Ganaste!")
        break
    if not make_list_of_free_fields(board):
        print("¡Empate!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("La máquina ganó.")
        break
    if not make_list_of_free_fields(board):
        print("¡Empate!")
        break
