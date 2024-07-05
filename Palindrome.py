#code to check if a number is palindrome or not
n=int(input("ENTER A NUMBER: \n"))
temp=n
reverse=0
while(n>0):
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
if(reverse==temp):
    print(temp, "IS A PALINDROME NUMBER")
else:
    print(temp, "IS NOT A PALINDROME NUMBER")
    
