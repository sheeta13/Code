# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError
import os, sys,shutil

#dest_fold=sys.argv[1]

def check(dest_fold):
    list_file=os.listdir(dest_fold)
    failed = []
    for name in list_file:
    #print name
        if name.lower().endswith('pdf'):
            dest=os.path.join(dest_fold,name)
            with open(dest,'rb') as f:
            # if not pdf,exception throw
                try:
                    inputFile = PdfFileReader(f)
                # pageNums = inputFile.getNumPages() # pdf page nums
                # if pageNums<4:
                #     raise Exception
                except Exception,e:
                    print name+' failed\n'
                    failed.append(name)                    
                    f.close()
                    shutil.move(dest,'./failed/'+name)
    f=open('failed_pdfs.txt','w')
    for x in failed:
        f.write(x+'\n')
    f.close()