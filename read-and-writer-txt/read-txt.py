infile = open('file.txt', 'r') # read
lines = infile.readlines()
for i in range(len(lines)):
	print(lines[i].strip())
infile.close()

