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

from AStar import doAStar

import pygame
import glo

import random 
import numpy as np



# ---- ---- ---- ---- ---- ----
# ---- Misc                ----
# ---- ---- ---- ---- ---- ----


class RobotWorldSpriteBuilder(SpriteBuilder):
    """ classe permettant d'afficher le personnage sous 4 angles differents
    """
    def basicSpriteFactory(self, layername, tileid, x, y, img=None):
        if img is None: img = self.sheet[tileid]
        if layername == "joueur":
            imglist = [self.sheet[i, j] for i, j in ((10, 0), (8, 0), (9, 0), (11, 0))]
            p = Player(layername, tileid, x, y, imglist)
            if tileid[0] in [10, 8, 9, 11]:
                p.translate_sprite(0, 0, 90 * [10, 8, 9, 11].index(tileid[0]))
            return p
        elif layername == "personnage":
            return MovingSprite(layername, tileid, x, y, [img])
        else:
            return SpriteBuilder.basicSpriteFactory(self, layername, tileid, x, y, img)







# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'pathfindingWorld3'
    game = Game('Cartes/' + name + '.json', RobotWorldSpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    player = game.player
   
def main():

    init("pathfindingWorld_MultiPlayer2")
   




   
    #-------------------------------
    # Building the matrix
    #-------------------------------
       
       
       
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
    # Building the best path with A*
    #-------------------------------
   
    path = doAStar(initStates[0], goalStates[0], wallStates)
        
    #-------------------------------
    # Moving along the path
    #-------------------------------


    for i in path:

        player.set_rowcol(i[0],i[1])
        print ("pos:",i[0],i[1])
        game.mainiteration()
            
        # si on a trouvé l'objet on le ramasse
        if (i[0],i[1])==goalStates[0]:
            o = game.player.ramasse(game.layers)
            game.mainiteration()
            print ("Objet trouvé!")
            break
        '''
        #x,y = game.player.get_pos()
   
        '''

    pygame.quit()
   
        
   
  

if __name__ == '__main__':
    main()
   


