name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

stuff = []
mydictionary=dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        stuff = line[1]
        if stuff in mydictionary:
            mydictionary[stuff] = mydictionary.get(stuff,0)+1
        else:
           	mydictionary[stuff] = 1
    else:
        continue
        
condition = -1
sender_prolific = None

for stuff, num in mydictionary.items():
    if num > condition:
        condition = num
        sender_prolific = stuff
print(sender_prolific, condition)
