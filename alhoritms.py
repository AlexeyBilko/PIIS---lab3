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
        bestMove = None
        bestScore = float('-inf')
        if (depth == 0):
            return (self.evaluation.evaluate(), None)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1 * (self.getMaxScore(depth-1, alpha, beta))
            self.board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = move
        return (bestScore, bestMove)



    def getMaxScore(self, depth, alpha, beta):
            if (depth == 0):
                return self.evaluation.evaluate()
            a = alpha
            b = beta
            i = 1
            for move in self.board.legal_moves:
                self.board.push(move)
                t = -1*(self.NegaScout(depth - 1, -b, -alpha)[0])
                self.board.pop()
                if t > alpha and t < beta and i > 1 and depth < self.maxDepth - 1:
                    a = -1*(self.NegaScout(depth - 1, -beta, -t)[0])
                a = max(a, t)
                if a >= beta:
                    return a
                b = a + 1
                i = i + 1
                
            return a



    def PVS(self, depth, alpha, beta):
        bestMove = chess.Move.null()
        bestScore = float('-inf')
        if (depth == 0):
            return (self.evaluation.evaluate(), None)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1*(self.getPVSscore(depth-1, alpha, beta))
            self.board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = move
        return (bestScore, bestMove)



    def getPVSscore(self, depth, alpha, beta):
        if depth == 0:
            return self.evaluation.evaluate()
        bSearchPv = True
        for move in self.board.legal_moves:
            self.board.push(move)
            if bSearchPv:
                score = -1*(self.getPVSscore(depth - 1, -beta, -alpha))
            else:
                score = -1*(self.getPVSscore(depth - 1, -alpha-1, -alpha))
                if score > alpha and score < beta:
                    score = -1*(self.getPVSscore(depth - 1, -beta, -alpha))
            self.board.pop()
            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
                bSearchPv = False
        return alpha