# md-toc
a python script to generate the toc (table of contents) of markdown

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
### output toc
```
python gen-toc.py test.md
```
### output md with toc
```
python gen-toc test.md -i
```