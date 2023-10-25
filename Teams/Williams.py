# Defines Williams

import random
from Teams import Constructors 

class Williams():
	"""Defines Williams"""
	
	# Class Variables
	circuitPerformance = {
		'melbourne': 5,
		'cota': -1,
		'redbullring': 3,
		'marinabay': -2
		}
	weatherPerformance = {
		'clear': 3,
		'cloudy': 3,
		'drizzly': -9, 
		'rainy': -12
	}
	tyrePerformance =	{
		'hard': 0,
		'medium': 6,
		'soft': 9,
		'intermediate': 8,
		'wet': 7
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (0, 163, 224)

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
			initialSpeed = random.randint(115, 140)

			# performance values
			CP = Williams.circuitPerformance[circuit]
			W = Williams.weatherPerformance[weather]
			T = Williams.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = Williams.circuitPerformance[circuit]
			W = Williams.weatherPerformance[weather]
			T = Williams.tyrePerformance[tyre]

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
