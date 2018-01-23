#!/bin/env python

'''
This script simply crops and rotates the input numpy arrays,
and outputs them as images for QC. These ideas are all also
written into the modeling algorithm script.
'''

# deps
import numpy as np
import glob
import scipy.misc

# folder names
in1 = '../dat/fold_dyke_fault_model/*'
in2 = '../dat/fault_dyke_fold_model/*'
in3 = '../dat/gbasin_simplified_model/*'

out = '../dat/clean_imgs/'

# initialize
idx = 1

'''
# all files in first folder
for name in glob.glob(in1):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]

	# flip
	pic = np.transpose(pic)

	# write out
	scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1


# all files in second folder
for name in glob.glob(in2):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]

	# write out
	scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1
'''

# all files in third folder
for name in glob.glob(in3):
	# read
	pic = np.load(name)

	# crop
	pic = pic[:200, :200]

	# flip
	pic = np.transpose(pic)
	pic = np.flip(pic, axis=0)

	# write out
	scipy.misc.imsave(''.join((out, str(idx), '.jpg')), pic)

	# count
	idx += 1


