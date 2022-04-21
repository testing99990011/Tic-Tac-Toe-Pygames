import random
import copy

class GameLogic:
    '''
    Functions for main game logic.
    Includes AI function
    '''

    def __init__(self):
        # Default values that the AI will prefer
        self.prefer_moves_center = 22
        self.prefer_moves_corner = [11, 13, 31, 33]

    def check_game_over(self, board):
        # Return true if game over and who wins

        # Check the rows
        for row in range(1, 4):
            if board[int(str(row) + "1")]['val'] == board[int(str(row) + "2")]['val'] == board[int(str(row) + "3")]['val'] and board[int(str(row) + "1")]['val'] != None:
                return board[int(str(row) + "1")]['val']

        # Check the columns
        for col in range(1, 4):
            if board[int("1" + str(col))]['val'] == board[int("2" + str(col))]['val'] == board[int("3" + str(col))]['val'] and board[int("1" + str(col))]['val'] != None:
                return board[int("1" + str(col))]['val']

        # Check the diagonals top left across
        if board[11]['val'] == board[22]['val'] == board[33]['val'] and board[11]['val'] != None:
           return board[11]['val']

        # Check the diagonals top right across
        if board[13]['val'] == board[22]['val'] == board[31]['val'] and board[13]['val'] != None:
            return board[13]['val']

        # Check if a tie
        new_lst = []
        for row in range(1, 4):
            for col in range(1, 4):
                new_lst.append(board[int(str(row) + str(col))]['val'])
        if None not in new_lst:
            return "Tie"

    def AI_easy_turn(self, board):
        # Run an easy random number generation script for AI turn
        aval_numbers = []
        for row in range(1, 4):
            for col in range(1, 4):
                if board[int(str(row) + str(col))]['val'] == None:
                    aval_numbers.append(int(str(row) + str(col)))
        return random.choice(aval_numbers)

    def AI_medium_turn(self, board, ai_symbol):
        # Check if turn causes a win
        # Create a copy board. Deepcopy cant copy pygames font.
        # Create a new board with just values
        stripped_board = {}
        for row in range(1,4):
            for col in range(1, 4):
                stripped_board[int(str(row) + str(col))] = {'val': board[int(str(row) + str(col))]['val']}

        # Find aval_numbers
        aval_numbers = []
        for row in range(1, 4):
            for col in range(1, 4):
                if board[int(str(row) + str(col))]['val'] == None:
                    aval_numbers.append(int(str(row) + str(col)))

        # Find the winning moves using the copy board
        winning_moves = []
        for number in aval_numbers:
            # See notes on how deepcopy works in browser bookmark
            copy_board = copy.deepcopy(stripped_board)
            copy_board[number]['val'] = ai_symbol
            if self.check_game_over(copy_board) == ai_symbol:
                winning_moves.append(number)
        if winning_moves:
            return winning_moves[0]
        else:
            return random.choice(aval_numbers)

    def AI_hard_turn(self, board, ai_symbol, player_symbol):
        # Check if next move causes AI win
        # Check if next move causes player win
        # Prefer AI win, call player block, then choose random
        stripped_board = {}
        for row in range(1, 4):
            for col in range(1, 4):
                stripped_board[int(str(row) + str(col))] = {'val': board[int(str(row) + str(col))]['val']}

        # Find aval numbers
        aval_numbers = []
        for row in range(1, 4):
            for col in range(1, 4):
                if board[int(str(row) + str(col))]['val'] == None:
                    aval_numbers.append(int(str(row) + str(col)))

        # Check if aval numbers result in a win
        winning_moves = []
        for number in aval_numbers:
            copy_board = copy.deepcopy(stripped_board)
            copy_board[number]['val'] = ai_symbol
            if self.check_game_over(copy_board) == ai_symbol:
                winning_moves.append(number)

        # Check if aval numbers result in a block
        blocking_moves = []
        for number in aval_numbers:
            copy_board = copy.deepcopy(stripped_board)
            copy_board[number]['val'] = player_symbol
            if self.check_game_over(copy_board) == player_symbol:
                blocking_moves.append(number)

        # Return winning moves, blocking moves
        if winning_moves:
            return winning_moves[0]
        elif blocking_moves:
            return blocking_moves[0]

        # Return the middle move
        if self.prefer_moves_center in aval_numbers:
            return self.prefer_moves_center

        # Return possible corner moves
        possible_corner = []
        for value in aval_numbers:
            if value in self.prefer_moves_corner:
                possible_corner.append(value)
        if possible_corner:
            return random.choice(possible_corner)
        return random.choice(aval_numbers)

if __name__ == '__main__':
    # Testing check_game_over
    instance = GameLogic()
    dictt = {11: {'val': None}, 12: {'val': None}, 13: {'val': None}, 21: {'val': None}, 22: {'val': 1}, 23: {'val': None}, 31: {'val': 0}, 32: {'val': 0}, 33: {'val': 0}}
    print(instance.check_game_over(dictt))
