
"""
Spyder Editor

This is a temporary script file.
"""
print("輸入國中會考成績:")

A=int(input("國文: "))
B=int(input("英文: "))
C=int(input("數學: "))
D=int(input("社會: "))
E=int(input("自然: "))
print("")
a=[A,B,C,D,E]
AA=0
BB=0
CC=0
for i in range(0,5):
   if a[i]>94 and a[i]<101:    
       a[i]="A++"
       AA=AA+1
   elif a[i]<95 and a[i]>90:
       a[i]="A+"
       AA=AA+1
   elif a[i]<91 and a[i]>84:
       a[i]="A"
       AA=AA+1
   elif a[i]<85 and a[i]>71:
       a[i]="B++"
       BB=BB+1
   elif a[i]<72 and a[i]>63:
       a[i]="B+"
       BB=BB+1
   elif a[i]<64 and a[i]>41:
       a[i]="B"
       BB=BB+1
   elif a[i]<42 and a[i]>-1:
       a[i]="C"
       CC=CC+1
   else:
       a[i]="ERROR"
   
print("國文:",a[0])
print("英文:",a[1])
print("數學:",a[2])
print("社會:",a[3])
print("自然:",a[4])
print("等級: ",end="")
if AA>0:
    print(AA,"A ",end="")
if BB>0:
    print(BB,"B ",end="")
if CC>0:
    print(CC,"C ",end="")
    