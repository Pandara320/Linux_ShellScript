score = input("Enter a Score between 0.0 and 1.0: ")
try:
    fscore=float(score)
except:
    print("Error, bad input")
    quit()

if fscore >= 0.9 and fscore <= 1.0:
	print ("A")
elif fscore >= 0.8 and fscore < 0.9:
    print ("B")
elif fscore >= 0.7 and fscore < 0.8:
    print ("c")
elif fscore >= 0.6 and fscore < 0.7:
    print ("D")
elif fscore >= 0.0 and fscore < 0.6:
    print ("F")
else:
    print("Error: input score is not in range")
