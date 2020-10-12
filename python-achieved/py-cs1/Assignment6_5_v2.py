text = "X-DSPAM-Confidence:    0.8475";
smPosition=text.find(':')
print(smPosition)
textPiece=text[smPosition+2:]
print(textPiece)
fnumber=float(textPiece)
print(fnumber)
