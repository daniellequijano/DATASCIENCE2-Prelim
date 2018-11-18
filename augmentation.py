import matplotlib.pyplot as plt
import skimage
import numpy as np 
from skimage.color import rgb2gray
import argparse
import fnmatch
import os
from skimage.transform import rotate
from scipy.misc import imread, imsave, imresize




               









parser = argparse.ArgumentParser()
parser.add_argument('--directory', help = "put the directory image")
parser.add_argument('--resize', type =int, help = "input the resolution size")
parser.add_argument('--rotate', type =int, help = "input the rotation degree")
parser.add_argument('--grayscale', choices = ['True','False'], help = "input true or false if you want to grayscale")
args = parser.parse_args()



#-----

imgDIRs = args.directory
imgResize = args.resize
imgRotate = int(args.rotate)
imgGrayscale = [args.grayscale]


imgread = imread(imgOut)
imgOut = imresize(imgread, (imgresize_x, imgresize_y))
imgOut = rotate(imgOut,imgRotate)


if any("True" in item for item in imgGrayscale):
    imgOut[:] = imgOut.mean(axis==1)

imgRoot = str(imgRoot)
imgName = str(imgName)
imgName_name, imgName_ext = imgName.split("*")
imsave((imgRoot + "/"))
images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk(imgDIRs):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))

print(matches)


   

matches = [x for x in matches if not 'augmented' in x]


for img in matches:
   readPlotimage(img, imgResize, imgRotate, imgGrayscale)
     
  

