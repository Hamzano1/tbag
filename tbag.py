print("__________          __  .__                      ________                       ")
print("\______   \___.__._/  |_|  |__   ____   ____    /  _____/_____    _____   ____  ")
print(" |     ___<   |  |\   __\  |  \ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \ ")
print(" |    |    \___  | |  | |   Y  (  <_> )   |  \ \    \_\  \/ __ \|  Y Y  \  ___/ ")
print(" |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /__|_|  /\___  >")
print("           \/                \/            \/          \/     \/      \/     \/ ")

import sys
from time import sleep

def restart_the_game():
    sleep(2.5)
    print("\nEnter 'restart' to restart the game or anything else to end the game:")
    action= input().lower()

    if action == "restart":
        start()
    else:
        sleep(2.5)
        print("Game Over!")

def start():
    import time
    sleep(2.5)
    print("\nYou are on a spaceship and the fuel runs out!")
    sleep(2.5)
    print("\nYou crash land on an unkown planet.")
    sleep(2.5)
    print("\nYou put on your astronaut suit.")
    sleep(2.5)
    print("\nAs you step out, you find yourself in a forest.")
    sleep(2.5)
    print("\nYou also see a small wooden cottage in the distance.")
    sleep(2.5)
    print("\nDo you got to the cottage or stay at the spaceship?")
    sleep(2.5)
    print("\nEnter 'go' to go to the cottage or 'stay' to stay at the spaceship:")
    
    action = input().lower()
    
    x = False
    while x==False:
        if action == "go":
            sleep(2.5)
            print("\nYou have approached the wooden cottage.")
            x = True
            in_the_cottage()
        elif action=="stay":
            sleep(2.5)
            print("\nYou have gone back into the spaceship")
            x = True
            back_in_spacecraft()
        else:
            sleep(2.5)
            print("\nError! Enter 'go' to go to the cottage or 'stay' to stay at the ship:")
            action = input().lower


def back_in_spacecraft():
    sleep(2.5)
    print("\nYou slowly run out of oxygen.")
    sleep(2.5)
    print("\nYou are dead!")
    restart_the_game()



def in_the_cottage():
    import time
    sleep(2.5)
    print("\nYou are inside the cottage now.")
    sleep(2.5)
    print("\nThe living room is empty and you find a swiss knife on the floor")
    sleep(2.5)
    print("\nDo you pick it up or explore the cottage?")
    sleep(2.5)
    print("\nEnter 'pick' to pick up the knife or 'explore' to explore the cottage:")
    
    action = input().lower()
    x = False
    
    while x==False:
        if action == "pick":
            x = True
            pick_knife()
        elif action=="explore":
            x = True
            no_knife()
        else:
            sleep(2.5)
            print("\nError! Enter 'pick' to pick up the knife or 'explore' to explore the ship:")
            action = input().lower()

def no_knife():
    sleep(2.5)
    print("\nYou are exploring the inside of the cottage.")
    sleep(2.5)
    print("\nYou look thorugh each room.")
    sleep(2.5)
    print("\nYou open one room and there is a giant spider")
    sleep(2.5)
    print("\nOh No! You don't have any weapons to fight the spider!")
    sleep(2.5)
    print("\nThe spider attacks and kills you")
    sleep(2.5)
    restart_the_game()

def pick_knife():
    sleep(2.5)
    print("\nYou have picked up the knife.")
    sleep(2.5)
    print("\nLet's explore the cottage.")
    sleep(2.5)
    print("\nEnter 'explore' to explore the cottage:")

    action=input().lower()
    x = False

    while x==False:
        if action == "explore":
            x = True
            explore_the_cottage()
        else:
            sleep(2.5)
            print("\nError! Enter 'explore' to explore the cottage:")
            action = input().lower()


def explore_the_cottage():
    sleep(2.5)
    print("\nYou are exploring the inside of the cottage.")
    sleep(2.5)
    print("\nYou look thorugh each room.")
    sleep(2.5)
    print("\nYou open one room and there is a giant spider")
    sleep(2.5)
    print("\nEnter 'attack' to kill the spider with your knife!")
    sleep(2.5)
    action=input().lower()
    x = False

    while x==False:
        if action=='attack':
            sleep(2.5)
            print("\nYou have killed the spider!")
            x = True
        else:
            sleep(2.5)
            print("\nError! Enter 'attack' to kill the spider with your knife:")
            action = input().lower()


start()