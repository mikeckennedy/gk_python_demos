import os

# not great
# filename = workingdir + "data\\subdata\\test.txt"

workingdir = os.path.abspath(os.path.dirname(__file__, ))
print(os.path.abspath(workingdir))
filename = os.path.join(workingdir, 'data', 'subdata', 'test.txt')
print(filename)

with open(filename, 'r') as fin:
    print(fin.readline())