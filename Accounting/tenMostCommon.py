fhead = open('example.txt')
counts = dict()
for line  in fhead:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

lst = lst()
for key, val in counts.item():
  newtup = (val,key)
  lst.append(newtup)
  
lst = sorted(lst, reverse=True)
for val, key in lst[:10]
  print(key, val)
