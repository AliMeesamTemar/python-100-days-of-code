                                    #IF Else Statement
'''height=input("Enter the height:")
Height=int(height)
if Height>=120:
    print("You can take a ride  ride")
else:
    print("You cannot take a ride")'''
                                    #Even and Odd
'''x=input("Enter the number:")
num=int(x)
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")'''
                                    #Nasted iF else Statemen
'''A = input("Enter the height in cm: ")
B = input("Enter the age: ")
Height = int(A)
Age = int(B)

if Height > 120:
    print("You can ride")
    if Age < 18:
        bill = 12
        print("You have to pay $12")
    elif Age < 12:
        bill = 5
        print("You have to pay $5")
    elif Age>45 and Age<55:
        bill=0
    print("They ride free")
elif Age<5:
        bill = 7
        print("You have to pay $7")
    
C=input("Do you want to take a photo? (Y/N): ")
if C == "Y":
        bill += 3
        print("You have to pay an additional $3 for the photo")
    
        print(f"Your total bill is ${bill}")
else:
        print("You cannot ride")'''

                                   #BMI Calculator
'''W=input("enter the weight=")
H=input("enter the height=")
A=int(W)
B=float(H)**2
BMI=A/B
if BMI<18.5:
    print(f"your bmi is {BMI},They are underweight")
elif BMI<25:
    print(f"your bmi is {BMI},They are normal")
elif BMI<30:
    print(f"your bmi is {BMI},They are overweight")
elif BMI<35:
    print(f"your bmi is {BMI},They are obese")
else:
    print(f"your bmi is {BMI},They are clinically Obese")'''
                                #Leap year
'''year = input("Enter the year: ")
Year = int(year)

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")'''
#Pizzar
'''Size=input("what you want o buy?(S/L/M)")
Bill=0
if Size=="S":
 Bill+=15
elif Size=="L":
  Bill+=20
  
elif Size=="M":
  Bill+=25
else:
  print("invalid")
Add_pepproni=input("Add pepproni? (Y/N)")
if Add_pepproni=="Y":
 if Size=="S":
   Bill+=1
 else:
   Bill+=2
Extra_cheese=input("extra cheese? (Y/S)")

if Extra_cheese=="Y":
  Bill+=3
else:
  print("invalid")
print(f"Your total Bill IS {Bill}")'''
#LOVE CALCULATOR
'''x=input("Enter the first name=")
y=input("Enter the second name=")
combined_string=x+y
lower_case_string=combined_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
print(love_score)'''
                                                #Welcome to the tressure box
'''print("WELCOME TO THE TRESSURE BOX")
x=input("you want to go left or right? R/L=")
if   x=="R":
    print("Game over")
elif x=="L":
     print("Game continu")
     y=input("Do you want to swim or wait? S/W=")
if   y=="S":
    print("Game over")
elif y=="W":
    print("Game continu")
z=input("which door you want open Red or Yellow or Blue? R/Y/B=")
if z=="R" and z=="B":
    print("Game over")
else:
    print("You win")'''





