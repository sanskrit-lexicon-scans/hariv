# coding=utf-8
from __future__ import print_function
import sys, re,codecs
import json

class Pagerec(object):
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  assert len(parts) in [4,5]
  self.line = line
  self.iline = iline
  self.page = parts[0]
  self.verse1 = parts[1]
  self.verse2 = parts[2]
  self.numverse = parts[3]
  assert re.search(r'^[0-9]+$',self.numverse) 
  if len(parts) == 5:
   print('%s,%s,%s,%s comment=%s' %(self.page,self.verse1,self.verse2,
                                    self.numverse,parts[4]))
 
 def todict(self):
  e = {
   'page':int(self.page), 
   'v1':int(self.verse1), 'v2':int(self.verse2), 'n':int(self.numverse)
  }
  return e
def init_pagerecs(filein):
 """ filein is a csv file, with tab-delimiter and with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if iline == 0:
    # skip field names
    continue
   pagerec = Pagerec(line,iline)
   recs.append(pagerec)
 print(len(recs),'Page records read from',filein)
 return recs

def init_pagelist(pagerecs):
 d = []
 for rec in pagerecs:
  recobj = rec.todict()
  d.append(recobj)
 return d
def write(fileout,x):
 
 with codecs.open(fileout,"w","utf-8") as f:
  outarr = []
  outarr.append('indexdata = [')
  for d in x:
   jsonstring = json.dumps(d)
   outarr.append('%s,' %jsonstring)
  outarr.append('];')
  for out in outarr:
   f.write(out +'\n')
 print('json written to',fileout)
 
if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 pagelist = init_pagelist(pagerecs)
 write(fileout,pagelist)
 
 
