# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    sLine=line.rstrip()
    print(sLine.upper())
    
