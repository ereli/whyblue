from PIL import Image
from sys import argv 
import json
filename = argv[1]
im = Image.open(filename)
print(json.dumps(im.histogram()))
