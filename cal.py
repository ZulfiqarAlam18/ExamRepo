#a=10
#b=20
a = int(input("Enter First Number:"))
op= input("Enter Operator:")[0]
b = int(input("Enter Second Number:"))

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