import sys

from Basic_easy_level import Game
from Medium import MediumGame
from Hard_AI import HardGame


users = {'easy', 'user'}
users_medium = {'medium', 'user'}
mixed = {'medium', 'easy'}
mixed1 = {'medium', 'easy', 'hard'}
users_hard = {'hard', 'user'}

if __name__ == "__main__":
    while True:
        print("Input command: ")
        cmd = sys.stdin.readline().strip().split()
        if len(cmd) == 1:
            if cmd[0].lower() == 'exit':
                break
            else:
                print("Bad parameters!")
                continue
        elif len(cmd) == 3:
            if cmd[0].lower() == 'start':
                if cmd[1] in users and cmd[2] in users:
                    game = Game(player1=cmd[1], player2=cmd[2])
                    game.start_game()
                elif (cmd[1] in users_medium and cmd[2] in users_medium) or (cmd[1] in mixed and cmd[2] in mixed):
                    game = MediumGame(player1=cmd[1], player2=cmd[2])
                    game.start_game()
                elif (cmd[1] in users_hard and cmd[2] in users_hard) or (cmd[1] in mixed1 and cmd[2] in mixed1):
                    game = HardGame(player1=cmd[1], player2=cmd[2])
                    game.start_game()
                else:
                    print("Bad parameters!")
                    continue
        else:
            print("Bad parameters!")
            continue
