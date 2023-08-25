
import random

#from game.gamemanager import GameManager
from game.checkers import Checkerboard
infinity = 1.0e400
def random_player(state, game):
    """A player that chooses a legal move at random."""
    return random.choice(game.legal_moves())

# possible move looks like this: [[[17, 6, 16], [12, 16, 6]], [[35, 6, 16], [30, 16, 6]], [[35, 6, 16], [29, 16, 6]], [[37, 6, 16], [31, 16, 6]], [[39, 6, 16], [34, 16, 6]], [[40, 6, 16], [34, 16, 6]], [[42, 6, 16], [36, 16, 6]], [[47, 6, 16], [41, 16, 6]]]
# [[42, 6, 16], [36, 16, 6]]


def bot(state: Checkerboard, game):
    player = game.to_move(state)
    print(player)
    """A player that chooses a legal move at random."""
    print(state)
    print(game)
    legal_choices = game.legal_moves()
    
    print(legal_choices)
    #our_move = random.choice(legal_choices)
    highest_score = -infinity
    best_move = None
    for move in legal_choices:
        state.make_move(move, notify=True, undo=True)
        moves2 =state.moves
        for move2 in moves2:
            state.make_move(move2, notify=True, undo=True)
            moves3 = state.moves
            for move3 in moves3:
                state.make_move(move3, notify=True, undo=True)
                score = evaluate(state, player)
                if score > highest_score:
                    highest_score = score
                    print(score)
                    best_move = move
                state.undo_move()
            state.undo_move()
        state.undo_move()

    print(best_move)
    
    return best_move

def evaluate(state: Checkerboard, player):
    state.center
    if player == 2:
        return state.white_total - state.black_total
    else:
        return state.black_total - state.white_total 
    




