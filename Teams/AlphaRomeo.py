# Defines the Alpha Romeo classes

# IMPORTS
import random
from Teams import Constructors

# -------------------------------------------------------------------------------

class AlphaRomeo():
	"""Defines Alpha Romeo"""

	# Class Variables 
	circuitPerformance = {
		'melbourne': 3,
		'cota': 9,
		'redbullring': 9,
		'marinabay': -3
		}
	weatherPerformance = {
		'clear': 2,
		'cloudy': 8,
		'drizzly': -9, 
		'rainy': -17
	}
	tyrePerformance =	{
		'hard': -4,
		'medium': 1,
		'soft': 7,
		'intermediate': 7,
		'wet': 14
	}

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		self.color = (164,33,52)

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
				strat = Constructors.Constructor.drizzleStrat
			elif weather == 'rainy':
				strat = Constructors.Constructor.wetStrat
			else:
				strat = random.choice(Constructors.Constructor.dryStrats)
			self.strat = strat
		else:
			self.strat = strat

	# -------------------------------------------------------------------------------

	# Speed
	def getSpeed(self, circuit, weather, tyre, pit=False):
		if pit == False:
			# initial speed
			initialSpeed = random.randint(115, 160)

			# performance values
			CP = AlphaRomeo.circuitPerformance[circuit]
			W = AlphaRomeo.weatherPerformance[weather]
			T = AlphaRomeo.tyrePerformance[tyre]

			# final speed 
			self.rawSpeed = initialSpeed
			self.speed = initialSpeed + CP + W + T
			
		elif pit == True:
			# performance values
			CP = AlphaRomeo.circuitPerformance[circuit]
			W = AlphaRomeo.weatherPerformance[weather]
			T = AlphaRomeo.tyrePerformance[tyre]

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
