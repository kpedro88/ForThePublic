PANDOC = pandoc
M4 = m4
TAIL = tail
CLEANMD = python clean_bibtex_md.py
CITEPROCTEXFLG = --pdf-engine=xelatex --filter=pandoc-citeproc --standalone
PANFLG = --pdf-engine=xelatex --standalone
PAN2FLG = --pdf-engine=xelatex --standalone -M date="`date "+%B %e, %Y"`" --template=latex_template.tex
PDFS = media_list.pdf short_media_list.pdf

.PHONY: clean all $(PDFS)

all: $(PDFS)

$(PDFS):
	rm -f _tmp.tex _tmp1.md _tmp2.md
	$(PANDOC) $(CITEPROCTEXFLG) $(subst .pdf,_template_citeproc.md,$@) -o _tmp.tex
	$(PANDOC) $(PANFLG) _tmp.tex -o _tmp1.md
	$(TAIL) -n +7 _tmp1.md > _tmp2.md
	$(CLEANMD) _tmp2.md > $(subst .pdf,.md,$@)
	$(M4) $(subst .pdf,_template_resolved.md,$@) > $(subst .pdf,_resolved.md,$@)
	$(PANDOC) $(PAN2FLG) $(subst .pdf,_resolved.md,$@) -o $@
	rm -f _tmp.tex _tmp1.md _tmp2.md

clean:
	rm -f *.pdf *.out *.log *.aux _tmp.tex _tmp1.md _tmp2.md
