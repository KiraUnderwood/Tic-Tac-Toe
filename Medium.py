import random

from Basic_easy_level import Game, GameState, Field


class MediumGame(Game):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.with_easy = self.easy()

    def easy(self):
        if self.player2 == 'easy' or self.player1 == 'easy':
            return True
        else:
            return False

    def index_where_to_place_element(self, symb):
        for i, row in enumerate(self.tt_field):
            if row.count(symb) == 2 and Field.N.value in row:
                j = row.index(Field.N.value)
                return i, j
        for j in range(3):
            elems = []
            for i in range(3):
                elems.append(self.tt_field[i][j])
            if elems.count(symb) == 2 and Field.N.value in elems:
                i = elems.index(Field.N.value)
                return i, j
        diag1 = [self.tt_field[0][0], self.tt_field[1][1], self.tt_field[2][2]]
        if diag1.count(symb) == 2 and Field.N.value in diag1:
            if self.tt_field[0][0] == Field.N.value:
                i, j = 0, 0
                return i, j
            elif self.tt_field[1][1] == Field.N.value:
                i, j = 1, 1
                return i, j
            elif self.tt_field[2][2] == Field.N.value:
                i, j = 2, 2
                return i, j
        diag2 = [self.tt_field[0][2], self.tt_field[1][1], self.tt_field[2][0]]
        if diag2.count(symb) == 2 and Field.N.value in diag2:
            if self.tt_field[0][2] == Field.N.value:
                i, j = 0, 2
                return i, j
            elif self.tt_field[1][1] == Field.N.value:
                i, j = 1, 1
                return i, j
            elif self.tt_field[2][0] == Field.N.value:
                i, j = 2, 0
                return i, j
        return False

    def ai_turn(self):

        if self.count % 2 != 0 and self.with_easy:
            super().ai_turn()
        else:
            fields = [''.join(y) for i in self.tt_field for y in i]
            fields_string = ''.join(fields)
            if fields_string.count(Field.X.value) > fields_string.count(Field.O.value):
                symb = Field.O.value
            else:
                symb = Field.X.value
            opposite_symb = Field.X.value if symb == Field.O.value else Field.O.value
            # check if can win
            if self.index_where_to_place_element(symb):
                i, j = self.index_where_to_place_element(symb)
                tup = self.STEPS[i][j]
                self.placement(i, j, tup)
                print('Making move level "medium"')
                self.draw_board()
            elif self.index_where_to_place_element(opposite_symb):
                i, j = self.index_where_to_place_element(opposite_symb)
                tup = self.STEPS[i][j]
                self.placement(i, j, tup)
                print('Making move level "medium"')
                self.draw_board()
            else:
                i, j = random.choice(self.avail_steps)
                x, y = self.find_idx_of_inp_coord(i, j)
                self.placement(x, y, (i, j))
                print('Making move level "medium"')
                self.draw_board()
            self.count += 1
