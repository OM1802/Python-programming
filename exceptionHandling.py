#code showing syntax of exceptional handling in python 
try:
    result=10/0
    print(result)
except:
    print("ERROR IDENTIFIED!!")
else:
    print("CODE EXECUTED SUCCESSFULLY")
finally:
    print("PROGRAM OVER")
