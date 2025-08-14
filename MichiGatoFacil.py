 
def display_board(board):
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("| ",board[1][0],"   |  ",board[1][1],"  |  ",board[1][2],"  |")
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


from random import randrange

def draw_move(board):
    while True:
        movimiento = randrange(1, 10)   
        for fila in range(3):
            for col in range(3):
                if board[fila][col] == movimiento:
                    board[fila][col] = "X"
                    return   

            

board = [[1,2,3],[4,"X",6],[7,8,9]]
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
 


 
