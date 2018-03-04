# publication list

## Query Inspire

```
make inspire
```

* query [Inspire](http://inspirehep.net) for all publications of [Oliver Gutsche](http://inspirehep.net/author/profile/O.Gutsche.1)
* add [additional publications not listed in Inspire](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/additional_publication_list.bib)
* store [all publications in one BiBTeX file](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.bib)
* separate all publications into 3 categories:
    * [Physics Publications with Major Personal Contributions](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/physics_publication_list.bib)
    * [Computing Publications with Major Personal Contributions](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.bib)
    * [Publications from all Collaborations and Experiments](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/experiment_publication_list.bib)
* manually maintain shortened lists of the last most important physics and computing publications
    * [Short Physics Publications with Major Personal Contributions](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_physics_publication_list.bib)
    * [short Computing Publications with Major Personal Contributions](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_computing_publication_list.bib)

## Prepare BibTex files using local information

```
make local
```

* same process as in above without querying [Inspire](http://inspirehep.net) but reading in the [BibTeX file of the complete list of publications](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.bib) from the local directory

## Prepare all markdown and pdf

```
make all
```

* prepare markdown files of all publication BiBTeX files from above
    * [complete_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/complete_publication_list.md)
    * [physics_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/physics_publication_list.md)
    * [computing_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.md)
    * [experiment_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/experiment_publication_list.md)
    * [short_physics_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_physics_publication_list.md)
    * [short_computing_publication_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_computing_publication_list.md)
* prepare PDFs of all publication BiBTeX files from above
    * [complete_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/complete_publication_list.pdf)
    * [physics_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/physics_publication_list.pdf)
    * [computing_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.pdf)
    * [experiment_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/experiment_publication_list.pdf)
    * [short_physics_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_physics_publication_list.pdf)
    * [short_computing_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_computing_publication_list.pdf)

## Prepare individual markdown and PDF

```
make <pdf name>
```

replacing <pdf name> with one of:

* [complete_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/complete_publication_list.pdf)
* [physics_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/physics_publication_list.pdf)
* [computing_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/computing_publication_list.pdf)
* [experiment_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/experiment_publication_list.pdf)
* [short_physics_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_physics_publication_list.pdf)
* [short_computing_publication_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/publication_list/short_computing_publication_list.pdf)
