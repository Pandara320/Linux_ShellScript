try:
    num=input("Enter the number of mimeng follower in Friendzone: \n") 
    total=input("Enter the total number of wechat friends: \n")
    fnum=float(num)
    ftotal=float(total)
except:
    print("Invalid input, Exit program ")
    quit()


def computeRate(n,t):
    rate = n / t * 100
    
    if rate<5:
        print("Nice! Result < 5%")
    elif rate<10:
        print("Good! Result < 10%")
    else:
        print("GG! Result > 10%")
    
    return rate
	
cResult=computeRate(fnum,ftotal)
roundResult=float(round(cResult,3))
print("Your mimeng Rate is: ", roundResult)

