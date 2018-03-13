PANDOC = pandoc
M4 = m4
PANFLG = --pdf-engine=xelatex --standalone
PDFS = cv.pdf

.PHONY: clean all $(PDFS)

all: $(PDFS)

$(PDFS): 
	$(M4) $(subst .pdf,_template.md,$@) > $(subst .pdf,.md,$@)
	$(PANDOC) $(PANFLG) $(subst .pdf,.md,$@) -o $@
	
clean:
	rm -f *.pdf *.out *.log *.aux

