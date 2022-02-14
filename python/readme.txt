Convert the tab-delimited index file into a json object,
python make_json_index.py hariv_index.txt index.js

copy index.js for use by index.html
 cp index.js ../

---------------------------------------------------------------------
Output from make_json_index.py after changes
59,1697,1726,29: readme.txt
89,2582,2610,29: readme.txt
144,4196,4230,30: readme.txt
345,10075,10104,30: readme.txt
346,10105,10134,30: readme.txt
347,10135,10164,30: readme.txt
348,10165,10194,30: readme.txt
409,11935,11961,27: readme.txt
410,11962,11991,30: readme.txt
411,11992,12017,26: readme.txt
412,12018,12047,30: readme.txt
413,12048,12081,30: readme.txt
499,14543,14571,29: readme.txt
563 Page records read from hariv_index.txt
json written to index.js
check1: 144,4196,4230,30 (-5)
check1: 413,12048,12081,30 (-4)
check1 stats: nok=561, nprob=2
check2 stats: nok=562, nprob=0



---------------------------------------------------------------------
changes made to hariv_index.txt
---------------------------------------------------------------------
59	1697	1726	29 question? After verse 1713, the line is not a verse

OLD:
88	2552	2581	30
89	2582	1610	29
90	2611	2640	30
NEW:
88	2552	2581	30
89	2582	2610	29 change
90	2611	2640	30

144	4196	4230	30 verse gap: 1425-1429 (1415, 1420, 1430)

OLD:
344	10045	10074	30
345	10075	11004	30 
346	11005	11034	30 *
347	11035	11064	30 *
348	11065	11094	30 *
349	10195	10224	30
NEW:
344	10045	10074	30
345	10075	10104	30 verse count?
346	10105	10134	30 change
347	10135	10164	30 change
348	10165	10194	30 change
349	10195	10224	30

OLD:
408	11907	11934	28
409	935	961	27 *
410	962	991	30 *
411	992	1017	26 *
412	1018	1047	30 *
413	1048	12081	30 *
414	12082	12111	30
NEW:
408	11907	11934	28
409	11935	11961	27 change
410	11962	11991	30 change
411	11992	12017	26 change
412	12018	12047	30 change
413	12048	12081	30 change
414	12082	12111	30


OLD:
499	14543	14566	29 
500	14572	14600	29
NEW:
499	14543	14571	29 change, versegap  14567-14571
500	14572	14600	29

---------------------------------------------------------------------
notes on preparation of the pdfpages file.
Mahabharata Calcutta Edition
The source of these documents is given at
https://github.com/sanskrit-lexicon/COLOGNE/issues/371#issuecomment-971742611
.

The MAHA1BHA1RATA, AN EPIC POEM written by THE CELEBRATED VEDA VYA1SA RISHI.
VOL. I. Calcutta 1834 
  PART I. -- THE A1DI PARVA.
      II. -- THE SABHA1 PARVA.
     III. -- THE VANA PARVA.
VOL. II. Calcutta 1836
 PART IV. -- VIRAT PARVA.
 PART V. -- UDYOGA PARVA.
 PART VI. -- BHISMA PARVA.
 PART VII. -- DRONA PARVA.
VOL. III. Calcutta 1837
 PART VIII. KARNA PARVA.
 PART IX . SAILA PARVA.
 PART X. SAUPTIKA PARVA.
 PART XI . STRI PARVA.
 PART XII. SANTI PARVA.

VOL. IV. Calcutta 1839
 PART XIII.  ANUSHA1SANA PARVA.
 PART XIV. A1SHUAMEDHIKA PARVA.
 PART XV.  A1SHRAMABA1SIKA PARVA.
 PART XVI.  MAUSALA PARVA.
 PART XVII. MAHA1PRASTHA1NIKA PARVA.
 PART XVIII. SUARGA1ROHANIKA PARVA.
 PART XIX.  KHILA HARIBANSHA PARVA.

 
-------------------
  In mbh_calc_1.pdf, (mbh_calc_1 N.pdf)
   page 6 English title page  
   page 8 Sanskrit title page
   page 10 Internal page 1
    ...
   page 840 Internal page 831
Adobe Acrobat 9.0 Extract pages as Separate files: 1 to 840
-------------------
In mbh_calc_2.pdf (mbh_calc_2 N.pdf)
 page 6 English title page
 page 8 Sanskrit title page
 page 10 Internal page 1
    ...
   page 873 Internal page 868
Adobe Acrobat 9.0 Extract pages as Separate files: 1 to 873
-------------------
  In mbh_calc_3.pdf, (mbh_calc_3 N.pdf)
   page 6 English title page  
   page 8 Sanskrit title page
   page 10 Internal page 1
    ...
   page 866 Internal page 859
Adobe Acrobat 9.0 Extract pages as Separate files: 1 to 866
-------------------
  In mbh_calc_4.pdf, (mbh_calc_4 N.pdf)
   page 6 English title page  
   page 8 Sanskrit title page
   page 10 Internal page 1
    ...
   page 452 Internal page 443  (last page of MBH proper).
   page 453 blank page
   page 454 Internal page 445  (first page of Harivamsha)
    ...
   page 1016 Internal page 1009 (last page of Harivamsha)
   
Adobe Acrobat 9.0 Extract pages as Separate files: 1 to 1016


MBh.Calc.ed.index.Vol.s.1-4.txt

For volume 4, goes to end of PART XVIII; last line is
 4	443	XVIII	312	312	1

-------------------------------------------------
<L>9567<pc>1-0717<k1>ASAvant<k2>ASAvant
<ls>HIT. I, 72.</ls> {#baBUvASAvatI bAlA punarBartfsamAgame#} 
<ls>MBH. 1, 16164.</ls> {#ASAvAMstezu (vAnarapuMgavezu)#}
found at 16164
1	785	III	16150	16178	29
Not found at 17164
1	820	III	17136	17164	29

-------------------------------------------------

PAGE PROBLEMS
1. vol.3 p 727 replace bad page
2. Two pages missing in vol. 3
3	498	ΧΙΙ	3752	3776	25
3	499	ΧΙΙ	3777	3805	29
------------------------------------------------
vol 1 page renumbering:
   6 -> English title
   8 ->
   10 -> 1, 11 -> 2, ..., 840 -> 831 (last)
   417->408 blank page. ok to retain. Remove next from index
1	408	--	--	--	-- blank ok to leave
-------------------------------------------------
vol 2 page renumbering:
   6 -> English title
   8 ->
   10 -> 1, 11 -> 2, ..., 133 -> 124
   134 -> 129, 135 -> 130, ...,
   539 -> 534 (blank ok to leave),
   ..., 873 -> 868 (last)
remove from index: 2	534	--	--	--	--

p. 125 marked as p. 129
 Page gap 125 - 128 QUESTION:
2	130	V	1050	1078	29

-------------------------------------------------
vol 3 page renumbering:
   6 -> English title
   8 ->
   10 -> 1, 11 -> 2, ..., 506 -> 497, 
   replacement -> 498, replacement -> 499,
   507 -> 500, ..., 607 -> 600, ...,
   734 -> 727 (replace bad page),
   866 -> 859 (last page)

-------------------------------------------------
vol 4 page renumbering:
   6 -> English title
   8 ->
   10 -> 1, 11 -> 2, ..., 
   452 -> 443 (last)
-------------------------------------------------
-------------------------------------------------
vol 4 page renumbering: HarivaMSa 
 pages 445 - x of mbh_calc_4.pdf
   6 -> English title
   8 ->
   454 -> 445, ..., 1016 -> 1007 (last page)
-------------------------------------------------
mbhcalc_renum.py
 python mbhcalc_renum.py mbhcalc_renum.sh

Generate script to move files in each of vol1,...,vol4 files to
 pdfpages directory (for parvan 1-18)

sh mbhcalc_renum.sh
file format 'pdfpages/mbhcalc_v.ppp.pdf'   (where v is 1-4 and ppp is 0-filled)
2 title pages for each volume
  'pdfpages/mbhcalc_v.000a' and 'pdfpages/mbhcalc_v.000b' and

3003 files
-------------------------------------------------
TODO: 
 hariv/pdfpages directory for parvan 19 (harivaMSa)
 
-------------------------------------------------

2	83	IV	2293	2322	30
Correction: 2322 -> 2321
2	84	IV	2323	2360	28
Correction: 2323 -> 2322

2	124	V	990	1019	30
995 > 990: -5 ?   QUESTION: what is this comment

2	129	V	1020	1049	30
p. 125 marked as p. 129
 Page gap 125 - 128 QUESTION:
2	130	V	1050	1078	29

2	148	V	1556	1578	23
2	149	V	1578	1598	21
1579 >1578 : -1
Page 148 ends with 1575 and 3 more verses, thus 1575-1578,
Page 149 begins with 2 verses then 1580, thus 1578-1580.
So there is confusion over verse 1578.

2	308	V	7013	7040	28
p. 308 marked as  p.380  (book typo.  Next page marked as 309. no page gap)

2	534	--	--	--	--

3	34	VIII	927	956	30
928 > 928 : -1
Extra verse either at end of page 33 or beginning of page 34

3	315	Χ	225	253	29
221 > 225 : 4   JIM: I don't see this

-----------------------------------------------------------------
verse-gap.txt

-----------------------------------------------------------------
n /e/pdfwork/mbhcalc/vol4,
'mbh_calc_4 454.pdf 'is first page of Harivamsa.
  internal page number is 445.

'mbh_calc_4 1016.pdf 'is last page of Harivamsa.
  internal page number is 1007.

