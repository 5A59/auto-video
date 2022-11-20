
import json

class Content:
    author = ''
    text_list = []


def read_all(f):
    text_list = []
    line_list = []
    l = f.readline().strip()
    while l:
        if l == '===':
            text_list.append(line_list)
            break
        if l == '--':
            if len(line_list) > 0:
                text_list.append(line_list)
            line_list = []
            l = f.readline().strip()
            continue
        else:
            line_list.append(l.strip())
            l = f.readline().strip()
    return text_list


def read_content():
    f = open("./content/content.txt", encoding='utf-8')
    content_list = []
    line = f.readline().strip()
    content = Content()
    while line:
        if line == '===':
            content = Content()
            content_list.append(content)
            content.author = f.readline().strip()
            line = f.readline().strip()
            continue
        if line == '==':
            content.text_list = read_all(f)
            line = f.readline().strip()
            continue
    f.close()
    for c in content_list:
        print(str(json.dumps(c.__dict__)))
    return content_list


if __name__ == '__main__':
    read_content()
