# coding=utf-8
import os

PRE = '''# Webflux 
探索与实战
堂堂连载！

## 索引


'''

def resolveReadme():

    lines = []
    for root, dirs, files in os.walk(r'doc'):
        space = 0
        if root != 'doc':
            root = root.replace(' ', '%20')
            dirname = root.split('/')[-1].replace(' ', '%20')
            lines.append('- [%s](%s)' % (dirname, root))
            lines.append('\n')
            for f in files:
                lines.append('    - [%s : %s](%s/%s)' % (dirname, f, root, f))
                lines.append('\n')

    return lines


if __name__ == '__main__':
    strLine = resolveReadme()
    with open('README.md', 'w+') as readme:
        readme.write(PRE)
        readme.writelines(strLine)
