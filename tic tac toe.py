import random

class TicTacToe:
    def _init_(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.player = 'X'
        self.winner = None

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def is_winner(self, mark):
        for i in range(3):
            if self.board[i][0] == mark and self.board[i][1] == mark and self.board[i][2] == mark:
                return True
            if self.board[0][i] == mark and self.board[1][i] == mark and self.board[2][i] == mark:
                return True
        if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark:
            return True
        if self.board[2][0] == mark and self.board[1][1] == mark and self.board[0][2] == mark:
            return True
        return False

    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def make_move(self, row, col):
        self.board[row][col] = self.player
        if self.is_winner(self.player):
            self.winner = self.player
        self.player = 'O' if self.player == 'X' else 'X'

    def get_score(self):
        if self.winner == 'X':
            return 1
        elif self.winner == 'O':
            return -1
        elif self.is_full():
            return 0
        else:
            return None

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.winner is not None:
            return self.get_score()
        if maximizing_player:
            best_score = -float('inf')
            for row, col in self.get_available_moves():
                new_board = self.copy()
                new_board.make_move(row, col)
                score = new_board.minimax(depth - 1, alpha, beta, False)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for row, col in self.get_available_moves():
                new_board = self.copy()
                new_board.make_move(row, col)
                score = new_board.minimax(depth - 1, alpha, beta, True)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

    def get_best_move(self):
        best_score = -float('inf')
        best_move = None
        for row, col in self.get_available_moves():
            new_board = self.copy()
            new_board.make_move(row, col)
            score = new_board.minimax(depth=9, alpha=-float('inf'), beta=float('inf'), maximizing_player=True)
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

    def copy(self):
        new_board = TicTacToe()
        new_board.board = [[x for x in row] for row in self.board]
        new_board.player
