import chess

class Evaluation:
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def balance(self):
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        
        pawns = chess.popcount(white & self.board.pawns) \
                - chess.popcount(black & self.board.pawns)
                  
        bishops = chess.popcount(white & self.board.bishops) \
                  - chess.popcount(black & self.board.bishops)
                  
        rooks = chess.popcount(white & self.board.rooks) \
                - chess.popcount(black & self.board.rooks)

        knights = chess.popcount(white & self.board.knights) \
                  - chess.popcount(black & self.board.knights)
        
        kings = chess.popcount(white & self.board.kings) \
                - chess.popcount(black & self.board.kings)

        queens = chess.popcount(white & self.board.queens) \
                 - chess.popcount(black & self.board.queens)

        return pawns * 1 + knights * 3 + bishops * 3 + rooks * 5 + queens * 9 + kings * 100
    
    def evaluate(self):
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        score = self.balance() * (white - black)

        if (self.board.turn == self.color):
            return score

        return -score