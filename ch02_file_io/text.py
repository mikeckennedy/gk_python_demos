import io

filename = r'C:\Users\Administrator\Desktop\holder\reqs_new.txt'

# one huge string
# print(fin.read())

def read_data(fin):
    lines = [l.strip('\n') for l in fin.readlines()]

    print(lines)

    for line in lines:
        print(line.strip('\n'))


# with open(filename, 'r', encoding='utf-8') as fin:
#     read_data(fin)

data = """\
Line 1
Line 2
Line 3
"""

test_stream = io.StringIO(data)
read_data(test_stream)

filename = r'out.txt'
# fout = open(filename, 'w', encoding='utf-8')
#
# fout.write("This is a line\n")
# fout.writelines(["Line 1\n", "line 2\n"])
# fout.close()

def writer():
    with open(filename, 'w', encoding='utf-8') as fout:
        write_data(fout)


def write_data(fout):
    fout.write("This is a line TEST\n")
    fout.writelines(["Line 1\n", "line 2 TEST\n"])


writer()








