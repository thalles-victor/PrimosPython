import matplotlib.pyplot as plt
import numpy as np
import os


class GeneratorCounsinPrimes():
	def __init__(
		self, 
		min=0,
		max=10000,
		showInConsole=False,
		infoProgress = True
		):

		self.min = min
		self.max = max
		self.showInConsole = showInConsole
		self.infoProgress = infoProgress
		
		self.cousinNumbers = []
		self.listVariation = []
		self.inteiros = np.arange(self.min, self.max)
	
	def render(self, value):
		os.system('cls' if os.name == 'nt' else 'clear')
		x = value * 100 / self.max
		text = ''
		for index in range(int(x)):
			if (index % 5 == 0):
				text += '='
		text +='> ' + str(x)+ '%'
		print(text)

	def analysisP1rocessOfCounainPrimes(self, plotSimples=False):
		cousinInitial=[2, 3, 5, 7, 11, 13, 17, 19, 23 ]

		self.cousinNumbers.extend(cousinInitial)

		for elementInlistOfInteger in self.inteiros:
			validation=True

			if self.infoProgress:
				self.render(elementInlistOfInteger)

			for elementInListOfPrimes in cousinInitial:
				if ((elementInlistOfInteger % elementInListOfPrimes) == 0  or elementInlistOfInteger == 1):
					validation = False
				

			if validation :
				self.cousinNumbers.append(elementInlistOfInteger)
			
		if self.showInConsole:
			print(self.cousinNumbers)

		if plotSimples:
			plt.plot(self.cousinNumbers)		
			plt.show()
	

	
	def variationCounsinPrimes(self, showSimplesPlot=False, showInConsole=False):
		self.listVariation =[]
		
		before = None
		for currentCousinNumber in self.cousinNumbers:
			if self.cousinNumbers.index(currentCousinNumber) == 0:
				before = currentCousinNumber
				continue
			
			variation = currentCousinNumber - before
			
			self.listVariation.append(variation)

			before = currentCousinNumber
		
		if showSimplesPlot:
			plt.plot(self.listVariation)
			plt.show()
		if showInConsole:
			print(self.listVariation)

		

counsinGenerator = GeneratorCounsinPrimes()
counsinGenerator.analysisP1rocessOfCounainPrimes()
counsinGenerator.variationCounsinPrimes(showSimplesPlot=True)
print(counsinGenerator.cousinNumbers)
