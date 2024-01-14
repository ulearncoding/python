outfile = open('file.txt', 'w') # write
outfile.writelines("line1")
outfile.writelines("\n")
outfile.writelines("line2")
outfile.writelines("\n")
outfile.writelines("line3")
outfile.writelines("\n")
outfile.close()

