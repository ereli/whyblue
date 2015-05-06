import os
import shutil
from sys import argv
import urllib2
import urlparse
import download
input_filename = argv[1]
folder = argv[2]
print argv



		#if filename[1][""] os.path.isfile(path+i)
	#file = urllib2.urlopen(url)
	#print(parsed_url.path)
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

for line in open(input_filename):
	#download(line)
	q.enqueue(download.download, line, folder)


#output = open('test.mp3','wb')

#output.write(mp3file.read())

#output.close()



#files = os.listdir(path)
#for i in files:
	#test if folder exits, if exists, move file,
#	if os.path.exists(path+i[0:3]) is True and os.path.isfile(path+i) is True :
#		shutil.move(path+i, path+i[0:3]+"/"+i)
	#print os.path.exists(path+i[0:3])
#	else:
#		if os.path.isfile(path+i) is True:
#			os.makedirs(path+i[0:3])
#			shutil.move(path+i, path+i[0:3]+"/"+i)

	# if folder doesn't exits, create folder, then move file.

#
#os.path.exists(path)