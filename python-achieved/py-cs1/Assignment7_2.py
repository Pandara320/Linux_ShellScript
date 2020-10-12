# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
value = 0
count = 0
average = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
		continue
    position = line.find(" ")
    val = line[position:].rstrip()
    fval = float(val)
    count = count + 1
    value = value + fval
print("Average spam confidence:", value/count)
