num1=int(input("Enter first number:"))
sign=input("Enter a sign:")
num2=int(input("Enter second number:"))
if sign=='+':
      print("Ans=",num1+num2)
elif sign=='-':
      print("Ans=",num1-num2)
elif sign=='*':
      print("Ans=",num1*num2)
elif sign=='/':
      print("Ans=",num1/num2)
else:
    print("Enter valid sign")
