from engine.main import Game
import scriptblue
import scriptred1
import scriptred
import sample1
import script
import oldus
import oldnewus
# import V2
if __name__ == "__main__":
    for i in range (1):
        try:
            G = Game((40, 40), scriptred1, oldnewus)
            G.run_game() 
        except:
            pass
