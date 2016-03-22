from __future__ import division

import random

class PotionGame:

	def __init__(self, l = []):
		self.ps = l
		self.strategies = [self.randomStrat, self.aggressiveStrat, self.peacefulStrat, self.opportunistStrat, self.learningStrat]
		self.statAgro = [0 for i in range(len(l))]
		self.statTalk = [0 for i in range(len(l))]

	def addStrategy(self, s):
		self.ps += s

	def meet(self, a, b, score):
		print ("A : ", a, ", B : ", b)
		print ("SCORE INITIAL : ", score)
		print ("Strats : ", self.ps)
		self.score = score
		mise = min(score[a], score[b])
		print ("MISE : ", mise)
		ab = self.isAggressive(a, b)
		ba = self.isAggressive(b, a)
		if ab and ba:
			print ("AFFRONTEMENT")
			score[a] -= mise
			score[b] -= mise
			self.statAgro[a] += 1
			self.statAgro[b] += 1
		elif ab:
			print ("A VOLE B")
			score[a] += mise
			score[b] -= mise
			self.statAgro[a] += 1
			self.statTalk[b] += 1
		elif ba:
			print ("B VOLE A")
			score[b] += mise
			score[a] -= mise
			self.statTalk[a] += 1
			self.statAgro[b] += 1
		else:
			print ("COOPERATION")
			score[a] += mise//2
			score[b] += mise//2
			self.statTalk[a] += 1
			self.statTalk[b] += 1
		print("SCORE FINAL : ", score)
		return score

	def isAggressive(self, p, a):
		if len(self.strategies) <= p:
			return self.strategies[0](p, a)
		return self.strategies[int(self.ps[p])](p, a)

	def aggressiveStrat(self, a, b):
		return True

	def peacefulStrat(self, a, b):
		return False

	def randomStrat(self, a, b):
		return bool(random.getrandbits(1))

	def opportunistStrat(self, a, b):
		return self.score[a] < (2*self.score[b])

	def learningStrat(self, a, b):
		print ("LEARNING STRAT ", a," SUR ", b)
		print ("CHANCE D AGRO DE ", b," : ", self.chanceTalk(b))
		mise = min(self.score[a], self.score[b])
		agro = self.chanceTalk(b) * mise - (1 - self.chanceTalk(b)) * mise
		talk = self.chanceTalk(b) * (mise//2) - (1 - self.chanceTalk(b)) * mise
		print ("MISE D AGRO : ", agro)
		print ("MISE DE PAROLE", talk)
		if agro > talk :
			return True
		else :
			return False

	def chanceTalk(self, b):
		if self.statTalk[b] + self.statAgro[b] == 0:
			return 0.5
		return self.statTalk[b]/(self.statTalk[b] + self.statAgro[b])

