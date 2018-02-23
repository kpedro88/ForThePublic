#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys, re, time
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup, Comment
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

inspirehepapi='http://inspirehep.net/search?'
author_query='author:O.Gutsche.1 AND collection:citeable'

def inspire_get_number_of_records():
    """
        return number of records for author_query
    """
    url = inspirehepapi + 'of=xm&rg=1&ot=001&p=' + author_query.replace(' ', '+')
    request = Request(url)
    try:
        response = urlopen(request)
        result = response.read()
        soup = BeautifulSoup(result, "lxml")
    except URLError, error:
        print 'URL =', url
        print 'No result. Got an error code:', error
        quit()
    try:
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        number_of_records = int(re.sub(r'\D', '', comments[0]))
    except IndexError:
        number_of_records = 0
        
    return number_of_records
    
def write_file(filename,input_string):
    with open(filename,'w') as output_file:
        output_file.write(input_string)
    
def inspire_get_bibtex(number_of_records):
    """
        get BiBTeX of all records
    """

    db = BibDatabase()
    
    nrecords = 250
    nsteps = int(number_of_records/nrecords) + 1
    for step in range(nsteps):
        jrec = step*nrecords+1
        url = inspirehepapi + 'of=hx&rg='+str(nrecords)+'&jrec='+str(jrec)+'&p=' + author_query.replace(' ', '+')
        request = Request(url)
        try:
            response = urlopen(request)
            BiBTeX = response.read()
        except URLError, error:
            print 'URL =', url
            print 'No result. Got an error code:', error
            quit()

        if 'No records' in BiBTeX:
            print "no records were found in SPIRES to match your search, please try again"
            print 'url:',url
            quit()
            
        parser = BibTexParser()
        tmp_db = bibtexparser.loads(BiBTeX, parser=parser)
        for entry in tmp_db.entries:
            # repair some broken output
            entry['title'] = entry['title'].replace('\n',' ')
            entry['title'] = entry['title'].replace('\sqrts','\sqrt{s}')
            entry['title'] = entry['title'].replace(' $','$')
            entry['title'] = entry['title'].replace('amp;','')
            entry['title'] = entry['title'].replace('text {','text{')
            entry['title'] = re.sub(r"\\text\{(.*?)\}",r"\\mathrm{\1}",entry['title'])
            entry['title'] = re.sub(r"([^ ])\$",r"\1 $",entry['title'])
            entry['title'] = entry['title'].replace('\\,\\mathrm','\\mathrm')
            entry['title'] = entry['title'].replace('\\;\\mathrm','\\mathrm')
            entry['title'] = entry['title'].replace('=\\ ','=')
            entry['title'] = entry['title'].replace('\\mathrm {','\\mathrm{')
            entry['title'] = entry['title'].replace('_\mathrm{NN}','_{\\mathrm{NN}}')
            entry['title'] = entry['title'].replace('$\sigma_\mathrm{t \\bar{t} b \\bar{b}} / \sigma_\mathrm{t \\bar{t}  jj } $','$\sigma_{\mathrm{t \\bar{t} b \\bar{b}}} / \sigma_{\mathrm{t \\bar{t}  jj }} $')
        db.entries.extend(tmp_db.entries)
    return db
# $\,TeV$
# $\sqrt{s_{_\mathrm {NN}}}

def write_bibtex_file(filename,db):
    """
        Write BiBTeX file with content from db
    """
    writer = BibTexWriter()
    with open(filename,'w') as output_file:
        bibtex_str = bibtexparser.dumps(db,writer=writer)
        output_file.write(bibtex_str.encode('utf8'))
    
def main(args):
    number_of_records = inspire_get_number_of_records()
    print "OLI's publication list has",number_of_records,"entries"
    inspire_db = inspire_get_bibtex(number_of_records)
    print "OLI's publication db has:",len(inspire_db.entries),"entries"
    write_bibtex_file('all.bib',inspire_db)
    
if __name__ == '__main__':
    main(sys.argv)