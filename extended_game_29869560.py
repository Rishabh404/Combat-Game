#This program introduces an extended game which can be fought between two users on a command line interface
#Program Author - Rishabh Singh Kochhar
#Creation date - 3rd August 2018
#Last updated - 24th August 2018

#Some variables that will be used throughout the program have been created below
#Units of the army of both the players are stores in separate lists.
balance = 10 #Initial balance
units = 0 #Initial units
army = [] #Creates an empty list for army, will be later assignes to both the player's army units initially
army_1 = [] #Army of first player
army_2 = [] #Army of second player
medic_balance_1 = 0 #Medic balance of first army
medic_balance_2 = 0 #Medic balance of second army
i = 0
j = 0
a_t = []
b_t = []
print('Greetings Commanders!! This is the start of the extended game to be fought against two players.')
print('Two new features have been implemented in this game - Medics and Expanded Armies.')
print('Medics are allocated at 1$ per medic after the commander doesn\'t wish to purchase further units.')
print('Two mew units have been added - Wizards and Siege Equipment.')
print('Cost of Wizard - 4$, Cost of Siege Equipment = 3$, Cost of Knight and Archer - 2$.')
print('Cost of Soldiers - 1$')
player_one = input('Enter your name, commander 1: ')
player_two = input('Enter your name, commander 2: ')

'''

This function starts the extended game for the first player in this game by greeting him/her
and showing the initial balance and available units(0) initially. Then it calls another function
to initiate the purchase of the units. As a part of this function, if the first player runs out of
10$, it displays it on the screen. Also after the purchase of the units, the remaining balance if
greater than zero is assigned to the medic balance.
No parameters have been defined and no return values have been created for this function.

'''

def func_play_1():
    global army_1
    global army_2
    global medic_balance_1
    global balance
    print('\nHello Commander', player_one)
    print('Your initial balance is 10$. Available units:',units)
    purchase_validation()
    army_1 = army
    if balance>0:
        medic_balance_1 = balance
        print('Your remaining amount has been assigned as medic balance amounting to',medic_balance_1,'dollars')
        balance = 0

    elif balance==0:
        print('Insufficient funds to make a further purchase')

'''

This function starts the extended game for the second player in this game by greeting him/her
and showing the initial balance and available units(0) initially. Then it calls another function
to initiate the purchase of the units. As a part of this function, if the second player runs out of
10$, it displays it on the screen. Also after the purchase of the units, the remaining balance if
greater than zero is assigned to the medic balance.
No parameters have been defined and no return values have been created for this function.

'''

def func_play_2():
    global balance
    global units
    global army
    global unit
    global army_1
    global army_2
    global medic_balance_2
    balance = 10
    units = 0
    army = []
    unit = ''
    print('\nHello Commander', player_two)
    print('Your initial balance is 10$. Available units:',units)
    purchase_validation()
    army_2 = army
    if balance>0:
        medic_balance_2 = balance
        print('Your remaining amount has been assigned as medic balance amounting to',medic_balance_2,'dollars')
        balance = 0

    elif balance==0:
        print('Insufficient funds to make a further purchase')


'''

This function contains the logic of when the purchase is finalized. It displays the
unit that has been purchased along with the units that may have been purchased earlier
by this player earlier during the same game. After that the balance gets deducted by the
respective amount depending upon the unit and the remaining balance gets displayed on the screen.
Additional logic has been implemented as compared to the basic game, since the price of all the units is
different. Hence the player won't be able to proceed if his/her balance drops below the price of unit
he/she wishes to purchase.
No parameters have been defined and no return values have been created for this function.

'''

def purchase_flow():
    global units
    global balance
    global army
    global purchase
    if  unit.lower() == 'soldier':
        if balance>0:
            balance = balance - 1
            purchase = 'success'
        elif balance==0:
            print('Insufficient funds to purchase Soldier')
            purchase = 'failure'
    elif unit.lower() == 'knight' or unit.lower() == 'archer':
        if balance>=2:
            balance = balance - 2
            purchase = 'success'
        elif balance<2:
            print('Insufficient funds to purchase Archer or Knight')
            purchase = 'failure'
    elif unit.lower() == 'wizard':
        if balance>=4:
            balance = balance - 4
            purchase = 'success'
        elif balance<4:
            print('Insufficient funds to purchase Wizard')
            purchase = 'failure'
    elif unit.lower() == 'siege':
        if balance>=3:
            balance = balance - 3
            purchase = 'success'
        elif balance<3:
            print('Insufficient funds to purchase Siege')
            purchase = 'failure'
    print('Your remaining balance is '+ str(balance)+ '$')

    if purchase == 'success':
        units = units+1
        print('You now have',units, 'units')
        army.append(unit)
        print('Units currently available with you:')
        print('\n'.join(army).title())
    if purchase == 'failure':
        print('Kindly check your balance and look at other options to purchase')

'''
This function gives the option to select the units for the players which can be purchased at the costs
mentioned at the starting of the game. The user inputs the type of unit that he/she wishes to buy.
Case of the input entered does not matter. In case of an invalid input, it recursively calls itself to
prompt the user again to enter the correct input. Also calls another function which dictates what happens
when the purchase is made on player's behalf. No parameters have been defined and no return values have been
created for this function.

'''

def game_purchase():
    global balance
    global units
    global army
    global unit
    x = balance
    while balance == x:
        unit = input('Enter the type of unit you want to purchase from the following: \nArcher, Soldier, Knight, Wizard, Siege \nEnter input here - ')
        if unit.lower() == 'archer':
            purchase_flow()
            if purchase == 'success':
                print('You have successfully purchased an Archer')
        elif unit.lower() == 'soldier':
            purchase_flow()
            if purchase == 'success':
                print('You have successfully purchased a Soldier')
        elif unit.lower() == 'knight':
            purchase_flow()
            if purchase == 'success':
                print('You have successfully purchased a Knight')
        elif unit.lower() == 'wizard':
            purchase_flow()
            if purchase == 'success':
                print('You have successfully purchased a Wizard.')
        elif unit.lower() == 'siege':
            purchase_flow()
            if purchase == 'success':
                print('You have successfully purchased a Siege Equipment')
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

This function defines the medic logic for first player. In this function, it firstly checks the
medic balance assigned to the player. If that balance is greater than zero, it revives the
first player's defeated unit by placing it at the end of the current list in the player's army
and decrements the medic balance by 1$ and displays the remaining medic balance on the screen.
No parameters have been defined and no return values have been created for this function.

'''

def medic_logic_a():
    global a_t
    global medic_balance_1
    if medic_balance_1 >0:
        print('In progress - attempting to revive your unit by calling the Medic')
        print('Commander',player_one,'unit to be revived', a_t[-1])
        prompt_1.append(a_t[-1])
        print('Commander - your',a_t[-1],'has been revived')
        medic_balance_1 = medic_balance_1 - 1
        print(medic_balance_1,'is the remaining medic balance')

'''

This function defines the medic logic for second player. In this function, it firstly checks the
medic balance assigned to the player. If that balance is greater than zero, it revives the
second player's defeated unit by placing it at the end of the current list in the player's army
and decrements the medic balance by 1$ and displays the remaining medic balance on the screen.
No parameters have been defined and no return values have been created for this function.

'''

def medic_logic_b():
    global b_t
    global medic_balance_2
    if medic_balance_2 >0:
        print('In progress - attempting to revive your unit  by calling the Medic')
        print('Commander',player_two,'unit to be revived', b_t[-1])
        prompt_2.append(b_t[-1])
        print('Commander - your',b_t[-1],'has been revived')
        medic_balance_2 = medic_balance_2 - 1
        print(medic_balance_2,'is the remaining medic balance')


'''

This is the main logic of how the game will be played amongst the players when both the  players
consent to continue the game. As long as both the players have the units, it makes the units which
are alive and in the fighting position(in the order of purchase) to fight and gives the logic of
who will win between archers, knights,soldiers,siege equipments and wizards with the help of
if-else statements. Units which have lost are deleted from the list of the player(who has lost)
and stored in another list. It also makes calls to the two medic functions for the two players
depending upon which player unit is defeated.
No parameters have been defined and no return values have been created for this function.

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
    prompt_1 = army_1[:]
    prompt_2 = army_2[:]
    while prompt_1!=[] and prompt_2!= []:
        if prompt_1[i].lower() == prompt_2[j].lower():
            print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
            print('This battle resulted in a tie')
            a_t.append(prompt_1[i])
            b_t.append(prompt_2[j])
            del prompt_1[i]
            del prompt_2[j]
            medic_logic_a()
            medic_logic_b()
        else:
            if prompt_1[i].lower() == 'soldier':
                if prompt_2[j].lower() == 'knight':
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_one,'wins this battle')
                    b_t.append(prompt_2[j])
                    del prompt_2[j]
                    medic_logic_b()
                else:
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_two,'wins this battle')
                    a_t.append(prompt_1[i])
                    del prompt_1[i]
                    medic_logic_a()
            elif prompt_1[i].lower() == 'archer':
                if prompt_2[j].lower() == 'soldier' or prompt_2[j].lower() == 'wizard':
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_one,'wins this battle')
                    b_t.append(prompt_2[j])
                    del prompt_2[j]
                    medic_logic_b()
                else:
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_two,'wins this battle')
                    a_t.append(prompt_1[i])
                    del prompt_1[i]
                    medic_logic_a()
            elif prompt_1[i].lower() == 'knight':
                if prompt_2[j].lower() == 'archer' or prompt_2[j] == 'siege':
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_one,'wins this battle')
                    b_t.append(prompt_2[j])
                    del prompt_2[j]
                    medic_logic_b()
                else:
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_two,'wins this battle')
                    a_t.append(prompt_1[i])
                    del prompt_1[i]
                    medic_logic_a()
            elif prompt_1[i].lower() == 'siege':
                if prompt_2[j].lower() == 'knight' or prompt_2[j].lower() == 'wizard':
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_two,'wins this battle')
                    a_t.append(prompt_1[i])
                    del prompt_1[i]
                    medic_logic_a()
                else:
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_one,'wins this battle')
                    b_t.append(prompt_2[j])
                    del prompt_2[j]
                    medic_logic_b()
            elif prompt_1[i].lower() == 'wizard':
                if prompt_2[j].lower() == 'archer':
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_two,'wins this battle')
                    a_t.append(prompt_1[i])
                    del prompt_1[i]
                    medic_logic_a()
                else:
                    print('Commander '+player_one+'\'s'+' '+prompt_1[i]+' vs Commander '+player_two+'\'s'+' '+prompt_2[j])
                    print(player_one,'wins this battle')
                    b_t.append(prompt_2[j])
                    del prompt_2[j]
                    medic_logic_b()
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
        print('\nGame - Advanced Version\n')
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
                print('Proceeding..')
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
