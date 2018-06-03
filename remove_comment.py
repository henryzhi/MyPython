#!/usr/bin/python

import os
import os.path
import string

def enumAllMatchFiles(root,files):
    extType = ['.c','.h','.s']
    try:
        ls=os.listdir(root)
    except:
        print 'access deny'
    else:
        for l in ls:
            temp=os.path.join(root,l)        
            if os.path.isdir(temp):
                enumAllMatchFiles(temp,files)
            else:
                (fname,ext) = os.path.splitext(temp)
                if ext in extType:
                    files.append(temp)
                    
def clearDeclaration(fname):
    fp = open(fname)
    fultxt = fp.readlines();
    cond1 = False
    cond2 = False
    curLineNo = 0
    startLineNo = 0
    endLineNo = 0
    for line in fultxt:
        if string.find(line,'/*') != -1:
            cond1 = True
            startLineNo = curLineNo
        if string.find(line,'*/') != -1:
            endLineNo = curLineNo
            if cond2:
                break    
            cond1 = False       
        if  cond1 and string.find(line,"* Copyright (c) 2007, 2008 University of Tsukuba") != -1:
            cond2 = True
            
        curLineNo += 1
    fp.close()
    
    if cond1 and cond2:
        os.remove(fname)
        leftList = []
        idx = 0
        for line in fultxt:
            if idx >= startLineNo and idx <= endLineNo:
                idx += 1
                continue
            idx += 1
            leftList.append(line)
        
        newfp = open(fname,'w')
        for newline in leftList:
            newfp.write(newline)
        newfp.close()
                
if __name__ == "__main__":
    rootDir = raw_input("Type a directory name:");
    matchFiles = [];
    enumAllMatchFiles(rootDir, matchFiles)
    print matchFiles
    for file in matchFiles:
        clearDeclaration(file)
    