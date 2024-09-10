                                                #Loop
'''Fruits=["Apple","Peach","Pear"]
for Fruit in Fruits:
    print(Fruit)
    print(Fruit + " " "Ali")
    print(Fruits)
print("Ali")'''
                                                #Averge Height
'''Height=input("Enter the height of students").split()
for n in range(0, len(Height)):
 Height[n]=int(Height[n])
print(Height)
Total_height=sum(Height)
Total_len=len(Height)
Average_Height=Total_height/Total_len
print(Average_Height)'''
                                                #Highest Number
'''High_score=input("ENter the score=").split()
for n in range(0, len(High_score)):
    High_score[n]=int(High_score[n])
print(High_score)
Highest_score=0
for score in High_score:
    if score > Highest_score:
        Highest_score=score
        print(f"The highest score in the class {Highest_score}")'''
    
                                            #Range in LOop
'''num=0
for number in range(0,100,5):
    num += number
    print(num)'''
                                            #Sum of Even number
'''total=0
for num in range(1,101):
    if num%2==0:
        total=total+num
print(total)'''
                                            #FIZZBUZZ Game
'''for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)'''
                                            #Password Generator
'''import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['@','#','!','$','^','&','*','~']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("WELCOME TO THE PASSWORD GENERATOR")
Letters=int(input(f"How many letters would you like in password  {letters}\n"))
Symbols=int(input(f"How many symbols would you like in password  {symbols}\n"))
Numbers=int(input(f"How many numbers would you like in password {numbers}\n"))
Password=""
for char in range(0,Letters+1):
    random_choice=random.choice(letters)
    Password+=random_choice
for char in range(0,Symbols+1):
    random_choice=random.choice(symbols)
    Password+=random_choice
for char in range(0,Numbers+1):
    random_choice=random.choice(numbers)
    Password+=random_choice
print(Password)'''
                                            #practise
'''students=["ali","yousaf","hasnat","ibrahim"]
for n in students:
    print(n)'''
                            #Average Height
'''height=input("enter the height of students").split()
for n in range(0,len(height)):
    height[n]=int(height[n])
    print(height[n])
Total=sum(height)
total_len=len(height)
Averge=Total/total_len
print(Averge)'''
                                #Highest Numbers
'''numbers=input("enter the numbers").split()
for num in range(0,len(numbers)):
    numbers[num]=int(numbers[num])
print(numbers)
Max=max(numbers)
print(Max)'''
                                    #
'''import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['@','#','!','$','^','&','*','~']
numbers=['0','1','2','3','4','5','6','7','8','9']
print("WELCOME TO THE PASSWORD GENERATOR")
Letters=int(input(f"How many letters would you like in password  {letters}\n"))
Symbols=int(input(f"How many symbols would you like in password  {symbols}\n"))
Numbers=int(input(f"How many numbers would you like in password {numbers}\n"))
password=""
for char in range(0,Letters+1):
    random_choice=random.choice(letters)
    password+=random_choice
for char in range(0,Symbols+1):
    random_choice=random.choice(symbols)
    password+=random_choice
for char in range(0,Numbers+1):
    random_choice=random.choice(numbers)
    password+=random_choice
print(password)'''

