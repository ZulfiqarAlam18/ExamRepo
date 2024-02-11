#a=10
#b=20
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))

op=input("Enter Operator :")[0]

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='/':
    print(a/b)
elif op =='*':
    print(a*b)
else:
    print("Error:Invalid operator")