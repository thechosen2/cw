from engine.main import Game
import scriptblue
import scriptred1

if __name__ == "__main__":
    G = Game((40, 40), scriptred1, scriptblue)
    G.run_game()