from PIL import Image
import os
import sys
import time
import getpass

username = getpass.getuser()
from sets import Set
watchdir = "/Users/%s/Pictures/Photo Booth Library/Pictures" % username
files = Set(os.listdir(watchdir))
locs = [(0,0), (1120,0), (0,760), (1120,760)]
while True:
	newfiles = Set(os.listdir(watchdir)).difference(files)
	if len(newfiles) > 0:
		print newfiles
		if len(newfiles) == 4:
			print "Found New Files %s" % newfiles
			big = Image.new("RGB", (1080 * 2 + 40, 720 *2 + 40), "white")
			i = 0
			for file in newfiles:

				timp = Image.open("%s/%s" % (watchdir, file))
				big.paste(timp, locs[i])
				i += 1
			outfile = "/Users/%s/booth/%s.jpg" % (username, time.time())
			big.save(outfile, "jpeg")
			os.popen("lp -o landscape -o fit-to-page -o media=4x6 %s" % outfile)
			files = Set(os.listdir(watchdir)) 
	time.sleep(1)

