# write your code here
import sys
import random
from enum import Enum


class Field(Enum):
    X = 'X'
    O = 'O'
    N = '_'


class GameState(Enum):
    C = "Game not finished"
    D = "Draw"
    X = "X wins"
    O = "O wins"


class Game:
    class GameMode(Enum):
        AI_AI = 'ai'
        U_AI = 'semi'
        U_U = 'user'
        LEVELS = {'easy', 'medium', 'hard'}

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2
        self.mode = self.mode()
        self.count = 1
        self.state = GameState.C.value
        self.STEPS = [[(1, 3), (2, 3), (3, 3)], [(1, 2), (2, 2), (3, 2)], [(1, 1), (2, 1), (3, 1)]]
        self.tt_field = [[Field.N.value for a in range(3)] for b in range(3)]
        self.avail_steps = [(1, 3), (2, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)]

    def mode(self):
        if self.player2 in self.GameMode.LEVELS.value and self.player1 in self.GameMode.LEVELS.value:
            return self.GameMode.AI_AI.value
        elif self.player1 == self.player2 == 'user':
            return self.GameMode.U_U.value
        else:
            return self.GameMode.U_AI.value

    def start_game(self):
        if self.mode == self.GameMode.AI_AI.value:
            self.draw_board()
            while self.game_state():
                self.ai_turn()
                if not self.game_state():
                    break
        elif self.mode == self.GameMode.U_AI.value:
            while self.game_state():
                x, y, tup = self.inp_coord()
                self.placement(x, y, tup)
                if not self.game_state():
                    break
                else:
                    self.ai_turn()
        elif self.mode == self.GameMode.U_U.value:
            while self.game_state():
                x, y, tup = self.inp_coord()
                self.placement(x, y, tup)
                if not self.game_state():
                    break

    def draw_board(self):
        print("---------")
        for row in self.tt_field:
            print("| " + ' '.join(row) + " |")
        print("---------")

    def find_idx_of_inp_coord(self, i, j):
        for x, row in enumerate(self.tt_field):
            for y, col in enumerate(row):
                if self.STEPS[x][y] == (i, j):
                    return x, y

    def inp_coord(self):
        while True:
            print("Enter the coordinates: ")
            coord = sys.stdin.readline().strip().split()

            if (len(coord) < 2 and len(coord[0]) != 2) or (len(coord) > 2):
                print("You should enter numbers!")
                continue

            elif len(coord) == 1 and len(coord[0]) == 2:
                check = True
                for elem in coord[0]:
                    if not elem.isdigit():
                        print("You should enter numbers!")
                        check = False
                        break
                    elif int(elem) not in range(1, 4):
                        print("Coordinates should be from 1 to 3")
                        check = False
                        break
                if check:
                    i, j = list(coord[0])
                    cor_i, cor_j = self.find_idx_of_inp_coord(int(i), int(j))
                    if self.tt_field[cor_i][cor_j] != Field.N.value:
                        print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        return cor_i, cor_j, (int(i), int(j))

            elif len(coord) == 2:
                check = True
                for el in coord:
                    if not el.isdigit():
                        print("You should enter numbers!")
                        check = False
                        break
                    elif int(el) not in range(1, 4):
                        print("Coordinates should be from 1 to 3!")
                        check = False
                        break
                if check:
                    i, j = coord
                    cor_i, cor_j = self.find_idx_of_inp_coord(int(i), int(j))
                    if self.tt_field[cor_i][cor_j] != Field.N.value:
                        print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        return cor_i, cor_j, (int(i), int(j))

    def placement(self, i, j, tup):
        fields = [''.join(y) for i in self.tt_field for y in i]
        fields_string = ''.join(fields)
        if fields_string.count(Field.X.value) > fields_string.count(Field.O.value):
            symb = Field.O.value
        else:
            symb = Field.X.value
        self.tt_field[i][j] = symb
        self.avail_steps.remove(tup)
        self.draw_board()

    def ai_turn(self):
        i, j = random.choice(self.avail_steps)
        x, y = self.find_idx_of_inp_coord(i, j)
        self.placement(x, y, (i, j))
        print('Making move level "easy"')
        self.draw_board()
        self.count += 1

    def game_state(self):
        state = True
        for i in self.tt_field:
            if ''.join(i) == Field.X.value * 3:
                print(GameState.X.value)
                self.state = GameState.X.value
                state = False
                return state
            elif ''.join(i) == Field.O.value * 3:
                print(GameState.O.value)
                self.state = GameState.O.value
                state = False
                return state
        for j in range(3):
            elems = []
            for i in range(3):
                elems.append(self.tt_field[i][j])
            if ''.join(elems) == Field.X.value * 3:
                print(GameState.X.value)
                self.state = GameState.X.value
                state = False
                return state
            elif ''.join(elems) == Field.O.value * 3:
                print(GameState.O.value)
                self.state = GameState.O.value
                state = False
                return state
        if self.tt_field[0][0] == self.tt_field[1][1] == self.tt_field[-1][-1] == Field.X.value:
            print(GameState.X.value)
            self.state = GameState.X.value
            state = False
            return state
        elif self.tt_field[0][0] == self.tt_field[1][1] == self.tt_field[-1][-1] == Field.O.value:
            print(GameState.O.value)
            self.state = GameState.O.value
            state = False
            return state
        elif self.tt_field[0][-1] == self.tt_field[1][1] == self.tt_field[-1][0] == Field.X.value:
            print(GameState.X.value)
            self.state = GameState.X.value
            state = False
            return state
        elif self.tt_field[0][-1] == self.tt_field[1][1] == self.tt_field[-1][0] == Field.O.value:
            print(GameState.O.value)
            self.state = GameState.O.value
            state = False
            return state

        fields = [''.join(y) for i in self.tt_field for y in i]
        fields_string = ''.join(fields)
        if Field.N.value not in fields_string:
            print(GameState.D.value)
            self.state = GameState.D.value
            state = False
        # else:
        # print(GameState.C.value)
        return state

