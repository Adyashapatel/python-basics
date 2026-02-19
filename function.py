#salary = input("Enter your salary: ")
#  if int(salary) < 30000:
   # print("You are eligible for a 10% bonus.")
# int(salary) >= 30000 and int(salary) < 70000:
 #   print("You are eligible for a 15% bonus.")
#lif int(salary) >= 70000:
 #   print("You are eligible for a 20% bonus.")  


#2 
#def all_even( a , b ):
 #   for i in range(a,b+1):
  ##      if i%2==0:
    #        print(i)
#all_even(1,20)

#3
'''def digit(a):
    while a>0:
        digit=a%10
        print(digit)
        a=a//10
digit(1234)'''

'''a= 100%5
print(a)
b= 100//5   
print(b)
c=90/3
print(c)'''

#4
'''def count(n):
    sum=0
    sum1=0
    while n>0:
        n=n//10
        sum1=sum1+1
        sum=sum+1
    print("number of digits is :",sum,sum1)
count(859843)

#5
for i in range (1,101):
    if i%3==0 and i%5==0:
        print(i)
 '''       

#6
'''def calculator(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        return "Invalid operator"
result=calculator(10,5,'*')
print("Result is :",result)'''

#7
'''def is_prime(n):
 if n==2:
    return True
 for i in range(2,n-1):
    if n%i==0:
        return false


 return True
print(is_prime(11)). '''

#8
the_digit = 28 
urnumber = int(input("Guess the number: "))
if urnumber == the_digit:
    print("Congratulations! You guessed it right.")
elif urnumber < the_digit:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")   