#!/usr/bin/python
import os
import string
import commands
import sys
import math
VUL = './201617_vul.txt'
#FUNCS = './specint_image_lifetime.txt'
#MAP = './specint_funcmapcve.txt'
#FUNCS = './httperf_image_lifetime.txt'
#MAP = './httperf_funcmapcve.txt'
#FUNCS = './bonnie_image_lifetime.txt'
#MAP = './bonnie_funcmapcve.txt'
#FUNCS = './lamp_image_lifetime.txt'
#MAP = './lamp_funcmapcve.txt'
FUNCS = './nfs_image_lifetime.txt'
MAP = './nfs_funcmapcve.txt'

#def rdmsg():
#	fmsg = open(, 'r')
#	midFile=open(SYS_TMP,'w')
#	lines = fmsg.readlines()
#	for line in lines:
#		tmp_list = (line.strip('\n')).split(' syscall entry:')	
#		midFile.write(tmp_list[1] + ' \n' )
#		#print tmp_list[1]
#		#tmp_tmp_line = ''.join(tmp_list[1:])
#		#tmp_line = tmp_tmp_line.split('/*')[0]	
#		#for c in tmp_line:
#		#	index = -1
#		#	#if not(c in tmp_format):
#		#	if c in tmp_format:
#		#		index = tmp_line.index(c);
#		#		format_line = 'sys_' + tmp_line[:index] + ' ' + tmp_line[index:].strip() + '\n' 
#		#		midFile.write(format_line)
#		#		break 
#
#	midFile.close()
#	fmsg.close()
#def readhdr():
#	f = open(SYS_HDR, 'r')
#	midFile=open(SYS_MID,'w')
#	lines = f.readlines()
#	#tmp_format = '_abcdefghijklmnopqrstuvwxyz012345789'
#	tmp_format = '\t '	
#	for line in lines:
#		#print line 
#		if '__NR__' in line:
#			tmp_list = (line.strip('\n')).split('__NR__')	
#			tmp_tmp_line = ''.join(tmp_list[1:])
#			tmp_line = tmp_tmp_line.split('/*')[0]	
#			#print tmp_line
#			for c in tmp_line:
#				index = -1
#				#if not(c in tmp_format):
#				if c in tmp_format:
#					index = tmp_line.index(c);
#					format_line = 'sys_' + tmp_line[:index] + ' ' + tmp_line[index:].strip() + '\n' 
#					midFile.write(format_line)
#					break 
#		elif '__NR_' in line:
#			tmp_list = (line.strip('\n')).split('__NR_')	
#			tmp_tmp_line = ''.join(tmp_list[1:])
#			tmp_line = tmp_tmp_line.split('/*')[0]	
#			#print tmp_line
#			for c in tmp_line:
#				index = -1
#				#if not(c in tmp_format):
#				if c in tmp_format:
#					index = tmp_line.index(c);
#					format_line = 'sys_' + tmp_line[:index] + ' ' + tmp_line[index:].strip() + '\n'
#					midFile.write(format_line)
#					break 
#			#midFile=open('./'+'sys_num'+'.txt','w')
#			#midFile.write(content)
#
#	midFile.close()
#	f.close()

def imagehandle():
	ffunc = open(FUNCS,'r')
	lfunc = ffunc.readlines()
	fmap = open(MAP,'w')
	for line_func in lfunc:
		list_line_func = line_func.split(' ')
		strfunc = ''.join(list_line_func[5])
		if not('_' in strfunc.strip('\n')):
			continue 
		fvul = open(VUL, 'r')
		lvul = fvul.readlines()
		for line_vul in lvul:
			if ('The ' + strfunc.strip('\n') + ' function') in line_vul:
				list_line_vul = line_vul.split('\t')
				fmap.write(line_func.strip('\n') + ' ' + list_line_vul[1] + '\n')	
				#print (line_func.strip('\n') + ' ' + list_line_vul[1])	
				#break
		fvul.close()

	fmap.close()
	ffunc.close()
	
	#ffin = open(SYS_FIN,'w')
	#ret = 0	
	#fmid = open(SYS_MID,'r')
	#lmid = fmid.readlines()
	#
	#for line_mid in lmid:
	#	forig = open(SYS_ORIG, 'r')
	#	lorig = forig.readlines()
	#	for line_orig in lorig:
	#		list_orig = line_orig.split(' ')
	#		#tmp_line = ''.join(list_orig[2])
	#		if list_orig[2].strip('\n') in line_mid:
	#			#print list_orig
	#		#ffin.write(line_orig.strip('\n') + ' ' + list_mid[1])	
	#			ret = 1	
	#			break
	#	#if ret == 0:
	#	#	#print line_mid
	#	#else:
	#	#	ret = 0	
	#	forig.close()

	#ffin.close()
	#fmid.close()
#rdmsg()
#readhdr()
imagehandle()

