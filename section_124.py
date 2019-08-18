#section_124.py

def writeFile():
    try:
        f = open('file', 'w')
        try:
            f.write('Hello World!')
        finally:
            f.close()
    except IOError:
        print('oops!')

def readFile():
    try:
        f = open('file', 'r')
        line = f.readline()
    except IOError:
        print('oops!')
    else:
        print(line)
    finally:
        f.close()

writeFile()
readFile()
