# Talk Lost

## Prepare all markdown and pdf

```
make all
```

* prepare markdown files of all publication BiBTeX files from above
    * [talk_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/talk_list.md)
    * [short_talk_list.md](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/short_talk_list.md)
* prepare PDFs of all publication BiBTeX files from above
    * [talk_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/talk_list.pdf)
    * [short_talk_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/short_talk_list.pdf)

## Prepare individual markdown and PDF

```
make <pdf name>
```

replacing "\<pdf name\>" with one of:

* [talk_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/talk_list.pdf)
* [short_talk_list.pdf](https://raw.githubusercontent.com/gutsche/ForThePublic/master/talk_list/short_talk_list.pdf)

## Execution environment

A docker container with all necessary program packages based on CentOS 7 can be found [here](https://github.com/gutsche/docker-containers/tree/master/forthepublic-container).