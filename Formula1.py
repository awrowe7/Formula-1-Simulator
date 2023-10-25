# This file is the main code running the menus of the simulation. It houses the menu and presents the user with the final outcome. 

# -------------------------------------------------------------------------------

# IMPORTS
import random
import Teams.Constructors
import Circuits.Circuit
import Weather.weather
import Simulation

# -------------------------------------------------------------------------------

# SPACE PRINTER 
def space():
	"""
 	... pretty obvious!
 	"""
	print('')

# -------------------------------------------------------------------------------

# DIVIDER PRINTER
def divider():
	"""
 	Creates a divider aimed at making shell text/menus easier on the eyes and better sorted
 	"""
	print('---------------------------------------------------------------------')

# -------------------------------------------------------------------------------

# CONSTRUCTOR MENU
def constructorMenu():
	"""
 	Creates the menu for selecting a favorite constructor to play as. Also calls the joke statement to make fun of the user's favorite team. Finally, it returns the constructor of choice in string form
 	"""
	# Constructor Picker 
	constructorDone = False
	while (not constructorDone):
		try:
			# input
			selectedConstructor = str(input("What constructor do you like most?: ")).strip().lower().replace(' ', '')

			# checking validity 
			if selectedConstructor == 'help':
				constructorHelp()
				constructorDone = False
			elif selectedConstructor not in Teams.Constructors.Constructor.dictOfConstructors:
				raise ValueError
			else:
				constructor = selectedConstructor
				constructorDone = True
		except ValueError:
			space()
			print("Sorry, that's not a valid constructor name. Maybe check your spelling, though you should know how to spell you favoirte team's name!!")
			space()

	# Joke Statement
	constructorJoke(constructor)

	# Returned Constructor 
	return constructor

# -------------------------------------------------------------------------------

# CONSTRUCTOR HELPER
def constructorHelp():
	"""
 	Prints out the list of all possible constructors the user could choose in the case that they are new to F1. Called when 'help' is typed as constructor choice
	"""
	space()
	print('Possible constructors are:')
	for i in Teams.Constructors.Constructor.dictOfConstructors:
		print(Teams.Constructors.Constructor.dictOfConstructors[i])
	space()

# -------------------------------------------------------------------------------

# CONSTRUCTOR JOKES 
def constructorJoke(constructor):
	"""
 	Just a little playful roasting of the user's favorite teams. 
 	"""
	if constructor == 'alpharomeo':
		print("You sure? You can still go back and change your answer. No one seriously cheers for Alpha Romeo.")
	elif constructor == 'alphatauri':
		print('What is it about mediocrity that draws you to Alpha Tauri?')
	elif constructor == 'alpine':
		print("Ohhhhhh you must HATE Alonso this season! You know, there's still time to jump ship and become an Aston Martin fan.")
	elif constructor == 'astonmartin':
		print("This season is the most action you've seen in a while isn't it!")
	elif constructor == 'ferrari':
		print("Are you off your delusion meds?")
	elif constructor == 'haas':
		print('Are you Russian? No? Just enjoy supporting them?')
	elif constructor == 'mclaren':
		print('Ah the brave 6 stop strategists of Bahrain. Great pick!')
	elif constructor == 'mercedes':
		print("Really? Still? I'm sorry...")
	elif constructor == 'redbull':
		print('Ahhh, so you have a god complex.')
	elif constructor == 'williams':
		print("It's been 26 years since y'all were good. Time to pick a new favorite!")
	space()
	divider()
	space()

# -------------------------------------------------------------------------------

# CIRCUIT MENU
def circuitMenu():
	"""
 	Creates the menu for selecting a the circuit to race on. It then load an image of that circuit. Finally, it returns the circuit of choice in string form
 	"""
	print('Okay, next we need to pick a circuit to race on. Here are your options:')
	space()
	print('1. Melbourne - Australia')
	print('2. Circuit of the Americas - Texas, USA')
	print('3. Red Bull Ring - Austria')
	print('4. Marina Bay - Singapore')
	print('5. Pick for me!')
	space()
	circuitDone = False
	while (not circuitDone):
		try:
			# input
			selectedCircuit = int(input('Please enter the number of the circuit you would like?: '))
			
			# checking validity 
			if selectedCircuit > 5 or selectedCircuit < 1:
				raise ValueError
			else:
				circuitDone = True
		except ValueError:
			space()
			print("Sorry, that's not a valid circuit number. Please try again.")
			space()

	# Circuit Identifier 
	if selectedCircuit == 1:
		circuit = Circuits.Circuit.circuit.listOfCircuits[0]
	elif selectedCircuit == 2:
		circuit = Circuits.Circuit.circuit.listOfCircuits[1]
	elif selectedCircuit == 3:
		circuit = Circuits.Circuit.circuit.listOfCircuits[2]
	elif selectedCircuit == 4:
		circuit = Circuits.Circuit.circuit.listOfCircuits[3]
	elif selectedCircuit == 5:
		circuit = random.choice(Circuits.Circuit.circuit.listOfCircuits)

	# Menu Formatting
	space()
	divider()
	space()
	
	# Load Circuit
	Circuits.Circuit.imageLoader(circuit)

	# Returned Circuit
	return circuit

# -------------------------------------------------------------------------------

# WEATHER MENU
def weatherMenu(circuit):
	"""
 Creates the menu for selecting the weather conditions. It then load an image of the weather in one of the top two corners depending on the circuit. Finally, it returns the weather in string form
 	"""
	# Menu
	print("Now we need to establish the weather. We suggest selecting 'Realistic' as it'll alter the weather according to the actual liklihood of certain weather in the location you have chosen.")
	space()
	print('Clear')
	print('Cloudy')
	print('Drizzly')
	print('Rainy')
	print('Realistic')
	space()

	# Input
	weatherDone = False
	while (not weatherDone):
		try:
			# input
			selectedWeather = str(input('Please enter the weather you would like (pick realistic!): ')).strip().lower().replace(' ', '')
			
			# checking validity 
			if selectedWeather not in Weather.weather.weather.weatherList:
				raise ValueError
			else:
				weather = selectedWeather
				weatherDone = True
		except ValueError:
			space()
			print("Sorry, that's not a valid weather setting. Please try again.")
			space()

	# Realistic Definer 
	realistic = False
	if weather == 'realistic':
		realistic = True
		weather = specificWeather(circuit)	
	
	# Image Loader
	Weather.weather.imageLoader(weather, circuit)

	# Returned Weather
	return realistic, weather

# -------------------------------------------------------------------------------

# REALISTIC WEATHER SETTER
def specificWeather(circuit):
	"""
 	If the user chooses 'Realistic' weather, this function intakes the circuit and calculates the weather based on certain probabilities for each circuit. Returns this value as the weather 
	"""
	value = random.randint(1, 10)
	if circuit == 'melbourne':
		if value <= 3:
			weather = 'rainy'
		elif value <= 7:
			weather = 'cloudy'
		else:
			weather = 'drizzly'
	elif circuit == 'cota':
		if value <= 8:
			weather = 'clear'
		else:
			weather = 'cloudy'
	elif circuit == 'marinabay':
		if value <= 9:
			weather = 'clear'
		else:
			weather = 'cloudy'
	elif circuit == 'redbullring':
		if value <= 3:
			weather = 'drizzly'
		elif value <= 4:
			weather = 'rainy'
		else:
			weather = 'clear'
	return weather

# -------------------------------------------------------------------------------

# TRANSITION STATEMENT
def transition(circuit, weather):
	"""
 	Bridges the gap between setting up the race and actually making race decisions. Prints a simple statement that references the weather conditions and the circuit the user chose
	"""

	circuitName = circuitNameForPresentation(circuit)

	# Weather Word
	adjective = weatherWord(weather)
	
	space()
	print("Awesome! Now let's get ready for",  adjective ,"race", circuitName + "!")
	space()
	divider()
	space()

# -------------------------------------------------------------------------------

# Circuit Full Name Maker
def circuitNameForPresentation(circuit):
	"""
 	Returns the capitalized and spaced version of each ciruit's name
 	"""
	if circuit == 'melbourne':
		circuitNameForPresentation = "in Melbourne"
	elif circuit == 'cota':
		circuitNameForPresentation = "at COTA"
	elif circuit == 'redbullring':
		circuitNameForPresentation = "at The Red Bull Ring"
	elif circuit == 'marinabay':
		circuitNameForPresentation = "in Marina Bay"
	return circuitNameForPresentation

# -------------------------------------------------------------------------------

# WEATHER ADJECTIVE 
def weatherWord(weather):
	"""
	Returns an apt adjective to describe the race given the weather
 	"""
	if weather == 'clear':
		adjective = 'a beautiful'
		return adjective
	elif weather == 'cloudy':
		adjective = 'an overcast'
		return adjective
	elif weather == 'drizzly':
		adjective = 'a damp'
		return adjective
	elif weather == 'rainy':
		adjective = 'a wet'
		return adjective

# -------------------------------------------------------------------------------

# Strategy Choice
def strategyMenu():
	"""
	Creates the menu for selecting the stratgy the user would like to use in the race. Returns the strat in string form
 	"""
	# Intro and Options
	print("In Formula 1 racing there are 5 types of tyre compounds you can race on. These different compounds serve different purposes and can be utilized accordingly. This is a part of your 'racing strategy'. In an effort of keeping with parc ferme rules, as best we can at least, we will have you select a strategy before qualifying that you will start the race with. Let's decide which strategy you want to use!")
	space()
	print('Strategy 1: A one stop strategy, meaning you will only make one pit stop.')
	print('Strategy 2: A two stop strategy, meaning you will make two pit stops.')
	space()

	# User Input
	Circuitdone = False
	while Circuitdone != True:
		try:
			# input
			strat = str(input('Which number strategy do you want to start off with?: '))

			# checking validity 
			if strat == '1':
				Circuitdone = True
				strat = 'onestop'	
			elif strat == '2':
				Circuitdone = True
				strat = 'twostop'
			else:
				raise ValueError
		except ValueError:
			space()
			print("Sorry, that's not a valid strategy. Make sure you're only inputing the number!")
			space()

	# Menu Formatting
	space()
	divider()
	space()
	
	# Returned Strategy
	return strat

# -------------------------------------------------------------------------------

# TYRES MENU
def tyresMenu(strat, weather):
	"""
	Creates the menu that explains tyre compounds and their impact on racing. Then allows the user to select their tyre compounds given their strategy choice. Returns the tyres in a list 
 	"""
	# Explanation
	print("Now, tyre compounds each have their own advantages and disadvantages. Here's the quick and dirty:")
	print("Hard - Long lasting but low grip")
	print('Medium - Not as durable but a bit grippier')
	print("Soft - Extremely grippy but doesn't last long at all")
	print("Intermediate - Good for drizzle. Doesn't last extremely long but far better than wet tyres (only available if it's raining)")
	print("Wet - The only viable option when it's raining. Overall trash in all other situations (only available if it's raining)")
	space()
	print('Note: You will not be allowed to select Intermediate or Wet tires if the weather is not drizzling or raining.')
	space()
	
	# Variable Setup
	tyreList = list()
	numberWords = ('First', 'Second', 'Third')
	possibleTyres = ('hard', 'medium', 'soft', 'intermediate', 'wet')
	if strat == 'onestop':
		num = 2
	elif strat == 'twostop':
		num = 3

	# Input
	def tyrePicking(num, numC, numberWords, weather):
		# Base Case
		if numC <= 1: 
			tyre = input(numberWords[num - 1] + ' tyre compound: ').strip().lower().replace(' ', '')
			if weather == 'drizzly' or weather == 'rainy':
				if tyre not in possibleTyres:
					space()
					print('Check your spelling.')
					space()
					tyrePicking(num, numC, numberWords, weather)
				else:
					tyreList.append(tyre)
			elif weather == 'clear' or weather == 'cloudy':
				if tyre not in possibleTyres[:3]:
					space()
					print("Make sure you're not picking rain tyres!")
					space()
					tyrePicking(num, numC, numberWords, weather)
				else:
					tyreList.append(tyre)

		# Higher Cases
		elif numC > 1:
			wordNumber = num - numC
			tyre = input(numberWords[wordNumber] + ' tyre compound: ').strip().lower().replace(' ', '')
			if weather == 'drizzly' or weather == 'rainy':
				if tyre not in possibleTyres:
					space()
					print('Check your spelling.')
					space()
					tyrePicking(num, numC, numberWords, weather)
				else:
					tyreList.append(tyre) 
					tyrePicking(num, numC - 1, numberWords, weather)
			elif weather == 'clear' or weather == 'cloudy':
				if tyre not in possibleTyres[:3]:
					space()
					print("Make sure you're not picking rain tyres!")
					space()
					tyrePicking(num, numC, numberWords, weather)
				else:
					tyreList.append(tyre)
					tyrePicking(num, numC - 1, numberWords, weather)
	tyrePicking(num, num, numberWords, weather)

	# Menu Formatting 
	space()
	divider()
	space()
	
	# Returned List of Tyre Compounds
	return tyreList

# -------------------------------------------------------------------------------

# Qualifyer Recap String
def qualifyingRecap(qualifyingPosition, circuit, qWeather):
	"""
	Intakes the Circuit, thw Weather, and the Qualifying Position of the user's selected team 
	"""
	divider()
	space()
	positionString = positionWording(qualifyingPosition)
	circuit = circuitNameForPresentation(circuit)
	print('It was a', qWeather, 'qualifyer', circuit + '.', 'Your team placed', str(qualifyingPosition) + positionString + '!')
	space()
	
# -------------------------------------------------------------------------------

# Position Number Wording
def positionWording(position):
	"""
 	Returns the proper suffix(not sure if that's the right word) given the place that the user came in. 
	"""
	if position == 1:
		return 'st'
	elif position == 2:
		return 'nd'
	elif position == 3:
		return 'rd'
	else:
		return 'th'

# -------------------------------------------------------------------------------

# ENDING POSITION
def endingPositionGetter(endingPosition, constructor):
	"""
 	Returns the place the user came in which will be used to display the user's ending position after the race. Returns and integer
	"""
	place = 0
	positionNames = list(endingPosition)
	for team in positionNames:
		place += 1
		if team[0:7] == constructor[0:7]:
			return place

# -------------------------------------------------------------------------------

# POINTS VALUE AND STRING
def pointsString(place):
	"""
 	Returns a unique string for all points scoring positions. Also returns a generic "you finished outside the points" string. This string is displayed to the user after the race
	"""
	if place == 1:
		return "Wow! That's 25 championship points! Excellent job, unless you just picked RedBull to get an easy win."
	elif place == 2:
		return "In the words of the wise Scott Rowe (my dad), 'second place is just first loser'. In any case, that's 18 championship points. Coulda been 25... but you were too slow."
	elif place == 3:
		return "Third place ain't bad at all, still got a podium. 12 championship points for you."
	elif place == 4:
		return "Could have been worse. Brush it off and get a podium next time. For now though, you've won 6 championship points."
	elif place == 5:
		return "Soooo close to being outside the points. Lucky you, here's 1 championship point. Better than none I guess."
	else:
		return "Unfortunately you finished outside the points. Please play again and hopefully your luck will improve. Or, if you're desperate for a win you could just pick RedBull."

#################################################################################

### MENUS ###
def menus():
	"""
 	Creates the main menu of the simulator and then calls all the subsequent menus needed
 	"""
	# Menu Header
	print('Welcome to the Formula 1 Simulator')
	space()
	print("Your goal will be to make the best decisions possible to lead your team to victory. After reading this message, you will be prompted to first pick a team to represent, a circuit to race on, and the weather you'll be racing in. After that, you will be able to decide what startegy (amount of pitstops) and what tyres you would like to use. You'll witness the race one lap at a time with the ability to make pitstop decisions as you go. Finally, you'll be met with your finishing position and the number of points you scored. Goodluck! AND DON'T JUST PICK REDBULL EVERYTIME TO BOOST YOUR F1 EGO!")
	space()
	print("Let's get started by picking your favorite constructor! If you're new to F1 then type 'help' for a list of contructors!")
	space()

	# -------------------------------------------------------------------------------

	# Constructor
	constructor = constructorMenu()

	# -------------------------------------------------------------------------------

	# Circuit  
	circuit = circuitMenu()
	
	# -------------------------------------------------------------------------------
	
	# Weather
	realistic, weather = weatherMenu(circuit)
	
	# -------------------------------------------------------------------------------

	# Transition 
	transition(circuit, weather)

	# -------------------------------------------------------------------------------

	# Strategy Menu 
	strat = strategyMenu()

	# -------------------------------------------------------------------------------

	# Tyres Menu
	tyresList = tyresMenu(strat, weather)

	# -------------------------------------------------------------------------------

	# Qualifier Simulation Runner
	print("Awesome! Now we will begin the simulation by running a qualifier. For this, everyone will be running on soft tyres. If you have personally chosen the weather then the qualifying will be raced in that weather condition. However, if you have opted for the 'Realistic' weather option then the weather probabilities will be recalculated for the qualifier day. Therefore, the weather may be different for the qualifyer than for the race day. Your qualifying tyres will be adjusted automatically. Please direct your attention to the circuit map for the starting grid lineup.")
	space()
	classConstructs, classQualifyingResults, nameQualifyingResults, place, qWeather = Simulation.qualifierSimulation(constructor, circuit, weather, strat, tyresList, realistic)
	qualifyingPosition = place + 1

	# -------------------------------------------------------------------------------

	# Qualifer Recap
	qualifyingRecap(qualifyingPosition, circuit, qWeather)

	# -------------------------------------------------------------------------------

	# RACE PREP
	divider()
	space()
	print("You'll be starting P" + str(qualifyingPosition) + ', on', tyresList[0], "tyres. The weather for race day will be", str(weather) + ". When you're ready to start the race, please hit 'enter'!")
	input('')
	print("It's lights out and away we go!!")

	# -------------------------------------------------------------------------------

	# RACE
	endingPosition = Simulation.race(classConstructs, classQualifyingResults, nameQualifyingResults, constructor, circuit, weather, tyresList)

	# -------------------------------------------------------------------------------

	# ENDING MESSAGE
	space()
	divider()
	space()
	place = endingPositionGetter(endingPosition, constructor)
	placeString = positionWording(place)
	points = pointsString(place)
	print('Your team finished in', str(place) + str(placeString) + '! ' + str(points))
	input('')

#################################################################################

# MAIN 
def main():
	"""
 	Basic main functions which calls the Menus funtions to begin the simulation
	"""
	menus()
if __name__ == '__main__':
	main()
	