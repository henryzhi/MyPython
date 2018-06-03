#!/usr/bin/python
import os
import string
import commands
import sys
import math

OBJ_DIR = "./OBJ"
OBJDUMP = "objdump -hxt "
def readmod():
	num = 0 
	with open('./modlist.db', 'r') as f:
		while True:
			line1 = f.readline().strip('\n')
			if line1:
				content = commands.getoutput(OBJDUMP + line1)
				tmp_str = str(num)	
				midFile=open(OBJ_DIR+'/'+tmp_str+'.txt','w') 	
				midFile.write(content)
				midFile.close()
				num = num + 1	
			else:
				break

	f.close()

def objhandle():
	files = os.listdir(OBJ_DIR)
	sum_file = 0
	sum_code_page = 0
	for line2 in files:
		print line2
		sum_file += 1	
		lnum = 0
		llist = [] 
		with open(OBJ_DIR+'/'+line2, 'r') as f:
			for line3 in f.readlines():
				lnum += 1	
				if 'READONLY, CODE' in line3:
					llist.append(lnum)	
		f.close()
		lnum = 0
		with open(OBJ_DIR+'/'+line2, 'r') as f:
			code_page = 0	
			for line4 in f.readlines():
				lnum += 1
				tmp_lnum = lnum + 1	
				tmp_llist = [] 
				if tmp_lnum in llist:
					tmp_llist =  line4.split(' ')
					num_switch = 1 
					for element in tmp_llist:
						if element.isalnum():
							if num_switch == 1:	
								num_switch = 0
								continue 
							
							else:
								#print element.encode('hex')
								print int(element,16)
								print hex(int(element, 16))
								print '---\t'
								tmp = int(element,16)
								code_page += int(math.ceil(float(tmp)/4096))	
								break 
			print code_page	
			sum_code_page += code_page	
			#print line4
			print '\n-----------------------\n'
		f.close()
	print sum_file
	print sum_code_page
#print int(math.ceil(float(A)/B))
readmod()
objhandle()

