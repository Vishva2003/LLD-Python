from snake import Snake
from ladder import Ladder

class Board:
    board_size = 100
    
    def __init__(self):
        self.snakes = []
        self.ladders = []
        self._initiate_snake_and_ladder()
        
    def _initiate_snake_and_ladder(self):
        self.snakes.append(Snake(23, 8))
        self.snakes.append(Snake(45, 25))
        self.snakes.append(Snake(63, 17))
        self.snakes.append(Snake(88, 45))
        self.snakes.append(Snake(95, 19))
        
        
        self.ladders.append(Ladder(10, 30))
        self.ladders.append(Ladder(33, 55))
        self.ladders.append(Ladder(13, 80))
        self.ladders.append(Ladder(40, 74))
        self.ladders.append(Ladder(74, 87))
        self.ladders.append(Ladder(82, 96))
        
    def get_boardsize(self):
        return Board.board_size
        
    def get_position_on_board(self, position):
        for snake in self.snakes:
            if snake.get_start() == position:
                return snake.get_end 
            
        for ladder in self.ladders:
            if ladder.get_start == position:
                return ladder.get_end
            
        return position
        