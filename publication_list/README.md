# publication list

## query inspire and update publications

```
python update_publication_list.py
```

## generate complete publication list in markdown

```
pandoc --pdf-engine=xelatex --filter=pandoc-citeproc --standalone complete\ publication\ list.md -o complete\ publication\ list.pdf
```

## generate complete publication list in pdflatex

```
pdflatex 'complete publication list - pdflatex'
bibtex 'complete publication list - pdflatex'
pdflatex 'complete publication list - pdflatex'
pdflatex 'complete publication list - pdflatex'
```