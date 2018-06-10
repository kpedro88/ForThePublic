PANDOC = pandoc
M4 = m4
TAIL = tail
CITEPROCTEXFLG = --pdf-engine=xelatex --filter=pandoc-citeproc --standalone
PANFLG = --pdf-engine=xelatex --standalone
PAN2FLG = --pdf-engine=xelatex --standalone -M date="`date "+%B %e, %Y"`" --template=latex_template.tex
PDFS = complete_publication_list.pdf computing_publication_list.pdf physics_publication_list.pdf experiment_publication_list.pdf short_computing_publication_list.pdf short_physics_publication_list.pdf shortest_computing_publication_list.pdf shortest_physics_publication_list.pdf

.PHONY: inspire local clean all $(PDFS)

all: $(PDFS)

$(PDFS):
	rm -f _tmp.tex _tmp1.md
	$(PANDOC) $(CITEPROCTEXFLG) $(subst .pdf,_template_citeproc.md,$@) -o _tmp.tex
	$(PANDOC) $(PANFLG) _tmp.tex -o _tmp1.md
	$(TAIL) -n +7 _tmp1.md > $(subst .pdf,.md,$@)
	$(M4) $(subst .pdf,_template_resolved.md,$@) > $(subst .pdf,_resolved.md,$@)
	$(PANDOC) $(PAN2FLG) $(subst .pdf,_resolved.md,$@) -o $@
	rm -f _tmp.tex _tmp1.md

inspire:
	python update_publication_list.py

local:
	python update_publication_list.py --input complete_publication_list.bib

clean:
	rm -f *.pdf *.out *.log *.aux _tmp.tex _tmp1.md _tmp2.md
