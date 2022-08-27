def factorial( x):
    ans=1;
    for i in range (2,x+1):
        ans=ans*i;
    print(ans)

    

x=int(input("Enter the number whose factorial is to be found : "))
factorial(x)
