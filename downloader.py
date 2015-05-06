import os
import shutil
from sys import argv
import urllib2
import urlparse
input_filename = argv[1]
folder = argv[2]
print argv

def download(url):
	parsed_url = urlparse.urlparse(url)
	#print url
	filename = os.path.split(parsed_url.path)
	try:
		#
		full_path = (folder+filename[1][0:3]+"/"+filename[1]).strip()
		#print full_path
		if os.path.exists(full_path) is False:
			if os.path.exists(folder+filename[1][0:3]) is False:		
				os.path.makedirs(folder+filename[1][0:3])
		print("file doesn't exists, downloading...")
		output = open(full_path,'wb')
		file = urllib2.urlopen(url)
		output.write(file.read())
		output.close()
		print("file written")
		#print full_path
	except:
		raise

		#if filename[1][""] os.path.isfile(path+i)
	#file = urllib2.urlopen(url)
	#print(parsed_url.path)

for line in open(input_filename):
    download(line)



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