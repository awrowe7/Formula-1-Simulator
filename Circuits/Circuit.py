# Defines the circuit classes

# Image Sources:
# All images sourced from the formula1.com website 
# https://www.formula1.com/en/racing/2023.html

# IMPORTS
import picture

# -------------------------------------------------------------------------------

# CIRCUITS CLASS
class circuit():
	"""
 	Stores the list of acceptable circuit responses from the user
	"""
	# CIRUIT LIST
	listOfCircuits = (
		'melbourne',
		'cota',
		'redbullring',
		'marinabay'
	)

# -------------------------------------------------------------------------------

# IMAGE DISPLAYER
def imageDisplay(image):
	"""
 	Takes in the loaded image of a circuit and displays it to the user. Adds an additional 140 pixels to the right size of image to make space for the position board later. 
 	"""
	# Circuit Map
	width = picture.image_width(image)
	height = picture.image_height(image)
	picture.new_picture(width + 140, height)
	picture.draw_image(0, 0, image)

	# Display
	picture.display()

# -------------------------------------------------------------------------------

# IMAGE LOADER
def imageLoader(circuit):
	"""
 	Loads the images based on which circuit the user chose. Then passes that loaded image to the display function to be shown to the user. 
 	"""
	if circuit == 'melbourne':
		image = picture.load_image('Circuits/Melbourne.jpg')
		imageDisplay(image)
	elif circuit == 'cota':
		image = picture.load_image('Circuits/COTA.jpg')
		imageDisplay(image)
	elif circuit == 'redbullring':
		image = picture.load_image('Circuits/RedBullRing.jpg')
		imageDisplay(image)
	elif circuit == 'marinabay':
		image = picture.load_image('Circuits/MarinaBay.jpg')
		imageDisplay(image)