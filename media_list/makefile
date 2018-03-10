PANDOC = pandoc
M4 = m4
TEXFLG = --pdf-engine=xelatex --filter=pandoc-citeproc --standalone
PANFLG = --pdf-engine=xelatex --standalone
PDFS = media_list.pdf short_media_list.pdf

.PHONY: clean all $(PDFS)

all: $(PDFS)

$(PDFS): 
	rm -f _tmp.tex _tmp1.md
	$(PANDOC) $(TEXFLG) $(subst .pdf,_template.md,$@) -o _tmp.tex
	$(PANDOC) $(PANFLG) _tmp.tex -o _tmp1.md
	$(M4) $(subst .pdf,_template_2.md,$@) > $(subst .pdf,.md,$@)
	$(PANDOC) $(PANFLG) $(subst .pdf,.md,$@) -o $@
	rm -f _tmp.tex _tmp1.md
	
clean:
	rm -f *.pdf *.out *.log *.aux _tmp.tex _tmp1.md _tmp2.md

