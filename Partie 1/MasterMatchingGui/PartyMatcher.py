#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from guimatcher import Ui_GUIMatcher


# Un Parti est un candidat aux associations, demandeur ou offreur, pouvant être connectée à un ou plusieurs autres partis.
class Party:
    def __init__(self, i, name, relatives, wishes):
        self.id = int(i)                # Identifiant
        self.name = name;               # Nom de ce parti
        self.relatives = int(relatives) # Nombre d'éléments liés à celui-ci (capacité maximale)
        self.wishes = wishes            # Liste des voeux du Parti dans un ordre décroissant
        self.links = []                 # Partis associés à celui-ci.

    # Compare deux candidats selon un ordre de préférence. Renvoie True si le premier candidat est préféré, False sinon.
    def compare(self, a, b):
        for i in self.wishes:
            if i == a:
                return True
            if i == b:
                return False

    # Renvoie True si ce parti est pleinement satisfait (capacité de couplage maximum atteinte)
    def isTaken(self):
        if len(self.links) < self.relatives:
            return False
        else:
            return True

    # Ajoute une nouvelle relation
    def meet(self, n):
        self.links.append(n)


    # Propose une association à ce parti
    def ask(self, n, matcher):
        # Cas où ce parti a déjà atteint sa capacité maximale
        if self.isTaken():
            worst = n
            for j in self.links:
                if self.compare(worst, j):
                    worst = j
            # Cas où le parti proposé n'est pas intéressant
            if worst == n:
                return False
            # Cas où le parti proposé est plus intéressant qu'un autre déjà lié
            else:
                self.links.remove(worst)
                matcher.divorce(worst, self.id)

        # Etablissement de la relation
        self.meet(n)
        return True


# Le PartyMatcher gère les couplages entre deux listes de Partis (qui peuvent avoir une capacité de couplage variable)
class PartyMatcher:
    # Construit une liste de demandeurs ou d'offreurs à partir d'un fichier.
    def loadParty(self, f, m):
        # Lecture du fichier
        o = open(f, "r")
        data = o.readlines()
        o.close()

        # Nombre de demandeurs
        nApp = int(data[0].split()[0])
        del data[0]

        # Nombre de places (capacité)
        if m:
            tRel = data[0].split()
            del data[0]
        else:
            tRel = [1] * nApp

        # Initialisation
        party = []

        # Lecture des données
        j = 0
        for i in data:
            i = i.split()
            p = Party(j, i[0], tRel[j], i[1:])
            party.append(p)
            j+= 1

        return party

    # Creation d'une liste de partis a partir d'une liste de voeux
    def createParty(self, data, capacity = 1):
        party = []
        for i in range(len(data)):
            p = Party(i, data[i][0], capacity, data[i][1:])
            party.append(p)

        return party

    # Cree les demandeurs
    def setApplicants(self, data):
        self.applicants = self.createParty(data)

    # Cree les offrants
    def setProviders(self, data):
        self.providers = self.createParty(data)

    # Standardise les voeux d'une liste de parties (spécifique à la lecture de voeux Spe)
    def numberWishes(self, parties, std):
        dic = {}

        for i in std:
            dic[i.name] = std.index(i)

        ni = 0
        for i in parties:
            nj = 0
            for j in i.wishes:
                parties[ni].wishes[nj] = dic[j]
                nj+= 1
            ni+= 1

        return parties

    # Standardise les voeux d'une liste de parties (spécifique à la lecture de voeux Etu)
    def intWishes(self, parties):
        ni = 0
        for i in parties:
            nj = 0
            for j in i.wishes:
                parties[ni].wishes[nj] = int(j)
                nj+= 1
            ni+= 1

        return parties

    # Supprime bilatéralement une relation
    def divorce(self, n, m):
        # On modifie le compteur de partis pleinement satisfaits
        if self.applicants[n].isTaken():
            self.w+= 1
        # On supprime le parti
        self.applicants[n].links.remove(m)

    # Applique l'algorithme d'association de Gale-Shapley à l'avantage des demandeurs
    def match(self):

        c = [-1] * len(self.applicants)     # Tableau de compteurs pour les demandeurs
        self.w = len(self.applicants)       # condition de boucle (des demandeurs n'ont pas encore de couplage stable)
        # Tant qu'il existe un parti non pleinement satisfait
        while self.w > 0:
            ni = 0
            # Pour tous les demandeurs...
            for i in self.applicants:
                # ...qui ne sont pas déjà en relation,
                if not i.isTaken():
                    # Pour tous les voeux des demandeurs,
                    while c[ni] < len(i.wishes):
                        c[ni]+= 1
                        # Le demandeur i fait sa demande à son voeu j
                        if self.providers[i.wishes[c[ni]]].ask(i.id, self):
                            # En cas de réponse positive, on enregistre la nouvelle relation
                            i.meet(self.providers[i.wishes[c[ni]]].id)
                            # On note si le demandeur est pleinement satisfait (capacité max atteinte)
                            if i.isTaken():
                                self.w-= 1
                        break
                ni+= 1

    # Affichage
    def printMatch(self, applicants, providers):
        print(self.getMatch())

    # Recuperation des donnees
    def getMatch(self):
        trace = []
        ni = 0
        for i in self.providers:
            trace.append([i.name])
            for j in i.links:
                trace[ni].append(self.applicants[j].name)
            ni+= 1

        return trace

    def __init__(self, appFile = None, proFile = None):

        # Chargement des fichiers
        if appFile:
            self.etu = self.loadParty(appFile, False)
        if proFile:
            self.spe = self.loadParty(proFile, True)

        # Normalisation des voeux étudiants
        if appFile and proFile:
            self.applicants = self.numberWishes(self.etu, self.spe)
            self.providers = self.intWishes(self.spe)

# Interface graphique
# class GUIMatcher(Ui_GUIMatcher):
#     def __init__(self, dialog):
#         Ui_GUIMatcher.__init__(self)
#         self.setupUi(dialog)
#         self.matchButton.clicked.connect(self.match)

#     def match(self):
#         PartyMatcher(self.appFile.text(), self.proFile.text())

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = QtWidgets.QDialog()

#     prog = GUIMatcher(dialog)

#     dialog.show()
#     sys.exit(app.exec_())
