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
  # 4th field may have a comment. It should start with digits,
  # which are taken to be count of number of verses
  m = re.search(r'^([0-9]+)(.*)$',parts[3])
  if not m:
   print('Problem line %s: %s' %(iline,line))
   exit(1)
  self.numverse = m.group(1)
  comment = m.group(2).strip()
  if comment != '':
   print('%s,%s,%s,%s: %s' %(self.page,self.verse1,self.verse2,self.numverse,comment))

 def todict(self):
  try:
   e = {
   'page':int(self.page), 
   'v1':int(self.verse1), 'v2':int(self.verse2), 'n':int(self.numverse)
   }
  except:
   print('todict error at line',self.iline+1)
   print(self.line)
   exit(1)
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

def check1(pagerecs):
 nok = 0
 nprob = 0
 for rec in pagerecs:
  d = rec.todict() # to get int values
  n1 = d['v2'] - d['v1'] + 1 # estimate of number of verses
  n = d['n'] # number of verses from input
  ndiff = n - n1
  if ndiff in [0,-1,1]:
   nok = nok + 1
  else:
   nprob = nprob + 1
   print('check1: %s,%s,%s,%s (%s)' %(rec.page,rec.verse1,rec.verse2,rec.numverse,ndiff))
 print('check1 stats: nok=%s, nprob=%s' %(nok,nprob))

def check2(pagerecs):
 # check that rec1.v2 + 1 == rec2.v1
 nok = 0
 nprob = 0
 for irec1,rec1 in enumerate(pagerecs[0:-1]):
  d1 = rec1.todict() # to get int values
  rec2 = pagerecs[irec1+1] # next record
  d2 = rec2.todict()
  if (d1['v2'] + 1) == d2['v1']:
   nok = nok + 1
  else:
   nprob = nprob + 1
   print('check2 a: ',rec1.line.replace('\t',','))
   print('check2 b: ',rec2.line.replace('\t',','))
   print()
 print('check2 stats: nok=%s, nprob=%s' %(nok,nprob))

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 pagelist = init_pagelist(pagerecs)
 write(fileout,pagelist)
 check1(pagerecs)
 check2(pagerecs)
 
