M4=m4
DATE=$(shell date +"%d. %B %Y")

.PHONY: all clean

all:
	rm -f h_tmp1.md
	$(M4) templates/cv_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/cv/cv.md
	rm -f h_tmp1.md
	$(M4) templates/resume_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/resume/resume.md
	rm -f _tmp1.md
	$(M4) templates/about_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/home/about.md
	rm -f _tmp1.md
	$(M4) templates/articles_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/articles/articles.md
	rm -f _tmp1.md
	$(M4) templates/talks_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/talks/talks.md
	rm -f _tmp1.md
	$(M4) templates/physics_pubs_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/physics_pubs/physics_pubs.md
	rm -f _tmp1.md
	$(M4) templates/computing_pubs_template.md > _tmp1.md
	cat _tmp1.md | sed 's/AAAAAAAAAABBBBBBBBBBCCCCCCCCCC/$(DATE)/g' > content/computing_pubs/computing_pubs.md
	rm -f _tmp1.md


clean:
	rm -f _tmp1.md
