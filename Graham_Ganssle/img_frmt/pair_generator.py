#!/bin/env python

'''
This script takes clean seismic images, adds noise, and sorts them
into folders specified in the pix2pix framework. The step after
this is to use the pix2pix script "combine_A_and_B.py".
'''

# deps
import numpy as np
import matplotlib.image as img
import glob
import scipy.misc

# folder specs
inputs = '../dat/output_seismic/*'
outclean = '../dat/pairs/A/train/'
outnoisy = '../dat/pairs/B/train/'

# initialize
idx = 1

# add noise and write out image pairs
for name in glob.glob(inputs):
	# read in image
	pic = img.imread(name)
	pic = np.asarray(pic)

	# define white noise section
	errPerc = np.random.rand()
	noise = np.random.rand(pic.shape[0], pic.shape[1])

	# add noise to image
	noisy = pic + noise * np.max(pic) * errPerc

	# write out images
	scipy.misc.imsave(''.join((outclean, str(idx), '.jpg')), pic)
	scipy.misc.imsave(''.join((outnoisy, str(idx), '.jpg')), noisy)

	# count
	idx += 1



