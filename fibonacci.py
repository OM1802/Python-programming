#code to print Fibonacci series
n1=0
n2=1
count=0
ne=int(input("ENTER THE NUMBER OF ELEMENTS TO DISPLAY FOR FIBONACCI SERIES \n"))
if(ne==0):
    print("PRINT A POSITIVE INTEGER MORE THAN 0")
elif(ne==1):
    print("SERIES: \n")
    print(n1)
else:
    print("SERIES: \n")
    while(count<ne):
        print(n1)
        next=n1+n2
        n1=n2
        n2=next
        count+=1
    
