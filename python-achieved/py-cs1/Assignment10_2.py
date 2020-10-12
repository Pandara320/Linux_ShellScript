name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()

for line in handle :
	line = line.rstrip()
	if line == "" : continue
	words = line.split()
	if words[0]	!=	"From"	:	continue
	time = words[5].split(":")
	counts[time[0]] = counts.get(time[0], 0) + 1
    
list = list()

for k,v in counts.items() :    # add 
	list.append((k, v))

# sort list in order

list.sort()
for hour, num in list :
	print(hour,num)
