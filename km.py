lower=int(input("Enter number:"))
upper=int(input("Enter number:"))
for i in range(lower,upper+1):
    if(i%2==0):
        break
    else:
        print("Prime Number")
        print(i)
