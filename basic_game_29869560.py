#This program introduces a basic game which can be fought between two users on a command line interface
#Program Author - Rishabh Singh Kochhar
#Creation date - 3rd August 2018
#Last updated - 24th August 2018

#Some variables that will be used throughout the program have been created below
#Units of the army of both the players are stores in separate lists.
balance = 10
units = 0
army = [] #Creates an empty list for army, will be later assignes to both the player's army units initially
army_1 = [] #Units of first player's army will be stored here
army_2 = [] #Units of second player's army will be stored here
i = 0
j = 0
a_t = []
b_t = []
print('Greetings Commanders!! This is the start of the basic game to be fought against two players')
player_one = input('Enter your name, commander 1: ')
player_two = input('Enter your name, commander 2: ')

'''

This function starts the basic game for the first player in this game by greeting him/her
and showing the initial balance and available units(0) initially. Then it calls another function
to initiate the purchase of the units. As a part of this function, if the first player runs out of
10$, it displays it on the screen. No parameters have been defined and no return values have been
created for this function.

'''

def func_play_1():
    global army_1
    global army_2
    print('\nHello Commander', player_one)
    print('This game has three units available for fighting:')
    print('Archer, Soldier, Knight')
    print('Units are available at 1$ each')
    print('Your initial balance is 10$. Number of available units:',units)
    purchase_validation()
    army_1 = army #empty list assigned to first player's units

    if balance==0:
        print('Insufficient funds to make a further purchase')

'''

This function starts the basic game for the second player in this game by greeting him/her
and showing the initial balance and available units(0) initially. Then it calls another function
to initiate the purchase of the units. As a part of this function, if the second player runs out of
10$, it displays it on the screen. No parameters have been defined and no return values have been
created for this function.

'''

def func_play_2():
    global balance
    global units
    global army
    global unit
    global army_1
    global army_2
    balance = 10
    units = 0
    army = []
    unit = ''
    print('\nHello Commander', player_two)
    print('Your initial balance is 10$. Available units:',units)
    purchase_validation()
    army_2 = army #empty list assigned to second player's units

    if balance==0:
        print('Insufficient funds to make a further purchase')

'''

This function contains the logic of when the purchase is finalized. It displays the
unit that has been purchased along with the units that may have been purchased earlier
by this player earlier during the same game. After that the balance gets deducted by 1$
and the remaining balance gets displayed on the screen. No parameters have been defined and
no return values have been created for this function.

'''

def purchase_flow():
    global units
    global balance
    global army
    units = units+1
    print('You now have',units, 'units')
    army.append(unit)
    print('Units currently available with you:')
    print('\n'.join(army))
    balance = balance - 1
    print('Your remaining balance is '+ str(balance)+ '$')

'''
This function gives the option to select the units for the players which can be purchased at 1$ each.
The user inputs the type of unit that he/she wishes to buy. Case of the input entered does not matter.
In case of an invalid input, it recursively calls itself to prompt the user again to enter the correct
input. Also calls another function which dictates what happens when the purchase is made on player's
behalf. No parameters have been defined and no return values have been created for this function.

'''

def game_purchase():
    global balance
    global units
    global army
    global unit
    x = balance
    while balance == x:
        unit = input('Enter the type of unit you want to purchase from the following: \nArcher, Soldier, Knight \nEnter input here - ')
        if unit.lower() == 'archer':
            print('You have purchased an Archer')
            purchase_flow()
        elif unit.lower() == 'soldier':
            print('You have purchased a Soldier')
            purchase_flow()
        elif unit.lower() == 'knight':
            print('You have purchased a Knight')
            purchase_flow()
        else:
            print('Kindly enter a valid input')
            game_purchase()

'''

This function asks the player whether he/she wishes to make a purchase to proceed further.
This function is placed at strategic points in the program which will dictate when the user wishes
to break out of the purchase cycle and start the game. No parameters have been defined and
no return values have been created for this function.

'''
def purchase_wish():
    global unit_purchase
    unit_purchase = input('\nDo you wish to make a purchase?[Y/N]- ')

'''

This is the main logic of how the game will be played amongst the players when both the  players
consent to continue the game. As long as both the players have the units, it makes the units which
are alive and in the fighting position(in the order of purchase) to fight and gives the logic of
who will win between archers, knights and soldiers with the help of if-else statements. Units which
have lost are deleted from the list of the player(who has lost) and stored in another list.

'''


def game_logic():
    global i
    global j
    i = 0
    j = 0
    global a_t
    global b_t
    global prompt_1
    global prompt_2
    prompt_1 = army_1
    prompt_2 = army_2
    while prompt_1!=[] and prompt_2!= []:
        if (prompt_1[i].lower() == 'archer' and prompt_2[j].lower() == 'soldier') or (prompt_1[i].lower() == 'soldier' and prompt_2[j].lower() == 'archer'):
            if (prompt_1[i].lower() == 'archer'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_one,' wins this battle')
                b_t = prompt_2[j]
                del prompt_2[j]

            elif (prompt_2[i].lower() == 'archer'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_two,'wins this battle')
                a_t = prompt_1[i]
                del prompt_1[i]


        elif (prompt_1[i].lower() == 'knight' and prompt_2[j].lower() == 'soldier') or (prompt_1[i].lower() == 'soldier' and prompt_2[j].lower() == 'knight'):
            if (prompt_1[i].lower() == 'soldier'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_one,'wins this battle')
                b_t = prompt_2[j]
                del prompt_2[j]

            elif (prompt_2[i].lower() == 'soldier'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_two,'wins this battle')
                a_t = prompt_1[i]
                del prompt_1[i]

        elif (prompt_1[i].lower() == 'archer' and prompt_2[j].lower() == 'knight') or (prompt_1[i].lower() == 'knight' and prompt_2[j].lower() == 'archer'):
            if (prompt_1[i].lower() == 'knight'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_one,'wins this battle')
                b_t = prompt_2[j]
                del prompt_2[j]

            elif (prompt_2[i].lower() == 'knight'):
                print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                print('Commander',player_two,'wins this battle')
                a_t = prompt_1[i]
                del prompt_1[i]

        elif prompt_1[i].lower()==prompt_2[j].lower():
            print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
            print('This battle resulted in a tie')
            a_t = prompt_1[i]
            b_t = prompt_2[j]
            del prompt_1[i]
            del prompt_2[j]

        print('\n')


'''

This function gets called after the players have made their respective purchases.
It prompts on the screen whether the users wish to continue the game after the purchase.
Depending on the given input, it either takes them to the game or terminates the game
here itself if any player does not wish to continue. It also checks the validation of the
input entered. No parameters have been defined and no return values have been created for
this function.

'''
def game_proceed():
    global play_game1
    global play_game2
    play_game1 = input('\nCommander'+' '+str(player_one.title())+' '+'Continue to the game?[Y/N] ')
    play_game2 = input('\nCommander'+' '+str(player_two.title())+' '+'Continue to the game?[Y/N] ')
    if play_game1.lower() == 'y' and play_game2.lower() == 'y':
        print('\nGame - Basic Version\n')
        game_logic()
    elif play_game1.lower() == 'y' and play_game2.lower() == 'n':
        print('\nCommander',player_one,'has won this game since commander',player_two,'has quit.')
    elif play_game1.lower() == 'n' and play_game2.lower() == 'y':
        print('\nCommander',player_two,'has won this game since commander',player_one,'has quit.')
    elif play_game1.lower() == 'n' and play_game2.lower() == 'n':
        print('Both the players have quit the game, hence it is a tie with no winners')
    elif play_game1.lower()!='y' or play_game1.lower()!='n':
        print('Kindly enter a valid input')
        game_proceed()
    elif play_game2.lower()!='y' or play_game2.lower()!='n':
        print('Kindly enter a valid input')
        game_proceed()

'''

This function validates the input provided by the user to make a purchase in this game.
This function recursively calls itself in case invalid user input is encountered.Apart from
that it also checks the balance remaining for the player so he/she won't be able to continue purchasing
the units in case the balance drops to 0. In addition, it calls two other functions, one asking the
player if he/she wishes to make a purchase to continue further and the other one asking the
player to select the units which he/she wishes to purchase. No parameters have been defined
and no return values have been created for this function.

'''

def purchase_validation():
    purchase_wish()
    if unit_purchase.lower() == 'y':
        while balance>0 and unit_purchase.lower() == 'y':
            game_purchase()
            purchase_wish()
            if unit_purchase.lower()=='n':
                continue
            elif unit_purchase.lower() == 'y':
                continue
            elif unit_purchase.lower()!='y' or unit_purchase.lower()!='n':
                print('Kindly enter a valid input')
                purchase_validation()
    elif unit_purchase.lower() == 'n':
        print('Proceeding..')
    elif unit_purchase.lower()!='y' or unit_purchase.lower()!='n':
        print('Kindly enter a valid input')
        purchase_validation()

#The below functions are called in the sequence for the game play
func_play_1()
func_play_2()
game_proceed()

#Based on how many units remain for the player after fighting the following logic is executed
if play_game1.lower() == 'y' and play_game2.lower() == 'y':
    if prompt_1 == [] and prompt_2!= []:
        print('\nCommander',player_two,'has won this war')
    elif prompt_2 == [] and prompt_1!= []:
        print('\nCommander',player_one,'has won this war')
    elif prompt_1 == [] and prompt_2 == []:
        print('\nThis war resulted in a tie')


'''

REFERENCES

1.	More Control Flow Tools – Python 3.7.0 Documentation. Retrieved from
    https://docs.python.org/3/tutorial/controlflow.html
2.	“Can only join an iterable” python error. Retrieved from
    https://stackoverflow.com/questions/32144173/can-only-join-an-iterable-python-error
3.	Understanding Lists in Python 3. Retrieved from
    https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3
4.	Python tips - How to easily convert a list to a string for display. Retrieved from
    https://www.decalage.info/en/python/print_list
5.	Using global variables in function. Retrieved from
    https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
6.	How do I do a case-insensitive string comparison? Retrieved from
    https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison


'''
