import chess
from evaluation import Evaluation

class Alhoritms:
    def __init__(self, board: chess.Board, maxDepth, color, evaluation):
        self.board = board
        self.maxDepth = maxDepth
        self.color = color
        self.evaluation = evaluation

    def NegaMax(self, depth):
        bestMove = chess.Move.null()
        bestScore = float('-inf')
        if (depth == 0):
            return (self.evaluation.evaluate(), None)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1*(self.NegaMax(depth - 1)[0])
            if score > bestScore:
                bestScore = score
                bestMove = move
            self.board.pop()
        return bestScore, bestMove

    def NegaScout(self, depth, alpha, beta):
        return

    def PVS(self, depth, alpha, beta):
        return

    def getPVSscore(self, depth, alpha, beta):
        return
