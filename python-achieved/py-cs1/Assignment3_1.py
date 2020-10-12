hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter rate: ")
r = float(rate)
if hrs > 40 :
   payment = 40*r+(h-40)*(1.5*r)
else:
   payment = h*r
print (payment)
