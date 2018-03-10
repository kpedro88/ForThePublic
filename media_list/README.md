# media Lost

## Prepare all markdown and pdf

```
make all
```

* prepare markdown files of all publication BiBTeX files from above
    * [media_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/media_list.md)
    * [short_media_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/short_media_list.md)
* prepare PDFs of all publication BiBTeX files from above
    * [media_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/media_list.pdf)
    * [short_media_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/short_media_list.pdf)

## Prepare individual markdown and PDF

```
make <pdf name>
```

replacing "\<pdf name\>" with one of:

* [media_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/media_list.pdf)
* [short_media_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/media_list/short_media_list.pdf)

## Execution environment

A docker container with all necessary program packages based on CentOS 7 can be found [here](https://github.com/gutsche/docker-containers/tree/master/forthepublic-container).