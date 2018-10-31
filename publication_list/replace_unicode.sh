#!/bin/bash

cp complete_publication_list.bib complete_publication_list.bib.bak

cat complete_publication_list.bib.bak | \
sed -e 's/\xcf\x84/\\ensuremath{\\tau}/g' | \
sed -e 's/\xc2\xa0/ /g' | \
sed -e 's/\xe2\x80\xb2/\\ensuremath{\\prime}/g' | \
sed -e 's/\xe2\x80\x93/-/g' | \
sed -e 's/\xe2\x80\x89/ /g' | \
sed -e 's/\xe2\x80\xaf/ /g' | \
sed -e 's/\xe2\x86\x92/\\to /g' | \
sed -e 's/\xce\xbc/\\ensuremath{\\mu}/g' | \
sed -e 's/\xe2\x88\x92/-/g' | \
sed -e 's/\xe2\x88\x9a/\\ensuremath{\\surd}/g' | \
sed -e 's/\xe2\x88\x97/*/g' | \
sed -e 's/\xce\xb3/\\ensuremath{\\gamma}/g' | \
sed -e 's/\xe2\x84\x93/\\ensuremath{\\ell}/g' | \
sed -e 's/\xcf\x88/\\ensuremath{\\psi}/g' | \
sed -e 's/\xce\xbd/\\ensuremath{\\nu}/g' | \
sed -e 's/\xc2\xb1/\\ensuremath{\\pm}/g' \
> complete_publication_list.bib
