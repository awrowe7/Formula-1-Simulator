# Defines Weather 

# Image Sources:
# All images are cropped versions of on image found on sketchappsources.com 
# The image was originally created by Yaya Red
# https://www.sketchappsources.com/free-source/1313-weather-icons-sketch-freebie-resource.html

# IMPORT 
import picture

# -------------------------------------------------------------------------------

# WEATHER CLASS
class weather():
	"""
 	Stores the acceptable weather responses from the user
	"""
	# WEATHER LIST
	weatherList = {
		'clear',
		'cloudy',
		'drizzly', 
		'rainy',
		'realistic'
	}

# -------------------------------------------------------------------------------

# IMAGE DISPLAYER
def imageDisplay(image, circuit):
	"""
 	Displays the loaded image in the corner of the screen. Which corner is dependant on which circuit the user has chosen to race on as the images have different available space
 	"""
	# Width Setter
	width = picture.image_width(image)

	# Corner Picker 
	if circuit == 'melbourne':
		picture.draw_image(960 - (width + 30), 0, image)
		picture.display()
	else:
		picture.draw_image(0, 0, image)
		picture.display()

# -------------------------------------------------------------------------------

# Image Loader
def imageLoader(weather, circuit):
	"""
 	Loads the image of the corresponding weather condition. Then calls the display function to display that image. 
 	"""
	if weather == 'clear':
		image = picture.load_image('Weather/Clear.png')
		imageDisplay(image, circuit)
	elif weather == 'cloudy':
		image = picture.load_image('Weather/Cloudy.png')
		imageDisplay(image, circuit)
	elif weather == 'drizzly':
		image = picture.load_image('Weather/Drizzle.png')
		imageDisplay(image, circuit)
	elif weather == 'rainy':
		image = picture.load_image('Weather/Rain.png')
		imageDisplay(image, circuit)
		