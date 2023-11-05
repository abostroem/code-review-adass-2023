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
avg1 = np.mean(col1)
pyplot.axhline(avg1)
pyplot.legend(['Column 20', 'Mean'])
pyplot.title('Plot of Column 20 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')

pyplot.figure()
pyplot.plot(np.arange(1024), col2)
avg2 = np.mean(col2)
pyplot.axhline(avg2)
pyplot.legend(['Column 200', 'Mean'])
pyplot.title('Plot of Column 200 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity')

pyplot.figure()
pyplot.plot(np.arange(1024), col3)
avg3 = np.mean(col3)
pyplot.axhline(avg3)
pyplot.legend(['Column 800', 'Mean'])
pyplot.title('Plot of Column 800 Values and Mean')
pyplot.xlabel('Pixels')
pyplot.ylabel('Intensity') 
