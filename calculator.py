#calculator
print('1 add')
print('2 sub')
print('3 div')
print('4 mult')
c=int(input("enter the choice"))
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if c==1:
   result=a+b
   print("sum of",a,"+",b,result)
elif c==2:
   result=a-b
   print("sub of",a,"-",b,result)
elif c==3:
   result=a/b
   print("div of",a,"/",b,result)
elif c==4:
   result=a*b
   print("multiplication of",a,"*",b,result)
else:
   print("invalid syntax")
