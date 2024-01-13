class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, connect4):
        while True:
            try:
                col = int(input("Enter your move (column 0-6): "))
                if connect4.is_valid_move(col):
                    return col
                else:
                    print("Invalid move. Column is full. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")