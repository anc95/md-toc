# md-toc
a python script to generate the toc (table of contents) of markdown

## TOC
- [md-toc](#md-toc)
  - [todo](#todo)
  - [Ussage](#ussage)
  - [Example](#example)
    - [output toc](#output-toc)
    - [output md with toc](#output-md-with-toc)

## todo
- [ ] basic func
- [ ] unit test
- [ ] js version and a chrome extension

## Ussage

```
usage: gen-toc.py [-h] [-i] markdown

generate toc of markdown

positional arguments:
  markdown    markdown file from local or internet

optional arguments:
  -h, --help  show this help message and exit
  -i          insert the toc into md
```

## Example
test.md
````
# md-toc
a python script to generate the toc (table of contents) of markdown

## toc
@{md-toc}@

## todo
- [ ] basic func
- [ ] unit test
- [ ] js version and a chrome extension

## Ussage xx
### ussage1
### ussage 2
## todo2
# todo3

```
## Ussage
### ussage1
### ussage 2
## todo2
# todo3
```
````
### output toc
```
python gen-toc.py test.md
```
output
```
- [md-toc](#md-toc)
  - [toc](#toc)
  - [todo](#todo)
  - [Ussage xx - *](#ussage-xx---)
    - [ussage1](#ussage1)
    - [ussage 2](#ussage-2)
  - [todo2](#todo2)
- [todo3](#todo3)
```
### output md with toc
```
python gen-toc test.md -i
```
````
# md-toc
a python script to generate the toc (table of contents) of markdown

## toc
  - [md-toc](#md-toc)
    - [toc](#toc)
    - [todo](#todo)
    - [Ussage xx](#ussage-xx)
      - [ussage1](#ussage1)
      - [ussage 2](#ussage-2)
    - [todo2](#todo2)
  - [todo3](#todo3)


## todo
- [ ] basic func
- [ ] unit test
- [ ] js version and a chrome extension

## Ussage xx
### ussage1
### ussage 2
## todo2
# todo3

```
## Ussage
### ussage1
### ussage 2
## todo2
# todo3
```
````