import chess
from alhoritms import Alhoritms
from evaluation import Evaluation

class Main:
    def __init__(self, board: chess.Board):
        self.board = board
    
    def computerMakesMove(self, maxDepth, color, method, alpha, beta):
        evaluation = Evaluation(self.board, self.board.turn)
        engine = Alhoritms(self.board, maxDepth, color, evaluation)

        if(method=="nm"):
            bestMove = engine.NegaMax(maxDepth)[1]

        elif(method=="ns"):
            bestMove = engine.NegaScout(maxDepth, alpha, beta)[1]

        elif(method == "pvs"):
            bestMove = engine.PVS(maxDepth, alpha, beta)[1]
            
        else:
            return
            
        print("Currect best move", bestMove)
        self.board.push(bestMove)
        return

    def humanMakesMove(self):
        print("You can move to: ", self.board.legal_moves)
        play = input("Choose your move: ")
        self.board.push_san(play)

    def start(self, method):
        aiColor = chess.BLACK
        print("New Chess Game Started")
        print("Your color - white")
        maxDepth = 3
        alpha = float("-inf")
        beta = float("inf")
        turn = chess.WHITE

        while (not self.board.is_checkmate()):

            print(self.board)
            
            if turn == chess.WHITE:
                print("\n\n\n")
                print("White to move")
                print("\n\n\n")
                self.humanMakesMove()
                turn = chess.BLACK
                continue
            
            if turn == chess.BLACK:
                print("\n\n\n")
                print("Black to move")
                print("\n\n\n")
                self.computerMakesMove(maxDepth, aiColor, method, alpha, beta)
                turn = chess.WHITE
                continue
        return

if __name__ == '__main__':
    game = Main(chess.Board())

    print("Available alhoritms: \nNegaMax\nNegaScout\nPVS")
    method = input("Choose alhoritm: (nm, ns, pvs)")

    while True:
        if method != "nm" and method != "ns" and method != "pvs":
            print("Input incorrect!")
            method = input("Choose alhoritm: (nm, ns, pvs)")
        else:
            break

    print("Successful: ", method)
    
    game.start(method)