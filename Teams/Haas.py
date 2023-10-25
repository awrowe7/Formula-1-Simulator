# Defines Haas

import random
from Teams import Constructors 

class Haas():
	"""Defines Haas"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': 3,
		'cota': 7,
		'redbullring': 6,
		'marinabay': 6
		}
	weatherPerformance = {
		'clear': 10,
		'cloudy': 5,
		'drizzly': -14, 
		'rainy': -17
	}
	tyrePerformance =	{
		'hard': -5,
		'medium': 5,
		'soft': 8,
		'intermediate': 8,
		'wet': 11
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (249, 242, 242)

	# -------------------------------------------------------------------------------

	# Color
	def getColor(self):
		return (self.color)

	# -------------------------------------------------------------------------------

	# Name
	def name(self, name):
		self.name = name
		
	# -------------------------------------------------------------------------------

		# Set Strategy
	def setStrat(self, weather, circuit, strat='none'):
		if strat == 'none':
			if weather == 'drizzly':
				self.strat = Constructors.Constructor.drizzleStrat
			elif weather == 'rainy':
				self.strat = Constructors.Constructor.wetStrat
			else:
				self.strat = random.choice(Constructors.Constructor.dryStrats)
		else:
			self.strat = strat

	# -------------------------------------------------------------------------------

	# Speed
	def getSpeed(self, circuit, weather, tyre, pit=False):
		if pit == False:
			# initial speed
			initialSpeed = random.randint(110, 140)

			# performance values
			CP = Haas.circuitPerformance[circuit]
			W = Haas.weatherPerformance[weather]
			T = Haas.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = Haas.circuitPerformance[circuit]
			W = Haas.weatherPerformance[weather]
			T = Haas.tyrePerformance[tyre]

			# final speed
			self.speed = self.rawSpeed + CP + W + T

	# -------------------------------------------------------------------------------

	# Handling
	def getHandling(self, circuit, weather, tyre):
		originalTyreLife = Constructors.Constructor.tyreLife[tyre]
		currentCondition = self.tyreCondition
		self.handling = Constructors.remainingTyreLife(tyre, weather, originalTyreLife, currentCondition)
	
	# -------------------------------------------------------------------------------

	# Tyre Wear
	def tyreWear(self, tyre, laps):
		if laps == 0:
			self.tyreCondition = Constructors.Constructor.tyreLife[tyre] 
		else:
			tyreCondition = self.tyreCondition - 1
			self.tyreCondition = tyreCondition		
		
	# -------------------------------------------------------------------------------

	# Place
	def getPlace(self, pos):
		self.place = pos
