
# coding: utf-8

# inspired by this so answer http://stackoverflow.com/a/3244061/1265980
import struct
import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy as np

def main_color(filename):

	NUM_CLUSTERS = 8

	#print 'reading image'
	
	im = Image.open(filename)


	#im = im.resize((150, 150))	  # optional, to reduce time
	im = im.convert("RGB") # it's necessary  to convert to RGBA from RGBA in order to remove the redundant alpha channel.
	ar = scipy.misc.fromimage(im)
	shape = ar.shape

	ar = ar.reshape(scipy.product(shape[:2]), shape[2])

	# finding clusters
	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
	
	vecs, dist = scipy.cluster.vq.vq(ar, codes)		 # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))	# count occurrences
	
	index_max = scipy.argmax(counts)					# find most frequent

	#peak = codes[index_max] # this is the top color
	peak_arr = []


	#colour = ''.join(chr(c) for c in peak).encode('hex')
	#print 'most frequent is %s (#%s)' % (peak, colour)

	# sometimes we only get 3 colors, so we check i order to not to print the top 4 if there are only 3.
	# we then return the top 4 colors. 

	if len(counts) >= 4:
		ind = np.argpartition(counts, -4)[-4:]
		ind = ind[np.argsort(counts[ind])]
		ind = ind.tolist()
	
		for i in range(0,len(ind)):
			peak_arr.append(''.join(chr(c) for c in codes[i]).encode('hex')) # appending the colors into a list
	else:
		length = len(counts)
		ind = np.argpartition(counts, -length)[-length:]
		ind = ind[np.argsort(counts[ind])]
		ind = ind.tolist()
	
		for i in range(0,len(ind)):
			peak_arr.append(''.join(chr(c) for c in codes[i]).encode('hex'))
	return peak_arr # returing the top 4 colors list

