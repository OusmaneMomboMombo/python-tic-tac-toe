class Morpion:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

    def display_board(self):
        print("-------------")
        for i in range(3):
            print("|", self.board[i][0], "|", self.board[i][1], "|", self.board[i][2], "|")
            print("-------------")

    def convert_move_to_indices(self, move):
        if move == 1:
            row, col = 0, 0
        elif move == 2:
            row, col = 0, 1
        elif move == 3:
            row, col = 0, 2
        elif move == 4:
            row, col = 1, 0
        elif move == 5:
            row, col = 1, 1
        elif move == 6:
            row, col = 1, 2
        elif move == 7:
            row, col = 2, 0
        elif move == 8:
            row, col = 2, 1
        elif move == 9:
            row, col = 2, 2
        return row, col

    def play_move(self):
        while True:
            try:
                move = int(input("Entrer le numéro de la case à cocher (1-9) : "))
            except ValueError:
                print("Veuillez entrer un nombre entier.")
                continue

            if move < 1 or move > 9:
                print("Mouvement invalide, essayez un nombre entre 1 et 9.")
                continue

            row, col = self.convert_move_to_indices(move)

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                break
            else:
                print("La case est déjà prise. Essayez à nouveau.")

        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


morpion = Morpion()
morpion.display_board()

while True:
    morpion.play_move()
    morpion.display_board()

    if morpion.check_win():
        print(f"Félicitations ! {morpion.player2 if morpion.current_player == morpion.player1 else morpion.player1} a gagné !")
        break

    if morpion.check_draw():
        print("Match nul !")
        break
