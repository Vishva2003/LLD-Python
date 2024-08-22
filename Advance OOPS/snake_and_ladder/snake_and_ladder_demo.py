from game_manager import GameManager

def run():
    game_manager = GameManager.get_instance()
    
    players1 = ["Vis", "Kiss"]
    game_manager.start_new_game(players1)

    
if __name__ == '__main__':
    run()