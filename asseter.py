import re
import sys


def neutralize(template):
    result = ''
    for i in template:
        tmp = re.findall('(?:src|href)="([^"]*)"', i)

        if len(tmp) > 0:
            if 'http' not in tmp[0] and '#' not in tmp[0] and '.html' not in tmp[0]:
                result += i.replace(tmp[0], "{{asset('/%s')}}" % tmp[0])
            else:
                result += i
        else:
            result += i

    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage : python asseter.py file-template file-output"
    else:
        with open(sys.argv[1], 'r') as template:
            clean = neutralize(template.readlines())

        output = open(sys.argv[2], 'w')
        output.write(clean)
        output.close()
        print "[i] Jobs Done"
