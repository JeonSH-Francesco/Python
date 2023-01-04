
print("-"*20)
a=float(input("Input Number1 : "))
b=float(input("Input Number2 : "))
print("-"*20)


print("Select Calculator Mode")
print("1.Plus\n"\
    "2.Minus\n"\
    "3.Multiply\n"\
    "4.Divide\n")

try:
    oper=int(input("Input Number(1,2,3,4) : "))
    if oper==1 or oper ==2 or oper ==3 or oper ==4:
        mode = int(oper)
    else:
        print("Select only 1,2,3,4")
except ValueError:
    print("Select only 1,2,3,4~!!!")

print("\n")

if mode==1:
    print(a,"+",b,"=",a+b)
elif mode==2:
    print(a,"-",b,"=",a-b)
elif mode==3:
    print(a,"*",b,"=",a*b)
elif mode==4:
    try:
        print(a,"/",b,"=",a/b)
    except ZeroDivisionError:
        print("Don't divide 0")
    
else:
    print("Something was wrong. Please check again~")
