############## - Input snippet
import random
str = "RPS"
c = random.choice(str)

print("\n\n*************************** Rock-Paper-Scissors ***************************")

u = input('''\nChoose one of the following -
('R' for Rock, 'P' for Paper, 'S' for Scissors)
Enter your choice here: ''')

############# - Game logic snippet
def user_won(u,c):
        if c=='R':
            if u=='P':
                print('\n"Paper beats Rock"')
                return True
            else :
                print('\n"Rock beats Scissors')
                return False
        elif c=='P':
            if u=='R':
                print('\n"Paper beats Rock"')
                return False
            else :
                print('\n"Scissors beats Paper')
                return True
        else :
            if u=='P':
                print('\n"Scissors beats Paper')
                return False
            else :
                print('\n"Rock beats Scissors')
                return True

############# - Output snippet
if u!='R' and u!='P' and u!='S':
    print("\nINVALID CHOICE")
else :
    print("\nYou chose: ",u )
    print("Computer chose: ",c)

    if u==c:
        print("Tie! Try again.")
    else :
        if user_won(u,c):
            print("\nCheers! You won.")
        else :
            print("\nSorry! You lost.")

print("\n******************************** Game over ********************************\n")