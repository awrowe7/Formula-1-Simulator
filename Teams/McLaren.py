# Defines McLaren

import random
from Teams import Constructors 

class McLaren():
	"""Defines McLaren"""
	
	# Class Variables 
	circuitPerformance = {
		'melbourne': -4,
		'cota': 5,
		'redbullring': 2,
		'marinabay': 0
		}
	weatherPerformance = {
		'clear': 4,
		'cloudy': 9,
		'drizzly': -7, 
		'rainy': -11
	}
	tyrePerformance =	{
		'hard': -5,
		'medium': 7,
		'soft': 13,
		'intermediate': 9,
		'wet': 9
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (255, 128, 0)

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
			initialSpeed = random.randint(125, 160)

			# performance values
			CP = McLaren.circuitPerformance[circuit]
			W = McLaren.weatherPerformance[weather]
			T = McLaren.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = McLaren.circuitPerformance[circuit]
			W = McLaren.weatherPerformance[weather]
			T = McLaren.tyrePerformance[tyre]

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
