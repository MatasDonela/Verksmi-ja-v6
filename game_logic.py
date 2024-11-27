import time
from random import *

print("import")
player_count = 0

players = []

turn = 0
turn_count = 0

game_setup = True
choosing_players = True

while True:
# GAME SETUP

    # PLAYER COUNT AND PLAYER STARS

    if choosing_players == True:
        player_count = int(input("Player Count: "))
        if player_count < 5 and player_count > 1:
            print("There are", player_count,"players")
            choosing_players = False
            for i in range(player_count):
                players.append([i+1, i])
            print(players)
        else:
            print("INVALID PLAYER AMOUNT")
            choosing_players = True

    # MANAGING TURNS
    
    turn += 1
    turn_count +=1     # TURN COUNT IS KINDA JUST FOR FUN, IT DOESNT MATTER

    # FOR EACH PLAYERS TURN
    if turn > player_count:
        turn = 1
    print("turn =",turn_count)
    for i in range(len(players)):
        if players[i][0] == turn: # THE CODE HERE RUNS FOR THE PLAYER WHOS TURN IT IS
            print("player", i+1, "is moving")
            print("player", i+1, "has", players[i][1], "points")
            input("ROLL: ")
            roll = randint(1,4)
            print(roll)
            give_star =input("Give a star? ")
            if give_star == "y":
                players[i][1] +=1
            else:
                continue
        else:                                     # THE CODE HERE RUNS FOR THE PLAYERS WHOS TURN IT ISNT
            print("player", i+1, "is NOT moving")
            
    input("END TURN: ")
    
    time.sleep(0.1)
