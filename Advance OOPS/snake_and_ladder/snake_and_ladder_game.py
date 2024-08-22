from dice import Dice
from board import Board
from player import Player

class Snake_and_ladder:
    def __init__(self, player_list):
        self.dice = Dice()
        self.board = Board()
        self.players = [Player(player) for player in player_list]
        self.curr_player_position = 0
        
    def play(self):
        while not self._is_game_over():
            curr_player = self.players[self.curr_player_position]
            dice_roll = self.dice.roll()
            curr_position = curr_player.get_position()
            new_position = curr_position + dice_roll
            
            if new_position <= Board.board_size:
                curr_player.set_position(self.board.get_position_on_board(new_position))
                print(f'player {curr_player.get_name()} rolled a {dice_roll} and moved to {new_position}')
                
            if curr_player.get_position() == Board.board_size :
                print(f'{curr_player.get_name()} Wins!')
                break
            
            self.curr_player_position = (self.curr_player_position + 1) % len(self.players)
        
    def _is_game_over(self):
        for player in self.players:
            if player.get_position() == self.board.board_size:
                return True
        return False