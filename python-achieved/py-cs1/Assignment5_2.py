largest = None
smallest = None
while True:
	try:
		num = input("Enter a number: ")
		if num == "done" : break
		fnum = int(num)
		if largest < fnum :
			largest = fnum
		if smallest == None or smallest > fnum:
			smallest = fnum
	except:
		print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
