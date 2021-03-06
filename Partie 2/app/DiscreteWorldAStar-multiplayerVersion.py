# -*- coding: utf-8 -*-

# Nicolas, 2015-11-18

from __future__ import absolute_import, print_function, unicode_literals
import sys, os

cwd = os.getcwd()
sys.path.append(cwd.replace("app", "teaching-iaro/pySpriteWorld-forStudents", 1))

from gameclass import Game,check_init_game_done
from spritebuilder import SpriteBuilder
from players import Player
from sprite import MovingSprite
from ontology import Ontology
from itertools import chain

from repartiteur import *
from GTAPotion import *

import pygame
import glo

import random 
import numpy as np



    
# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'pathfindingWorld_multiPlayer'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    player = game.player
    game.mask.allow_overlaping_players = True
    
def main():

    #for arg in sys.argv:
    iterations = 100 # default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
    print ("Iterations: ")
    print (iterations)

    init("thirst")

    #rep = repGaleShapley
    rep = repEnchere

    
    #-------------------------------
    # Initialisation
    #-------------------------------
       
    players = [o for o in game.layers['joueur']]
    nbPlayers = len(players)
    score = [0]*nbPlayers
    playercpt = []

       
    #initStates= []
    
    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print ("Init states:", initStates)
    
    # on localise tous les objets ramassables
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print ("Goal states:", goalStates)
        
    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    #print ("Wall states:", wallStates)
        
    
    #-------------------------------
    # Boucle principale de déplacements 
    #-------------------------------
        
    path = rep(initStates, goalStates, wallStates)
    playercpt = [0 for i in range(nbPlayers)]

    # Preparation du jeu d'echange de potions
    
    if len(sys.argv) < 2:
        l = []
    else:
        l = sys.argv[2:]
    
    while len(l) < len(players):
        l.append(random.randrange(5))
    mG = PotionGame(l)

    for i in range(iterations):
        
        for j in range(nbPlayers): # on fait bouger chaque joueur séquentiellement
            row, col = path[j][playercpt[j]]
            players[j].set_rowcol(row, col)
            game.mainiteration()
            playercpt[j] += 1

            if (row,col) in goalStates:
                o = players[j].ramasse(game.layers)
                game.mainiteration()
                print ("Objet trouvé par le joueur ", j)
                goalStates.remove((row,col)) # on enlève ce goalState de la liste
                score[j]+=1
                
        
                # et on remet un même objet à un autre endroit
                x = random.randint(1,19)
                y = random.randint(1,19)
                while (x,y) in wallStates or (x,y) in goalStates or (x,y) in initStates:
                    x = random.randint(1,19)
                    y = random.randint(1,19)
                o.set_rowcol(x,y)
                goalStates.append((x,y)) # on ajoute ce nouveau goalState
                game.layers['ramassable'].add(o)
                game.mainiteration()

                initStates = [o.get_rowcol() for o in game.layers['joueur']]
                path = rep(initStates, goalStates, wallStates)
                playercpt = [0 for i in range(nbPlayers)]

            def getNeighbours(row, col):
                l = [o.get_rowcol() for o in game.layers['joueur']]
                r = []
                if (row+1, col) in l:
                    r.append(l.index((row+1, col)))
                if (row, col+1) in l:
                    r.append(l.index((row, col+1)))
                if (row-1, col) in l:
                    r.append(l.index((row-1, col)))
                if (row, col-1) in l:
                    r.append(l.index((row, col-1)))
                return r

            for k in getNeighbours(row,col):
                if(k == j):
                    print("BUG COLLISION")
                elif(score[k] != 0 and score[j] != 0):
                    score = mG.meet(j, k, score)
                else:
                    print("JEU IMPOSSIBLE, PAS ASSEZ DE POINTS")

                
    
    print ("scores:", score)
    pygame.quit()
    
        
    
   

if __name__ == '__main__':
    main()
    


