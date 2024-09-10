                                        #Randomisation
'''import random
random_number=random.randint(1,20)
print(random_number)

random_float=random.random()*5
print(random_float)

random_love=random.randint(0,100)
print(f"Your love Percentage is {random_love}")'''
                                        #Head or Tail
'''import random
random_Head_Tail=random.randint(0,1)
if random_Head_Tail==1:
    print("Head")
else:
    print("Tail")'''
                                        #List
'''USA_States=["New york","California","Maxico","Ohio","Florida"]
USA_States.append("Ali Meesam")
print(USA_States)'''
                                        #BANker Rollete
'''name_string=input("Enter the name with commas")
names=name_string.split(",")
random_items=(len(names))
import random
random_name=random.randint(0,random_items-1)
person_who_will_pay=names[random_name]
print(person_who_will_pay)'''   
                                        #Nested List
'''Fruits=["mango","cherry"]
Vegetables=["carrot","peeach"]
dirt=[Fruits,Vegetables]
print(dirt)'''
                                        #Tresure Map
'''row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
map=[row1,row2,row3]
print(f"{row1}\n,{row2}\n,{row3}\n")
positon=input("Enter the position")
horizontal=int(positon[0])
vertical=int(positon[1])
selected_row=map[vertical-1]
selected_row[horizontal-1]="X"'''
                                            #Rock Paper 
'''user_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors:\n")
import random
computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")

# Convert user_choice to an integer
try:
    user_choice = int(user_choice)
    
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice == user_choice:
        print("It's a draw")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    else:
        print("You lose")
except ValueError:
    print("Invalid input! Please enter 0, 1, or 2.")'''
                        #PRACTISE
                        #rollette
'''name=input("enter the names")
Names=name.split(",")
random_items=len(Names)
import random
random_name=random.randint(0,random_items-1)
who_will_pay=Names[random_name]
print(who_will_pay)'''
