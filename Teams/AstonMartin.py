# Defines Aston Martin

import random
from Teams import Constructors

class AstonMartin():
	"""Defines Aston Martin"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': 7,
		'cota': 5,
		'redbullring': 9,
		'marinabay': 6
		}
	weatherPerformance = {
		'clear': 12,
		'cloudy': 8,
		'drizzly': -10, 
		'rainy': -17
	}
	tyrePerformance =	{
		'hard': -6,
		'medium': 3,
		'soft': 8,
		'intermediate': 14,
		'wet': 19
	}

	# -------------------------------------------------------------------------------		
	
	# Constructor
	def __init__(self):
		self.color = (0, 36, 32)

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
			initialSpeed = random.randint(160, 180)

			# performance values
			CP = AstonMartin.circuitPerformance[circuit]
			W = AstonMartin.weatherPerformance[weather]
			T = AstonMartin.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = AstonMartin.circuitPerformance[circuit]
			W = AstonMartin.weatherPerformance[weather]
			T = AstonMartin.tyrePerformance[tyre]

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
