# Defines Mercedes

import random
from Teams import Constructors 

class Mercedes():
	"""Defines Mercedes"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': 5,
		'cota': 2,
		'redbullring': 7,
		'marinabay': -2
		}
	weatherPerformance = {
		'clear': 8,
		'cloudy': 7,
		'drizzly': -10, 
		'rainy': -18
	}
	tyrePerformance =	{
		'hard': -2,
		'medium': 8,
		'soft': 18,
		'intermediate': 13,
		'wet': 17
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (0, 161, 155)

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
			initialSpeed = random.randint(140, 180)

			# performance values
			CP = Mercedes.circuitPerformance[circuit]
			W = Mercedes.weatherPerformance[weather]
			T = Mercedes.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = Mercedes.circuitPerformance[circuit]
			W = Mercedes.weatherPerformance[weather]
			T = Mercedes.tyrePerformance[tyre]

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
