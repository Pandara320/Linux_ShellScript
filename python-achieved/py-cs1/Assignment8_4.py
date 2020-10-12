fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    if line == " ":continue
    splitedwords = line.split()
    for i in splitedwords:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)

