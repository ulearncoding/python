outfile = open('file.txt', 'w') # write
for i in range(1,4):
    outfile.writelines("line"+str(i)+"\n")
outfile.close()

