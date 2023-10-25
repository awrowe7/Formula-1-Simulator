# Defines the constructor lists and basic functions 

# -------------------------------------------------------------------------------

# TEAM ABREVIATION RETURNER
def displayName(team):
	"""
 	Returns the capitalized and spaced version of each constructor's name 
	"""
	return Constructor.dictOfConstructors[team]

# -------------------------------------------------------------------------------

# TYRE LIFE
def remainingTyreLife(tyre, weather, original, current):
	"""
 	Stores the handling value given the wear on the tyres. Differs based on the tyre that the team in question is using. Also takes into account if the proper tyre is being used given the weather, and if not punished the user accordingly 
	"""
	# hard tyre
	if tyre == 'hard':
		if weather == 'drizzly' or 'rainy':
			if original == current:
				return -50
			elif original - 1 == current:
				return -80
			elif original - 2 == current:
				return -110
			elif original - 3 == current:
				return -150
			elif original - 4 >= current:
				return -10000
		elif weather == 'clear':
			if original == current:
				return 0
			elif original - 1 == current:
				return -15
			elif original - 2 == current:
				return -30
			elif original - 3 == current:
				return -45
			elif original - 4 == current:
				return -60
			elif original - 4 > current:
				return -10000
		elif weather == 'cloudy':
			if original == current:
				return 0
			elif original - 1 == current:
				return -11
			elif original - 2 == current:
				return -22
			elif original - 3 == current:
				return -33
			elif original - 4 == current:
				return -44
			elif original - 4 > current:
				return -10000
				
	# medium tyre
	elif tyre == 'medium':
		if weather == 'drizzly' or 'rainy':
			if original == current:
				return -40
			elif original - 1 == current:
				return -65
			elif original - 2 == current:
				return -95
			elif original - 3 == current:
				return -115
			elif original - 4 >= current:
				return -10000
		elif weather == 'clear':
			if original == current:
				return 0
			elif original - 1 == current:
				return -10
			elif original - 2 == current:
				return -20
			elif original - 3 == current:
				return -30
			elif original - 3 > current:
				return -10000
		elif weather == 'cloudy':
			if original == current:
				return 0
			elif original - 1 == current:
				return -8
			elif original - 2 == current:
				return -16
			elif original - 3 == current:
				return -24
			elif original - 3 > current:
				return -10000
				
	# soft tyre
	elif tyre == 'soft':
		if weather == 'drizzly' or 'rainy':
			if original == current:
				return -30
			elif original - 1 == current:
				return -55
			elif original - 2 == current:
				return -85
			elif original - 2 > current:
				return -10000
		elif weather == 'clear':
			if original == current:
				return 0
			elif original - 1 == current:
				return -5
			elif original - 2 == current:
				return -10
			elif original - 2 > current:
				return -10000
		elif weather == 'cloudy':
			if original == current:
				return 0
			elif original - 1 == current:
				return -3
			elif original - 2 == current:
				return -6
			elif original - 2 > current:
				return -10000

	# intermediate tyre
	elif tyre == 'intermediate':
		if original == current:
			return 0
		elif original - 1 == current:
			return -7
		elif original - 2 == current:
			return -14
		elif original - 3 == current:
			return -21
		elif original - 3 > current:
			return -10000


	# wet tyre
	elif tyre == 'wet':
		if original == current:
			return 0
		elif original - 1 == current:
			return -5
		elif original - 2 == current:
			return -10
		elif original - 2 > current:
			return -10000
			
# -------------------------------------------------------------------------------

class Constructor():
	"""Defines the basics of most construtors"""

	# CLASS VARIABLES:
	
	# Constructors Input and Display Name
	dictOfConstructors = {
	'alpharomeo': 'Alpha Romeo', 
	'alphatauri': 'Alpha Tauri', 
	'alpine': 'Alpine', 
	'astonmartin': 'Aston Martin',
	'ferrari': 'Ferrari',
	'haas': 'Haas', 
	'mclaren': "McLaren", 
	'mercedes': 'Mercedes', 
	'redbull': 'RedBull', 
	'williams': 'Williams'
	}

	# Tyre Life
	tyreLife = {
	'hard': 4, 
	'medium': 3, 
	'soft': 2, 
	'intermediate': 3, 
	'wet': 2
	}
	
	# Tyre Strats
	dryStrats = (
	('soft', 'soft', 'soft'), 
	('soft', 'medium', 'soft'),
	('medium', 'medium'),
	('hard', 'soft'),
	('soft', 'hard'), 
	('medium', 'hard'),
	('hard', 'medium'),
	('hard', 'hard')
	)
	drizzleStrat = (('intermediate', 'intermediate'))
	wetStrat = (('wet', 'wet', 'wet'))

##################################################################################
# Below is a docstring for each of the constructor classes. All are virtually the same with only constructor specific things being different between them. 

### CONSTRUCTOR CLASSES DOCSTRINGS ###

# IMPORTS
"""
Imports all appropriate modules
"""

# -------------------------------------------------------------------------------

class constructor():
	"""Defines each constructor"""

	# Class Variables 
	"""
 	Used to store and call values specific to that constructor such as tyre performance
	"""

	# -------------------------------------------------------------------------------

	# Constructor
	def __init__(self):
		"""
		Stores the color of each constructor 
		"""

	# -------------------------------------------------------------------------------

	# Color
	def getColor(self):
		"""
		Returns the appropriate color of each constructor
		"""

	# -------------------------------------------------------------------------------

	# Name
	def name(self, name):
		"""
		Sets the display name of each constructor which will be presented to the user in the output window on the results board after the qualifier and each lap
		"""

	# -------------------------------------------------------------------------------

	# Set Strategy
	def setStrat(self, weather, circuit, strat='none'):
		"""
 		Sets the strategy for each constructor. Assumes each constructor will be opperated as a bot. If the constructor in question is the user's selected constructor, then it sets the stat equal to the strat the user chose. Otherwise, it calls a random strategy from a preset list of strategies
		"""

	# -------------------------------------------------------------------------------

	# Speed
	def getSpeed(self, circuit, weather, tyre, pit=False):
		"""
		Sets the speed given a random range of speeds for each constructor (roughly realistic). Includes the ability to call this function in a pitstop, which prevents the function from changing the speed value to a different number and instead just recalculates using the new tyres. 
 		"""
			
	# -------------------------------------------------------------------------------

	# Handling
	def getHandling(self, circuit, weather, tyre):
		"""
		Calls the handling function in the Constructor file given the tyres being used's health and the original health of those tyres. 
		"""
	
	# -------------------------------------------------------------------------------

	# Tyre Wear
	def tyreWear(self, tyre, laps):
		"""
		Decreases the tyre health on each lap. This value will be called for the handling 
		"""
		
	# -------------------------------------------------------------------------------

	# Place
	def getPlace(self, pos):
		"""
		Sets the current racing position of each team which will be used to sort them as their positions change
		"""
