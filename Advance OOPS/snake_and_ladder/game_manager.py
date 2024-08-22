from snake_and_ladder_game import Snake_and_ladder
import threading

class GameManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.games = []

    @staticmethod
    def get_instance():
        if not GameManager._instance:
            with GameManager._lock:
                if not GameManager._instance:
                    GameManager._instance = GameManager()
        return GameManager._instance

    def start_new_game(self, player_names):
        game = Snake_and_ladder(player_names)
        self.games.append(game)
        threading.Thread(target=game.play).start()
        


