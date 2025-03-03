import random


class Morpion:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

    def display_board(self):
        print("-------------" + "-----" * (self.size - 3))
        for row in self.board:
            print("|", " | ".join(row), "|")
            print("-------------" + "-----" * (self.size - 3))

    def convert_move_to_indices(self, move):
        row = (move - 1) // self.size
        col = (move - 1) % self.size
        return row, col

    def play_move(self):
        while True:
            try:
                move = int(input(f"Entrer le numéro de la case à cocher (1-{self.size * self.size}) : "))
            except ValueError:
                print("Veuillez entrer un nombre entier.")
                continue

            if move < 1 or move > self.size * self.size:
                print(f"Mouvement invalide, essayez un nombre entre 1 et {self.size * self.size}.")
                continue

            row, col = self.convert_move_to_indices(move)

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                break
            else:
                print("La case est déjà prise. Essayez à nouveau.")

    def computer_move(self):
        while True:
            move = random.randint(1, self.size * self.size)
            row, col = self.convert_move_to_indices(move)
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player2
                break

    def check_win(self):
        for row in self.board:
            if all(cell == row[0] and cell != ' ' for cell in row):
                return True

        for col in range(self.size):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != ' ' for row in range(self.size)):
                return True

        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != ' ' for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] and self.board[i][self.size - 1 - i] != ' ' for i in range(self.size)):
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


while True:
    try:
        size = int(input("Entrez la taille du tableau (n pour un tableau n x n) : "))
        if size < 3:
            print("La taille doit être supérieure ou égale à 3.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre entier.")

morpion = Morpion(size)
morpion.display_board()

while True:
    morpion.play_move()
    morpion.display_board()

    if morpion.check_win():
        print("Félicitations ! Vous avez gagné !")
        break

    if morpion.check_draw():
        print("Match nul !")
        break

    morpion.computer_move()
    morpion.display_board()

    if morpion.check_win():
        print("L'ordinateur a gagné !")
        break

    if morpion.check_draw():
        print("Match nul !")
        break
