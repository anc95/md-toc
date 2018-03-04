import re
import requests
import argparse

HEADER_REG = re.compile('^(#{1,6})\s+(\S+.*)')
ILLEGAL_ID_LETTER_REG = re.compile('[^a-zA-Z-_]*')
SPACE_REG = re.compile('\s+')
LINK_REG = re.compile('^https{0,1}://')
CODE_ZONE_REG = re.compile('^```')

def main():
    parser = argparse.ArgumentParser(description='generate toc of markdown')
    parser.add_argument('md', metavar='markdown', nargs=1, help="markdown file from local or internet")
    parser.add_argument('-d --dest', metavar='dest_file', nargs=1, help="the result write to a file")
    args = parser.parse_args()
    # print args.dest
    print get_toc(args.md[0])

def get_toc(md):
    header_list = parse_file_header(md)
    toc = header_list_2_md(header_list)
    return toc

def parse_file_header(file):
    header_List = []
    md_content = ''
    if LINK_REG.match(file):
        md_content = requests.get(file).text.split('\n')
    else:
        with open(file, 'r') as f:
            md_content = f.read().split('\n')
    inCode = False
    for line in md_content:
        if CODE_ZONE_REG.match(line):
            inCode = not inCode
        if not inCode:
            m = HEADER_REG.match(line)
            if m:
                level = len(m.group(1))
                name = m.group(2).strip()
                id = cal_header_id(name)
                header_List.append({
                    "name": name,
                    "level": level,
                    "id": id
                })
    return header_List

def header_list_2_md(header_list):
    md = ''
    for header in header_list:
        level = header.get('level')
        name = header.get('name')
        id = header.get('id')
        md +=  '{}- [{}](#{})\n'.format(' ' * 2 * level, name, id)
    return md

def cal_header_id(header):
    header = SPACE_REG.sub('-', header).lower()
    return ILLEGAL_ID_LETTER_REG.sub('', header)

if __name__ == '__main__':
    main()

