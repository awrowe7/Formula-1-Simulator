# Defines Ferrari

# IMPORTS
import random
from Teams import Constructors

class Ferrari():
	"""Defines Ferrari"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': -2,
		'cota': 3,
		'redbullring': 7,
		'marinabay': 9
		}
	weatherPerformance = {
		'clear': 12,
		'cloudy': 8,
		'drizzly': -8, 
		'rainy': -15
	}
	tyrePerformance =	{
		'hard': -4,
		'medium': 6,
		'soft': 13,
		'intermediate': 8,
		'wet': 13
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (255, 40, 0)

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
			initialSpeed = random.randint(150, 190)

			# performance values
			CP = Ferrari.circuitPerformance[circuit]
			W = Ferrari.weatherPerformance[weather]
			T = Ferrari.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = Ferrari.circuitPerformance[circuit]
			W = Ferrari.weatherPerformance[weather]
			T = Ferrari.tyrePerformance[tyre]

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
