// (setq js-indent-level 1)  # for Emacs

function verse_error(verse) {
 let elt=document.getElementById('verse');
 let html = '<p>Could not find verse ' + verse + '</p>';
 elt.innerHTML = html;
}

function verse_id(indexes) {
 [indexprev,indexcur,indexnext] = indexes;
 let vol = indexcur['v'];
 let page = indexcur['page'];
 let v1 = indexcur['v1'];
 let v2 = indexcur['v2'];
 let p = indexcur['p']; // parvan index 1 to 18
 let html = `<p>verses ${v1} - ${v2}</p>`;
 let elt = document.getElementById('verseid');
 elt.innerHTML = html;
 elt = document.getElementById('title');
 //html = 
}

function get_verse_from_url() {
 /* two methods to get verse (V)
 V 
 ?V     V digit string
*/
 let href = window.location.href;
 let url = new URL(href);
 let verse = url.searchParams.get('verse'); // Could be null
 if (verse == null) {
  let search = url.search  // ?X
  verse = search.substr(1)  // drop initial ?
 }
 //console.log('get_verse_from_url: ',verse);
 return verse;
}
function unused_get_index_from_verse(verse,indexdata) {
 // verse = v  
 if ((typeof verse) != 'string') {return null;}
 let v = verse;
 let pages = indexdata;
 let page = null;
 for (let x of pages) {
  if ((x.v1 <= v) && (v <= x.v2)) {
   page = x;
   break;
  }
 }
 return page;
}
function get_indexes_from_verse(verse,indexdata) {
 // verse = v  
 // return index info for previous, current, and next page.
 // current page derived from 'verse' (v).
 // previous and next page implied.
 ans = [null,null,null];
 if ((typeof verse) != 'string') {return ans;}
 let v = verse;
 let pages = indexdata;
 let cur = null;
 let prev = null;
 let next = null;
 let n = pages.length;
 for (let i=0;i<n;i++) {
  let x = pages[i];
  if ((x.v1 <= v) && (v <= x.v2)) {
   cur = x;
   if (i == 0) {
    prev = x;
   }else {
    prev = pages[i-1];
   }
   let j = i+1;
   if (j == n){
    next = x;
   }else {
    next = x[j];
   }
   break;
  }
 }
  return [prev,cur,next];
}

function get_pdfpage_from_index(index) {
/* index is object with keys:
  page: page in volume,
  v1: first verse, v2: last verse
  n: number of verses
 return name of file with the given volume and page
 hariv_NNN.pdf  where NNN is 0-filled from page
*/
 if (index == null) {return null;}
 let page = index['page']
 let text = page.toString();
 let nnn = text.padStart(3,'0');
 let pdf = 'hariv_' + nnn + '.pdf';
 return pdf
}

function get_verse_html(indexcur) {
 let html = null;
 if (indexcur == null) {return html;}
 let pdfcur = get_pdfpage_from_index(indexcur);
 let urlcur = `pdfpages/${pdfcur}`;
 let android = ` <a href='${urlcur}' style='position:relative; left:100px;'>Click to load pdf</a>`;
 let imageElt = `<object id='servepdf' type='application/pdf' data='${urlcur}' 
              style='width: 98%; height:98%'> ${android} </object>`;
 //console.log('get_verse_html. imageElt=',imageElt);
 return imageElt;
}


function display_verse_html(indexes) {
 verse_id(indexes);
 let html = get_verse_html(indexes[1]);
 let elt=document.getElementById('verse');
 elt.innerHTML = html;
}
function display_verse_url() {
 let v = get_verse_from_url();
 let indexes = get_indexes_from_verse(v,indexdata);
 let indexcur = indexes[1];
 if (indexcur == null) {
  verse_error(v);
  return;
 }
 display_verse_html(indexes);
}
//test();

// indexdata assumed available 
document.getElementsByTagName("BODY")[0].onload = display_verse_url;
/*
file:///E:/sanskrit-lexicon-scans/hariv/pdfpages/hariv_1.418.pdf
file:///E:/pdfwork/hariv/pdfpages/hariv_1.418.pdf

file:///E:/pdfwork/hariv/pdfpages/hariv_1.418.pdf

*/
