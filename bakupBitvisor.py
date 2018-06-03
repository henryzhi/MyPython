#!/usr/bin/python
import os
import time

sourceFiles = ['/home/wqj/guardian/crypt','/home/wqj/guardian/core','/home/wqj/guardian/kbguard',
'/home/wqj/guardian/driver','/home/wqj/guardian/netguard','/home/wqj/guardian/cmdshell',
'/home/wqj/guardian/attestation', '/home/wqj/guardian/keylogger', '/home/wqj/guardian/test']
destdir = '/home/MyBitvisorBakup/bitvisor1.1/'

today = destdir + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")


if not os.path.exists(destdir):
    os.mkdir(destdir)
    print "Mkdir %s successfully." % destdir
    
comment = raw_input("Enter a comment:\n")

if len(comment) == 0:
    myBakupDir = today + now
else:
    myBakupDir = today + now + '_' + \
                comment.replace(' ', '_')

if not os.path.exists(myBakupDir):
    os.mkdir(myBakupDir)
    print "Mkdir %s successfully." % myBakupDir

clean_command = "make clean"
if os.system(clean_command) == 0:
    print "make clean first"

cp_command = "cp -rf %s %s" % (' '.join(sourceFiles),myBakupDir)

if os.system(cp_command) == 0:
    print "bakup succesfully"
else:
    print "bakup failed"

zip_file = myBakupDir + ".zip"
zip_command = "zip -qr %s %s" % (zip_file,myBakupDir)
if os.system(zip_command) == 0:
	print "zip successfully"
else:
	print "zip failed"
