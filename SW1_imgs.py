
#SW1-1

#imports
import skimage
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import exposure
from skimage import feature 

from skimage.filters import gaussian, roberts, sobel, scharr, prewitt
from scipy.ndimage import convolve
from skimage import io


#read image web
#url = 'http://i.imgur.com/DojuJP4.png'
#img = io.imread(url)


#read image locally
img = imread("color-input.jpg")
#convert to Gray
grayImage = rgb2gray(img)
binaryImage = np.where(grayImage > np.mean(grayImage),1.0,0.0)

edges1 = roberts(binaryImage)
edges2 = feature.canny(binaryImage)


fig, axes = plt.subplots(ncols=2, figsize=(20,5))
ax = axes.ravel()

ax[0] = plt.subplot(1,3,1)
ax[1] = plt.subplot(1,3,2)




                   
ax[0].imshow(img,cmap = "gray")
ax[0].set_title('original')
ax[0].axis('off')

ax[1].imshow(grayImage,cmap = "gray")
ax[1].set_title('grayscale')
ax[1].axis('off')



fig.tight_layout()
plt.show()



#SW1-2
#imports
import skimage
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import exposure
from skimage import feature 
import skimage
import numpy as np
from skimage.io import imread
from skimage import exposure
import matplotlib.pyplot as plt

from skimage.filters import gaussian, roberts, sobel, scharr, prewitt
from scipy.ndimage import convolve

from skimage import io


#read image web
#url = 'http://i.imgur.com/DojuJP4.png'
#color_img = io.imread(url)

#read image
color_img = imread("color-input.jpg")


#Inverse
inv_img = ~color_img
#inv_img = -color_img + 255 #same effect

plt.imshow(inv_img)
plt.show()


#SW1-3

#RESIZE

from skimage import data
from skimage.transform import resize
import skimage
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import exposure
from skimage import feature 
import skimage
import numpy as np
from skimage.io import imread
from skimage import exposure
import matplotlib.pyplot as plt

from skimage.filters import gaussian, roberts, sobel, scharr, prewitt
from scipy.ndimage import convolve


from skimage import io


#read image web
#url = 'http://i.imgur.com/DojuJP4.png'
#img = io.imread(url)
#read image
img = imread("color-input.jpg")


resizedimg = resize(img, (700, 700))

plt.imshow(resizedimg)
plt.show()



#SW1-4

from skimage.transform import rotate
from skimage import data
from skimage.transform import resize
import skimage
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import exposure
from skimage import feature 
import skimage
import numpy as np
from skimage.io import imread
from skimage import exposure
import matplotlib.pyplot as plt

from skimage import io


#read image web
#url = 'http://i.imgur.com/DojuJP4.png'
#img = io.imread(url)

#read image
img = imread("color-input.jpg")


rotatedimg = rotate(img, 45)

plt.imshow(rotatedimg)
plt.show()
