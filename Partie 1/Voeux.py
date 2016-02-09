# -*- coding: utf-8 -*-

class VoeuxSpe :
    
    def __init__(self, fic):
        
        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()
        
        self.nbEtu = contenu[0].split()[0]
        temp = contenu[1].split()
        self.capaSpe = {}
        self.voeux = {}
        self.contient = {}
        for i in range( 2, len(temp)+2):
            contenu[i]=contenu[i].split()
            self.voeux[contenu[i][0]] = [int(a) for a in contenu[i][1:]]
            self.contient[contenu[i][0]] = []
            self.capaSpe[contenu[i][0]] = int(temp[i-2])
    
    def gCS(self,etu):
        dic = {} #dictionaire nomSpe->boolean(est plein)
        i = 0 #rang du voeux a prendre en compte
        while dicAnd(dic): #tant que toutes les spes ne sont pas pleines
            for x in self.voeux: #pour chaques clés du dico de spe
                if len(self.contient[x]) < self.capaSpe[x]: #test si la spe est pleine
                    dic[x] = False
                    rEtu = self.voeux[x][i]#alias
                    etuAppa = etu.tabEtu[rEtu] #alias
                    if etuAppa[1] == "":#Cas etu non appareillé
                        self.contient[x].append(rEtu)
                        etuAppa[1] = x
                    else:
                        if etu.voeux[rEtu].index(x) < etu.voeux[rEtu].index(etuAppa[1]): #Cas etu preferant la spe lui demandant
                            self.contient[etuAppa[1]].remove(rEtu)
                            self.contient[x].append(rEtu)
                            etuAppa[1] = x
                else:
                    dic[x] = True
        i +=1
        
class VoeuxEtu :
    
    def __init__(self, fic):
        
        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()
        
        self.nbEtu = int(contenu[0].split()[0])
        self.tabEtu = []
        self.voeux = []
        for i in range( 1, self.nbEtu):
            contenu[i]=contenu[i].split()
            self.voeux.append(contenu[i][1:])
            self.tabEtu.append([contenu[i][1], ""])

def dicAnd(dic):
    val = True
    for i in dic:
        val = val and i
    return val