# Defines Red Bull

import random
from Teams import Constructors 

# RED BULL CONSTRUCTOR
class RedBull():
	"""Defines Red Bull"""

	# Class Variables
	circuitPerformance = {
		'melbourne': 11,
		'cota': 6,
		'redbullring': 18,
		'marinabay': -5
		}
	weatherPerformance = {
		'clear': 3,
		'cloudy': 3,
		'drizzly': -14, 
		'rainy': -20
	}
	tyrePerformance =	{
		'hard': -8,
		'medium': 3,
		'soft': 10,
		'intermediate': 8,
		'wet': 14
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (35, 50, 106)

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
			initialSpeed = random.randint(160, 200)

			# performance values
			CP = RedBull.circuitPerformance[circuit]
			W = RedBull.weatherPerformance[weather]
			T = RedBull.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = RedBull.circuitPerformance[circuit]
			W = RedBull.weatherPerformance[weather]
			T = RedBull.tyrePerformance[tyre]

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
