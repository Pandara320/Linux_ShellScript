text = "X-DSPAM-Confidence:    0.8475";
zeroPosition=text.find('0')
Position=text.find('',zeroPosition)
number= text[zeroPosition:]
fnumber=float(number)
print(fnumber)
