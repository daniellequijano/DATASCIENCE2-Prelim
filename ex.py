import fnmatch
import os
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument('--directory', help = "put the directory image")
parser.add_argument('--resize', type =int, help = "input the resolution size")
parser.add_argument('--rotate', help = "input the rotation degree")
parser.add_argument('--grayscale', choices = ['True','False'], help = "input true or false if you want to grayscale")
args = parser.parse_args()
currentFrame = 1


images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

imgDIRs = args.directory
imgResize = args.resize
imgRotate = int(args.rotate)
imgGrayscale = [args.grayscale]
for root, dirnames, filenames in os.walk(imgDIRs):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
            print(matches)

matches = [x for x in matches if not 'augmented' in x]


for img in matches:
    readPlotimage(img, imgResize, imgRotate, imgGrayscale)
