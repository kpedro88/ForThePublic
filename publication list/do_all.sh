#!/bin/bash

python update_publication_list.py --input complete\ publication\ list.bib
pandoc --pdf-engine=xelatex --filter=pandoc-citeproc --standalone complete\ publication\ list.md -o complete\ publication\ list.pdf
pandoc --pdf-engine=xelatex --filter=pandoc-citeproc --standalone physics\ publication\ list.md -o physics\ publication\ list.pdf
pandoc --pdf-engine=xelatex --filter=pandoc-citeproc --standalone computing\ publication\ list.md -o computing\ publication\ list.pdf
pandoc --pdf-engine=xelatex --filter=pandoc-citeproc --standalone experiment\ publication\ list.md -o experiment\ publication\ list.pdf
