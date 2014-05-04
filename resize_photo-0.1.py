#-*-coding=utf-8-*-
from PIL import Image
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool

def getPhoto(foldername):
	if os.path.isdir(foldername):
		print foldername
		m=[]
		global PHOTOSTYLE
		for files in os.listdir(foldername):
			file_path=os.path.join(foldername,files)
			if os.path.isfile(file_path):
				if (os.path.splitext(file_path)[1]).lower() in PHOTOSTYLE:
					m.append(file_path)
		z=tuple(m)
		return z
		
def resize(filename):
	global usize
	photo=Image.open(filename)
	if photo.size[0]>int(usize[0]):
		h=int(int(usize[0])*int(photo.size[1])/int(photo.size[0]))
		p=photo.resize((int(usize[0]),h),Image.BILINEAR)
		p.save(filename)
		print filename,'======Resize Success.======'

PHOTOSTYLE=['.jpg','.jpeg']

print '''
	This software is use to resize all photos, if you want resize photos, just only copy to the folder which you need, select which size you want, and the software will resize all photos in this folder and include all folders under this folder. 
	Please choose the resize style:
	1.800x600
	2.1024x768
	3.2048x1536
'''

PHOTOSIZE=['800X600','1024X960','2048X1920']
while True:
	x=raw_input('please select:')	
	if x in ['1','2','3']:
		break

if x =='1':
	usize=[800,600]
elif x=='2':
	usize=[1024,768]
elif x=='3':
	usize=[2048,1536]
	
print usize
rootpath=os.path.dirname(os.path.abspath(sys.argv[0]))
print rootpath
if os.path.isdir(rootpath):
	for dirpath,dirname,filenames in os.walk(rootpath):
		x=getPhoto(dirpath)
		pool=ThreadPool(8)
		results=pool.map(resize,x)
		pool.close()
		pool.join()
