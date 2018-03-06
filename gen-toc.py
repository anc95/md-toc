import re
import requests
import argparse

HEADER_REG = re.compile('^(#{1,6})\s+(\S+.*)')
ILLEGAL_ID_LETTER_REG = re.compile('[^a-zA-Z0-9-_]*')
SPACE_REG = re.compile('\s+')
LINK_REG = re.compile('^https{0,1}://')
CODE_ZONE_REG = re.compile('^```')

def main():
    parser = argparse.ArgumentParser(description='generate toc of markdown')
    parser.add_argument('md', metavar='markdown', nargs=1, help="markdown file from local or internet")
    parser.add_argument('-i', dest='insert', action='store_true', help='insert the toc into md')
    args = parser.parse_args()
    toc_ins = Toc(args.md[0], args.insert)
    print toc_ins.get_toc()

class Toc:
    def __init__(self, md, if_insert):
        self.md = md
        self.if_insert = if_insert

    def get_toc(self):
        md_content = ''
        file = self.md
        if LINK_REG.match(file):
            md_content = requests.get(file).text.split('\n')
        else:
            with open(file, 'r') as f:
                md_content = f.read().split('\n')

        (header_list, insert_line_index) = self.parse_file_header(md_content)
        toc = self.header_list_2_md(header_list)
        
        if self.if_insert:
            toc = self.insert_toc(md_content, toc, insert_line_index)
        
        return toc
            
    def parse_file_header(self, md_content):
        header_List = []
        insert_line_index = 0
        inCode = False
        for index in range(len(md_content)):
            line = md_content[index]
            if self.if_insert and (line.lower() == '@{md-toc}@'):
                insert_line_index = index

            if CODE_ZONE_REG.match(line):
                inCode = not inCode
            if not inCode:
                m = HEADER_REG.match(line)
                if m:
                    level = len(m.group(1))
                    name = m.group(2).strip()
                    id = self.cal_header_id(name)
                    header_List.append({
                        "name": name,
                        "level": level,
                        "id": id
                    })
        return (header_List, insert_line_index)

    def header_list_2_md(self, header_list):
        md = ''
        for header in header_list:
            level = header.get('level')
            name = header.get('name')
            id = header.get('id')
            md +=  '{}- [{}](#{})\n'.format(' ' * 2 * level, name, id)
        return md

    def cal_header_id(self, header):
        header = SPACE_REG.sub('-', header).lower()
        return ILLEGAL_ID_LETTER_REG.sub('', header)

    def insert_toc(self, md_content, toc, line_index):
        md_content[line_index] = toc
        return '\n'.join(md_content)

if __name__ == '__main__':
    main()

