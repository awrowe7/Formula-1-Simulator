# Defines AlphaTauri

import random
from Teams import Constructors

class AlphaTauri():
	"""Defines AlphaTauri"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': -3,
		'cota': 5,
		'redbullring': 13,
		'marinabay': 0
		}
	weatherPerformance = {
		'clear': 3,
		'cloudy': 5,
		'drizzly': -13, 
		'rainy': -16
	}
	tyrePerformance =	{
		'hard': -3,
		'medium': 5,
		'soft': 11,
		'intermediate': 5,
		'wet': 2
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (32, 57, 76)

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
			initialSpeed = random.randint(120, 150)

			# performance values
			CP = AlphaTauri.circuitPerformance[circuit]
			W = AlphaTauri.weatherPerformance[weather]
			T = AlphaTauri.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = AlphaTauri.circuitPerformance[circuit]
			W = AlphaTauri.weatherPerformance[weather]
			T = AlphaTauri.tyrePerformance[tyre]

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
