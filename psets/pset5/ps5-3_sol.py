# open output file, write mode
outf = open("ps5-3_out.txt","w")

import re

# iterate throuugh input file
for line in open("ps4-5_in.txt"):
    # split on comma
    fields = line.split(',')
   
    if re.match('a',fields[0].strip()) and re.match('student$',fields[1].strip()):
        outf.write(line)

outf.close()

