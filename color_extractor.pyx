
# coding: utf-8

# In[ ]:

import struct
import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy as np
def main_color(filename):

	NUM_CLUSTERS = 8

	#print 'reading image'
	#filename = '/home/ereli/projects/play-images/ZZPdzvlpK9r_Df9C3M7j1rNRi7hhHRvPhlklJ3lfi5jk86Jd1s0Y5wcQ1QgbVaAP5Q=w300.png'
	im = Image.open(filename)


	#im = im.resize((150, 150))	  # optional, to reduce time
	im = im.convert("RGB")
	ar = scipy.misc.fromimage(im)
	shape = ar.shape

	ar = ar.reshape(scipy.product(shape[:2]), shape[2])

	#print 'finding clusters'
	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
	#print 'cluster centres:\n', codes

	vecs, dist = scipy.cluster.vq.vq(ar, codes)		 # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))	# count occurrences
	#print counts
	index_max = scipy.argmax(counts)					# find most frequent

	peak = codes[index_max]
	peak_arr = []


	colour = ''.join(chr(c) for c in peak).encode('hex')
	#print 'most frequent is %s (#%s)' % (peak, colour)
	print len(counts)
	if len(counts) >= 4:
		ind = np.argpartition(counts, -4)[-4:]
		ind = ind[np.argsort(counts[ind])]
		ind = ind.tolist()
	#print ind
		for i in range(0,len(ind)):
		#print i
		#peak_arr.append(ind[i])
			peak_arr.append(''.join(chr(c) for c in codes[i]).encode('hex'))
	else:
		length = len(counts)
		ind = np.argpartition(counts, -length)[-length:]
		ind = ind[np.argsort(counts[ind])]
		ind = ind.tolist()
	#print ind
		for i in range(0,len(ind)):
		#print i
		#peak_arr.append(ind[i])
			peak_arr.append(''.join(chr(c) for c in codes[i]).encode('hex'))



	#print peak_arr
	return peak_arr

