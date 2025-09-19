import  random
rock = "✊"
paper = "✋"
scissors = "✌️"
game=[rock,paper,scissors]
user_choice=int(input("Enter your choice Type  0 for rock 1,for  2 for paper 3 for scissors"))
if user_choice>=3 or user_choice<0:
    print("Invalid choice. You lose!")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(game[computer_choice])
    #case 1
    if computer_choice==user_choice:
        print("It is draw")
    elif (user_choice==0 and computer_choice==2) or \
     (user_choice==1 and computer_choice==0) or \
     (user_choice==2 and computer_choice==1):
     print("You win ") 
    else:
     print("You lose ") 



