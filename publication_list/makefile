PANDOC = pandoc
M4 = m4
TEXFLG = --pdf-engine=xelatex --filter=pandoc-citeproc --standalone
PANFLG = --pdf-engine=xelatex --standalone
PDFS = complete_publication_list.pdf computing_publication_list.pdf physics_publication_list.pdf experiment_publication_list.pdf short_computing_publication_list.pdf short_physics_publication_list.pdf

.PHONY: inspire local clean all $(PDFS)

all: $(PDFS)

$(PDFS): 
	rm -f _tmp.tex _tmp1.md _tmp2.md
	$(PANDOC) $(TEXFLG) $(subst .pdf,_template.md,$@) -o _tmp.tex
	$(PANDOC) $(PANFLG) _tmp.tex -o _tmp1.md
	$(M4) $(subst .pdf,.md,$@) > _tmp2.md
	$(PANDOC) $(PANFLG) _tmp2.md -o $@
	rm -f _tmp.tex _tmp1.md _tmp2.md

inspire:
	python update_publication_list.py

local:
	python update_publication_list.py --input complete_publication_list.bib
	
clean:
	rm *.pdf *.out *.log *.aux

