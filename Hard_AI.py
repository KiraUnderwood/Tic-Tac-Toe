import copy
import random

from Medium import MediumGame, GameState, Field


class HardGame(MediumGame):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.recursion_state = GameState.O.value
        self.with_medium = self.medium()

    def medium(self):
        if self.player2 == 'medium' or self.player1 == 'medium':
            return True
        else:
            return False

    def check_state_for_recurssion(self, board):
        state = True
        for i in board:
            if ''.join(i) == Field.X.value * 3:

                self.recursion_state = GameState.X.value
                state = False
                return state
            elif ''.join(i) == Field.O.value * 3:

                self.recursion_state = GameState.O.value
                state = False
                return state
        for j in range(3):
            elems = []
            for i in range(3):
                elems.append(board[i][j])
            if ''.join(elems) == Field.X.value * 3:

                self.recursion_state = GameState.X.value
                state = False
                return state
            elif ''.join(elems) == Field.O.value * 3:

                self.recursion_state = GameState.O.value
                state = False
                return state
        if board[0][0] == board[1][1] == board[-1][-1] == Field.X.value:

            self.recursion_state = GameState.X.value
            state = False
            return state
        elif board[0][0] == board[1][1] == board[-1][-1] == Field.O.value:

            self.recursion_state = GameState.O.value
            state = False
            return state
        elif board[0][-1] == board[1][1] == board[-1][0] == Field.X.value:

            self.recursion_state = GameState.X.value
            state = False
            return state
        elif board[0][-1] == board[1][1] == board[-1][0] == Field.O.value:

            state = False
            return state

        fields = [''.join(y) for i in board for y in i]
        fields_string = ''.join(fields)
        if Field.N.value not in fields_string:
            self.recursion_state = GameState.D.value
            state = False
        # else:
        # print(GameState.C.value)
        return state

    def minmax(self, board: list, player: str, ai_player: str):
        next_player = Field.O.value if player == Field.X.value else Field.X.value
        # print(player)
        if not self.check_state_for_recurssion(board):
            if self.recursion_state == GameState.D.value:
                return None, 0
            if self.recursion_state == GameState.X.value:
                if ai_player == Field.X.value:
                    return None, 10
                else:
                    return None, -10
            elif self.recursion_state == GameState.O.value:
                if ai_player == Field.O.value:
                    return None, 10
                else:
                    return None, -10

        else:
            res = {}
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if board[i][j] == Field.N.value:
                        copy_board = copy.deepcopy(board)
                        copy_board[i][j] = player
                        result = self.minmax(copy_board, next_player, ai_player)
                        res[(i, j)] = result[1]

            if player == ai_player:
                k = max(res, key=res.get)
                v = res[k]
                # print(k, v)
                return k, v
            else:
                k = min(res, key=res.get)
                v = res[k]
                # print(k, v)
                return k, v

    def ai_turn(self):

        if self.count % 2 != 0 and self.with_easy:
            super().ai_turn()
        elif self.count % 2 != 0 and self.with_medium:
            super().ai_turn()
        else:
            fields = [''.join(y) for i in self.tt_field for y in i]
            fields_string = ''.join(fields)
            if Field.O.value not in fields_string and Field.X.value not in fields_string:
                i, j = random.choice(self.avail_steps)
                x, y = self.find_idx_of_inp_coord(i, j)
                self.placement(x, y, (i, j))
                print('Making move level "hard"')
                self.draw_board()
            else:
                if fields_string.count(Field.X.value) > fields_string.count(Field.O.value):
                    symb = Field.O.value
                else:
                    symb = Field.X.value
                indexes, _ = self.minmax(self.tt_field, symb, symb)
                i, j = indexes
                tup = self.STEPS[i][j]
                self.placement(i, j, tup)
                print('Making move level "hard"')
                self.draw_board()
            self.count += 1
