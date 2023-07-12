import random


class Game:
    def __init__(self):
        self.board = [" "] * 9
        self.turn = True  # True for player 1, False for player 2
        self.possibleWins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def makePlay(self, player):
        playIndex = int(input("Please choose an index (1-9) "))

        while playIndex > 9 or playIndex < 0:
            playIndex = int(input("Sorry you chose an invalid number. Choose a number between 1 and 9. "))

        while self.board[playIndex - 1] == "X" or self.board[playIndex - 1] == "O":
            playIndex = int(input("Sorry, that spot is taken. Choose another spot. "))

        character = "X" if player else "O"

        self.board[playIndex - 1] = character
        self.printBoard()
        winner = self.checkGameBoardForWinner()
        if winner == "Player1" or winner == "Player2":
            print(f"\nCongrats {winner}! You won.")
            return True
        else:
            return False

    def makeAiPlay(self, char):
        print("AiBot now playing.")
        num = -1
        attempts = 0
        while num == -1:
            if attempts >= 100:
                print("AiBot can't make a play!")
                break
            num = random.randint(0, 8)
            if self.board[num] == "X" or self.board[num] == "O":
                num = -1
            attempts += 1
        if num > -1:
            self.board[num] = char
            self.printBoard()
            winner = self.checkGameBoardForWinner()
            if winner == "AiBot":
                print("\nAiBot won the game! Sorry Player1...")
            elif winner == "Player1" or winner == "Player2":
                print(f"\nCongrats {winner}! You won.")
                return True
            else:
                return False

    def checkGameBoardForWinner(self):
        chars = ["X", "O"]
        for route in self.possibleWins:
            for char in chars:
                if self.board[route[0]] == char and self.board[route[1]] == char and self.board[route[2]] == char:
                    if char == "X":
                        return "Player1"
                    elif char == "O":
                        return "Player2"
        return "None"

    def printBoard(self):
        print(
            f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} \n ---------- \n {self.board[3]} | {self.board[4]} | {self.board[5]}  \n "
            f"---------- \n {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def announceTurn(self):
        if self.turn:
            print("It is player 1's turn.")
        else:
            print("It is player 2's turn.")

    def playGame(self):
        print("Welcome to Tic-Tac-Toe!")
        self.printBoard()

        while True:
            self.announceTurn()

            if self.turn:
                if self.makePlay(self.turn):
                    break
            else:
                if self.makeAiPlay("O"):
                    break

            # Switch turns
            self.turn = not self.turn

        print("Game over!")

if __name__ == '__main__':
    game = Game()
    game.playGame()
