"""
We have now reached a point where we can learn about many fun things! Let's start by learning about picture cropping.
"""


#first we have to install pillow

#Do you remember how we covered imports? First we are going to import pillow. 
from PIL import Image
#

#this is how we pull up an image
image1 = Image.open('im1.jpg')
#in order to show it on the screen we do
image1.show()
#in order to save the image as a png insteag of jpg do
image1.save('pup1.png')

#What if you want to convert several images into pngs from jpg?
	#we will need to loop over each image

#we will need to 
import os
#make a loop that will loop through every image in the directory
for f in os.listdir('.'):
	if f.endswtich('.jpg'):
		#test to make sure it will print each one
		print(f)
		#opens the image
		i = Image.open(f)
		#in order to name the file the same name
		fn, fext = os.path.splitext(f)
		#saves images with same names
		i.save('pngs/{}.png'.format(fn))
		
#let's test the code above. Open it and check to make sure we have new names for each one.

#have you ever needed to resixe your photos when you try to post them or for an assignment? OFten times you get an error saying the image is too big or the image crops one some of the things in the photo. How do we make a fixed max size for all the photos? Let's try

#first we need to forloop through the images.

from PIL import Image
import os
size_300 = (300,300)
#make a loop that will loop through every image in the directory
for f in os.listdir('.'):
        if f.endswtich('.jpg'):
                #test to make sure it will print each one
                print(f)
                #opens the image
                i = Image.open(f)
                #in order to name the file the same name
                fn, fext = os.path.splitext(f)
                #changes size into a small photo
		i.thumbnail(size_300)
		
		#saves imaes into forlder 300
                i.save('300/{}_300'.format(fn,fext))

#mastercheck: Now let's try to imagine that your work requires you to decrease the images into 300x300 and into 700x700 how would you do this?

#so what are the benefits of using this instead of doing it all by hand?
#you could have 100+ photos and it woudl take a really long time to do it all by hand

#now let's do some projects and remember how to google!
	#rotate your images
	#blurr your images
	#think of your own
	

