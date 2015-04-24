#!/usr/bin/python2.7
import color_extractor as ce
from sys import argv

path = argv[1]
import glob
list_of_files =  glob.glob(path+'*')
for i in list_of_files:
	print(ce.main_color(i))
