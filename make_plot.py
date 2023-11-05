import numpy as np
from  matplotlib import pyplot
import os
from astropy.io import fits
import glob
data = fits.getdata('/Users/bostroem/Desktop/images/hubble_img.fits')
col1 = data[20, :]
col2 = data[200, :]
col3 = data[800, :]
pyplot.figure()
pyplot.plot(np.arange(1024), col1)
mean = np.mean(col1)
pyplot.axhline(mean)
pyplot.legend(['Column 20', 'Mean'])
pyplot.title('Plot of Column 20 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.figure()
pyplot.plot(np.arange(1024), col2)
mean = np.mean(col2)
pyplot.axhline(mean)
pyplot.legend(['Column 200', 'Mean'])
pyplot.title('Plot of Column 200 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')
pyplot.figure()
pyplot.plot(np.arange(1024), col3)
mean = np.mean(col3)
pyplot.axhline(mean)
pyplot.legend(['Column 800', 'Mean'])
pyplot.title('Plot of Column 800 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity') 
<<<<<<< HEAD
pyplot.title('Practice')
=======
>>>>>>> 5e268c20d62b2b802d0eef97bd4bbe5ffb3a625a
