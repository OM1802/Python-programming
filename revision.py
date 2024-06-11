#Revision practice class codes
import pandas as pd
import numpy as np
#greatest of 4 numbers 
a=int(input("ENTER VALUE: "))
b=int(input("ENTER VALUE: "))
c=int(input("ENTER VALUE: "))
d=int(input("ENTER VALUE: "))
if(a>b and a>c and a>d):
    print(a, "IS THE GREATEST NUMBER")
elif(b>a and b>c and b>d):
    print(b, "IS THE GREATEST NUMBER")
elif(c>a and c>b and c>d):
    print(c, "IS THE GREATEST NUMBER")
else:
    print(d, "IS THE GREATEST NUMBER")

#odd numbers
for n in range(1,10,2):
    print(n)

#right angle triangle 📐 pattern 
for i in range(5):
    for j in range(i+1):
        print(j, end=" ")
    print()

#area of a room, no of chair size accomodable
a=40
b=50
cs=4
ar=(2*(a+b))
print(ar/cs)

#implementation of pandas library using different data structures
d1=np.array([10,20,30,40,50])#using array
d2=[1,2,3,4,5]#using list
d3=(70,52,41,71,55)#using tuple
d4={'OM':35, 'RAWAT':100, 'SHIWA':80, 'UDIT':50}#using set
myseries=pd.Series(d4)
print(myseries)
