from pymongo import MongoClient
from urlparse import urlparse
import color_extractor as ce
import os.path
import urllib, cStringIO



def work(num_req):

	client = MongoClient()
	db = client.test
	collection = db.playstore_2015_4

	img_folder = '/home/ereli/projects/play-images/new/'
	batch_size = 0
#.batch_size(30)
	for data in collection.find({'top_4_colors' : { '$exists': False}}, no_cursor_timeout=True).limit(num_req):
		if len(data) != 0:
			batch_size = 1
			print "url: "+data['CoverImgUrl']
			o = urlparse(data['CoverImgUrl'])
			print("filename: "+o.path)
			full_path = (img_folder+o.path[1:4]+"/"+o.path).strip()
			print "full path: "+full_path
			print os.path.isfile(full_path)
			try:
				print("doc id: "+str(data['_id']))
				print("path "+str(full_path))
				if os.path.isfile(full_path) is True:
					try:
						top_4_colors = (ce.main_color(full_path))
						print top_4_colors
						collection.update({'_id' :  data['_id']}, {'$set': {'top_4_colors': top_4_colors }})			
					except Exception, e:
						raise

				else:
					pass
					#try:
					#	 file_web = cStringIO.StringIO(urllib.urlopen(data['CoverImgUrl']).read())
					#	 top_4_colors = (ce.main_color(file_web))
					#	 print top_4_colors
					#	 collection.update({'_id' :  data['_id']}, {'$set': {'top_4_colors': top_4_colors }})
					#except Exception, e:
					#	raise




				#a = collection.find({'_id' : data['_id']})
				#for i in a:
				#	print i


			except Exception, e:
				raise
			else:
				pass
			finally:
				pass
	return batch_size






from multiprocessing import Pool


if __name__ == '__main__':
#	print(work())


    pool = Pool(processes=8)              # start 4 worker processes
    state = 1
    while state == 1:
    	result = pool.apply_async(work, [2])    # evaluate "f(10)" asynchronously
    	
    	res = result.get(timeout=25)
    	print res
    	state = res
    
    

 