#Quijano, Danielle Mark O. SW1_5
#DATASCIENCE2

#argumentLine: run this in terminal
#python3 img_augmentation.py -l /Users/Danielle/Desktop/TIP-FILES/DATASCIENCE2/DataImages -d 200x200 -g True -r 45



import numpy as np
from scipy.misc import imread, imresize, imsave
from scipy.ndimage import rotate
from scipy.misc import face
import matplotlib.pyplot as plt
import os
import fnmatch
import scipy.misc
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--location", required=True,
	help="(LOCATION)directory to the input image folder")
ap.add_argument("-d", "--dimension",
	default=0,
	help="(RESIZE)enter dimensions separated by 'x'. Example: 200x300")
ap.add_argument("-g", "--grayscale",
	default="False",
    choices=['True','False'],
	help="(GRAYSCALE)Specify 'True' or 'False' if grayscaled or not")
ap.add_argument("-r", "--rotate",
	default=0,
	help="(ROTATE)input the degree to be rotated")
args = ap.parse_args()




#PARAMETER
location_images=args.location
dim=args.dimension
if dim != 0:
    dim=dim.split('x')
    x_dim=int(dim[0])
    y_dim=int(dim[1])
gray=args.grayscale
gray2=str(gray.lower())
gray3="true"
if gray2==gray3:
    gray=True
else:
    gray=False

rot=int(args.rotate)






#get all image addresses
extensions_list = ['.jpg', '.jpeg', '.png', '.tif', '.tiff']
images=[]
temp=[]
for root, dirs, files in os.walk(location_images):
    for extension in extensions_list:
        for file in files:
            if file.endswith(extension):
                images=images+[os.path.join(root, file)]





for image in images:
    
    img=imread(image)
    #RESIZE the image
    aug_img=imresize(img,(x_dim,y_dim))

    #GRAYSCALE the image
    if gray==True:
        x,y,z=aug_img.shape
        aug_img[:]=aug_img.mean(axis=-1,keepdims=1)

    #ROTATE the image
    aug_img=rotate(aug_img,rot)
    
    head, sep, tail = image.partition('.')
    temp=head+'-Augmented_image.jpg'
    scipy.misc.imsave(temp, aug_img)
    
print("Success! :)")


