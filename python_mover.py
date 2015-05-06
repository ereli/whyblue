import os
import shutil
from sys import argv
path = argv[1]
print argv
files = os.listdir(path)
for i in files:
	#test if folder exits, if exists, move file,
	if os.path.exists(path+i[0:3]) is True and os.path.isfile(path+i) is True :
		shutil.move(path+i, path+i[0:3]+"/"+i)
	#print os.path.exists(path+i[0:3])
	else:
		if os.path.isfile(path+i) is True:
			os.makedirs(path+i[0:3])
			shutil.move(path+i, path+i[0:3]+"/"+i)

	# if folder doesn't exits, create folder, then move file.

#
#os.path.exists(path)