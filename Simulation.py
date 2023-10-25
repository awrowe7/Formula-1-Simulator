# Runs the actual simulations given all the input and classes

# -------------------------------------------------------------------------------

# IMPORTS
from Teams import AlphaRomeo, AlphaTauri, Alpine, AstonMartin, Ferrari, Haas, McLaren, Mercedes, RedBull, Williams
from Teams.Constructors import Constructor, displayName
import Formula1
import picture
import random

# -------------------------------------------------------------------------------

# RESULT DISPLAYING
def resultDisplay(speedResults, nameResults, script):
	"""
 	First creates a backdrop board, similar to that seen on TV during real races, for the results to be printed on. Then displays each team ranked based on speed. 
 	"""
	# Score Grid 
	picture.set_fill_color('grey')
	picture.draw_filled_rectangle(950, 10, 140, 345)
	picture.draw_text(954, 20, script, 16)

	# Results
	names = list(nameResults)
	y = 60
	nameNum = 0
	for team in speedResults:
		picture.set_fill_color(team.getColor())
		picture.draw_filled_circle(965, y, 10)
		name = displayName(names[nameNum])
		picture.draw_text(985, y - 5, name, 13)
		y += 30
		nameNum += 1
	picture.display()

# -------------------------------------------------------------------------------

# QUALIFYING SPEEDS
def qualifierSimulation(constructor, circuit, weather, strat, tyresList, realistic=False):
	"""
 	Runs the simulation for the qualifier results, which affect the starting grid of the race. Rather skewed, as are the real qualifiers *eye roll*. Starts by changing the weather if the user chose 'Realistic'. It then initializes each constructor before getting the speed of each team. Then sorts those results into two dictionaries, one using the class as the key and the other using the team name. Finally, it passes thse two lists into the display function for them to be shown on screen to the user. 
 	"""
	# Checking Realistic Weather Condition and Re-Randomizing The Weather For The Qualifier Day
	if realistic == True:
		qWeather = Formula1.specificWeather(circuit)
	elif realistic == False:
		qWeather = weather

	# Qualifying Tyre Setup
	if weather == 'drizzly' or weather == 'rainy':
		tyre = 'wet'
	elif weather == 'clear' or weather == 'cloudy': 
		tyre = 'soft'
	
	# Team Setups
	alpharomeoClass = AlphaRomeo.AlphaRomeo()
	alphatauriClass = AlphaTauri.AlphaTauri()
	alpineClass = Alpine.Alpine()
	astonmartinClass = AstonMartin.AstonMartin()
	ferrariClass = Ferrari.Ferrari()
	haasClass = Haas.Haas()
	mclarenClass = McLaren.McLaren()
	mercedesClass = Mercedes.Mercedes()
	redbullClass = RedBull.RedBull()
	williamsClass  = Williams.Williams()
	classConstructs = (alpharomeoClass, alphatauriClass, alpineClass, astonmartinClass, ferrariClass, haasClass, mclarenClass, mercedesClass, redbullClass, williamsClass)
	
	# Team Speeds
	speedQualifyingResults = dict()
	nameQualifyingResults = dict()
	x = 0
	teams = list(Constructor.dictOfConstructors)
	for team in classConstructs:
		teamName = teams[x]
		pit = False
		team.getSpeed(circuit, qWeather, tyre, pit)
		speedQualifyingResults[team] = team.speed
		nameQualifyingResults[teamName] = team.speed
		x += 1
		
	# Sorting The Speeds
	speedQualifyingResults = dict(sorted(speedQualifyingResults.items(), key=lambda x: x[1], reverse=True))
	nameQualifyingResults = dict(sorted(nameQualifyingResults.items(), key=lambda x: x[1], reverse=True))
	
	# Display
	script = "Qualifying Results"
	resultDisplay(speedQualifyingResults, nameQualifyingResults, script)

	# User Results
	listForUserTeamRanking = list(nameQualifyingResults)
	for i in range(len(listForUserTeamRanking)):
		if listForUserTeamRanking[i] == constructor:
			return classConstructs, speedQualifyingResults, nameQualifyingResults, i, qWeather
		else:
			continue

# -------------------------------------------------------------------------------

# RACE
def race(classConstructs, classQualifyingResults, nameQualifyingResults, constructor, circuit, weather, tyresList):
	"""
 	Runs the simulations for the race. Iterates for each of the laps of the race, displaying the lap number, calculating the tyre wear, and adjusting the speed and positioning. As well, asks the user for input of pitstops for tyre changes. Finally, it returns the final order of the race for congratualiting, or pitying, the user accordingly. 
	"""	
	
	# Seperating User Team and Other Teams
	listOfConstructsStrings = ('alpharomeoClass', 'alphatauriClass', 'alpineClass', 'astonmartinClass', 'ferrariClass', 'haasClass', 'mclarenClass', 'mercedesClass', 'redbullClass', 'williamsClass')
	notUserTeams = list()
	for i in range(len(listOfConstructsStrings)):
		if listOfConstructsStrings[i][0:7] != constructor[0:7]:
			notUserTeams.append(classConstructs[i])
		else:
			userTeam = classConstructs[i]
	
	# Bot Strat Setup	
	for team in notUserTeams:
		team.setStrat(weather, circuit)
	# User Strat Setup
	userTeam.setStrat(weather, circuit, tyresList)

	# Starting Grid Positions and Names
	classPositions = list(classQualifyingResults)
	namePositions = list(nameQualifyingResults)
	for i in range(len(classPositions)):
		name = namePositions[i]
		classPositions[i].name(name)

		position = i + 1
		classPositions[i].getPlace(position)

	# Basic Team Setup
	for team in classConstructs:
		strat = team.strat
		tyre = strat[0]
		team.tyreWear(tyre, 0)

	# Position Sorting
	def positionSorting(classConstructs):
		"""
		Sorts all the team positions into variable classPositions. Called often as positions change
		"""
		positions = dict()
		for teams in classConstructs:
			positions[teams] = teams.place
			positions = dict(sorted(positions.items(), key=lambda x: x[1]))
		classPositions = list(positions)
		return classPositions

	# ------------------------------------------------------------------------------
	#  ################################## Laps ####################################
	# ------------------------------------------------------------------------------
	laps = 0
	while laps != 6:
		
		# Handling and Tyre Wear Settings
		for team in classConstructs:
			strat = team.strat
			tyre = strat[0]
			team.getHandling(circuit, weather, tyre)

		# Total Performance
		positionsDictForPassing = dict()
		for team in classPositions:
			pit = False
			strat = team.strat
			tyre = strat[0]
			team.getSpeed(circuit, weather, tyre, pit)
			performance = team.speed + team.handling
			positionsDictForPassing[team] = performance
		
		# Passing
		for i in range(len(positionsDictForPassing)):
			if i != (len(classPositions) - 1):
				# getting the teams
				teamOne = classPositions[i]
				teamTwo = classPositions[i + 1]
				
				if positionsDictForPassing[teamOne] < positionsDictForPassing[teamTwo]:
					# old positions
					teamOnePos = classPositions[i].place
					teamTwoPos = classPositions[i + 1].place
					# switch positions
					classPositions[i].getPlace(teamTwoPos)
					classPositions[i + 1].getPlace(teamOnePos)
					# sort positions
					classPositions = positionSorting(classConstructs)
				else:
					continue
			else:
				classPositions[i].getPlace(len(classPositions))
				classPositions = positionSorting(classConstructs)

		# New Position Sorting
		classPositions = positionSorting(classConstructs)

		# Tyre Weardown 
		laps += 1
		for team in classConstructs:
			strat = team.strat
			tyre = strat[0]
			team.tyreWear(tyre, laps)
		
		# Position Loss
		def losingPositions(currentTeam, classPositions, positionsLost, classConstructs):
			"""
	 		Handles times a team loses a position to the team behind it. Intakes the team losing position(s), the current positions list, how many positions the team is losing, and the list of all the class variable names. Uses recurssion to drop the losing team back in the order of racers. Also continously sorts the current positions
			"""
			if positionsLost == 1:
				position = currentTeam.place
				if position != 10:
					gainingTeam = classPositions[position]
					currentTeam.getPlace(position + 1)
					gainingTeam.getPlace(position)
					classPositions = positionSorting(classConstructs)
					return classPositions
				else:
					classPositions = positionSorting(classConstructs)
					return classPositions
			elif positionsLost > 1:
				position = currentTeam.place
				if position != 10:
					gainingTeam = classPositions[position]
					currentTeam.getPlace(position + 1)
					gainingTeam.getPlace(position)
					classPositions = positionSorting(classConstructs)
					classPositions = losingPositions(currentTeam, classPositions, positionsLost - 1, classConstructs)
					return classPositions
				else:
					classPositions = positionSorting(classConstructs)
					return classPositions

		# Bot Pit Stops (w/speed change)
		if laps != 6:
			for team in notUserTeams:
				if team.tyreCondition == 0:
					# strat
					currentStrat = team.strat
					newStrat = currentStrat[1:]
					team.setStrat(weather, circuit, newStrat)
					# speed and wear
					strat = team.strat
					tyre = strat[0]
					pit = True
					team.getSpeed(circuit, weather, tyre, pit)
					team.tyreWear(tyre, 0)
					# position loss
					positionsLost = random.randint(1, 3)
					classPositions = losingPositions(team, classPositions, positionsLost, classConstructs)

		# Pre User Input Display
		namePositions = list()
		for i in classPositions:
			namePositions.append(i.name)
		if laps == 6:
			string = 'Final Results'
		elif laps < 6:
			string = 'Lap ' + str(laps)
		resultDisplay(classPositions, namePositions, string)
		
		# User Input Pit Stops
		if laps != 6:
			lifeLeft = userTeam.tyreCondition
			Formula1.space()
			Formula1.divider()
			Formula1.space()
			print('After that lap your tyres have', str(lifeLeft), 'lap left in them.')
			done = False
			while done != True:
				pitstop = str(input('Would you like to pit (yes or no)? ')).strip().lower().replace(' ', '')

				# yes
				if pitstop == 'yes':
					# has pitstops left
					if len(userTeam.strat) > 1: 
						currentStrat = userTeam.strat
						newStrat = currentStrat[1:]
						userTeam.setStrat(weather, circuit, newStrat)
						strat = userTeam.strat
						tyre = strat[0]
						pit = True
						userTeam.getSpeed(circuit, weather, tyre, pit)
						userTeam.tyreWear(tyre, 0)
						if team.place != 10:
							positionsLost = random.randint(1, 3)
							classPositions = losingPositions(userTeam, classPositions, positionsLost, classConstructs)
							done = True
						else:
							done = True
					# has no pitstops left 
					elif len(userTeam.strat) == 1:
						Formula1.space()
						print("Sorry, you're all out of tyres to switch to.")
						done = True
				# no 
				elif pitstop == 'no':
					done = True
				# invalid input 
				else:
					Formula1.space()
					print("Sorry, that's not a valid input.")
					done = False
		
		# Position Sorting
		classPositions = positionSorting(classConstructs)

		# Results Menu Title
		if laps == 6:
			string = 'Final Results'
		elif laps < 6:
			string = 'After Lap ' + str(laps)
			
		# Displaying Positions
		namePositions = list()
		for i in classPositions:
			namePositions.append(i.name)

		# Post User Input Display
		resultDisplay(classPositions, namePositions, string)

		# Next Lap Input
		if laps != 6:
			input("To play the next lap hit 'enter' ")

	# Returned List of Final Positions 
	return namePositions
