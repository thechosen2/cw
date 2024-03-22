from engine.main import Game
import scriptblue
import scriptred1
import scriptred
import sample1
import script
import oldus
if __name__ == "__main__":
    for i in range (20):
        try:
            G = Game((40, 40), scriptred1, oldus)
            G.run_game() 
        except:
            pass
