def isprime():
    l=[]
    n=int(input("Enter your number:"))
    for i in range (1,n+1):
        if (n%i)==0:
            l.append(i)
    if len(l)>2:
        print(f"{n} is not prime")
    else:
        print(f"{n} is prime")
        
isprime()

//the print loop should be out of the first for loop
//I was not executing the function after defining it and thus was getting no o/p
//shoulf use f"{} instead of the C lang 


