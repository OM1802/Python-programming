#code to calculate the sum of digits of a number
def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = 569
print(getSum(n))
