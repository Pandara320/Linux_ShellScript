hrs = input("Enter Hours:")
rte = input("Enter Rate:")
fhrs = float(hrs)
frte = float(rte)

def computepay(h,r):
    if(h<=40):
    	payment=r*h
    else:
        payment=(h-40)*(1.5*r)+(40*r)
    return payment


p = computepay(fhrs,frte)

print(p)
