import re

HEADER_REG = re.compile('^(#{1,6})\s+(\S+.*)')
ILLEGAL_ID_LETTER_REG = re.compile('[^a-zA-Z-_]*')
SPACE_REG = re.compile('\s+')

def main():
    header_list = parse_file_header('./test.md')
    md = header_list_2_md(header_list)
    print md

def parse_file_header(file):
    header_List = []
    file = open(file, 'r')
    inCode = False
    for line in file:
        if not inCode: 
            m = HEADER_REG.match(line)
            if (m):
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
    header = SPACE_REG.sub('-', header)
    return ILLEGAL_ID_LETTER_REG.sub('', header)

if __name__ == '__main__':
    main()

