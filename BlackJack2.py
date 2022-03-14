import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
busted = False
flag = ''

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card_from_deck = self.deck.pop(0)
        return card_from_deck


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21:
            values['Ace'] = 1

    def __str__(self):
        hand_comp = ''  # start with an empty string
        for card in self.cards:
            hand_comp += '\n ' + card.__str__()  # add each Card object's print string
        return hand_comp

    def check_busted(self):

        if self.value > 21:
            busted = True
        else:
            busted = False

        return busted


class Account:

    def __init__(self):
        self.total = 200  # set to a default value
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet * 2
        print('You won!')

    def lose_bet(self):
        self.total = self.total - self.bet


def take_bet(conta):

    while True:
        try:
            conta.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if conta.bet > conta.total:
                print(f"Sorry, your bet can't exceed {conta.total}")
            else:
                break

def deal_cards():
    for x in range(2):
        a = my_deck.deal()
        b = my_deck.deal()

        my_hand.cards.append(a)
        my_hand.add_card(a)

        dealer_hand.cards.append(b)
        dealer_hand.add_card(b)

def display_secret():


    print('Dealers hand:\nSecret card\n' + dealer_hand.cards[0].__str__())
    print('\nYour hand:' + my_hand.__str__())

def compare():
    if (21 - dealer_hand.value) < (21 - my_hand.value):
        print('You lost!')
        my_account.lose_bet()
    elif (21 - dealer_hand.value) > (21 - my_hand.value):
        print('You win!')
        my_account.win_bet()
    else:
        print("It's a tie!")



#Preparo #Prep
print('\n'*100)
print("Welcome to BlackJack!")
my_deck = Deck()
my_hand = Hand()
dealer_hand = Hand()
my_account = Account()
game_on = 'Y'

#Lógica de jogo #Gameplay
while my_account.total > 0 and game_on == 'Y':
    my_hand.cards = []
    dealer_hand.cards = []
    my_hand.value = 0
    dealer_hand.value = 0
    take_bet(my_account)
    my_deck.shuffle()
    deal_cards()
    display_secret()


    if my_hand.check_busted():
        print('Player BUSTED!')
        my_account.lose_bet()
        game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
        if game_on == 'N':
            print('Game over')
            break
        else:
            continue
    else:
        choice = input('Do you wanna (H)it or (S)tay?').upper()
        if choice == 'S':

            if dealer_hand.check_busted():
                print('Dealer BUSTED!')
                my_account.win_bet()
                game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                if game_on == 'N':
                    print('Game over')
                    break
                else:
                    continue
            else:
                while dealer_hand.value <= 16:
                    d = my_deck.deck.pop(0)
                    dealer_hand.cards.append(d)
                    dealer_hand.add_card(d)

                    if dealer_hand.check_busted():
                        print('Dealer BUSTED!')
                        my_account.win_bet()
                        game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                        if game_on == 'N':
                            print('Game over')
                            flag = 'exit'
                            break
                        else:
                            flag = 'cont'

                if flag == 'exit':
                    break
                elif flag == 'cont':
                    continue
                else:
                    compare()
                    print(dealer_hand.__str__())
                    print(my_hand.__str__())
                    game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                    if game_on == 'N':
                        #print('Game over')
                        break
                    else:
                        continue

        if choice == 'H':
            flag2 = 'on'
            while flag2 == 'on':
                h = my_deck.deck.pop(0)
                my_hand.cards.append(h)
                my_hand.add_card(h)
                print('Dealers hand:\nSecret card\n' + dealer_hand.cards[0].__str__())
                print('\nYour hand:' + my_hand.__str__())


                if my_hand.check_busted():
                    print('Player BUSTED!')
                    my_account.lose_bet()
                    game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                    if game_on == 'N':
                        print('Game over')
                        flag2 = 'off'
                        break
                    else:
                        flag2 = 'on'
                        break


                choice = input('Do you wanna (H)it or (S)tay?').upper()
                if choice == 'S':

                    if dealer_hand.check_busted():
                        print('Dealer BUSTED!')
                        my_account.win_bet()
                        game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                        if game_on == 'N':
                            print('Game over')
                            flag2 = 'off'
                            break
                        else:
                            flag2 = 'on'
                            break

                    else:
                        while dealer_hand.value <= 16:
                            c = my_deck.deck.pop(0)
                            dealer_hand.cards.append(c)
                            dealer_hand.add_card(c)

                            if dealer_hand.check_busted():
                                print('Dealer BUSTED!')
                                my_account.win_bet()
                                game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                                if game_on == 'N':
                                    print('Game over')
                                    flag2 = 'off'
                                    break
                                else:
                                    flag2 = 'on'
                                    break

                        if flag2 == 'off':
                            break
                        elif flag == 'on':
                            break
                        else:
                            compare()
                            print(dealer_hand.__str__())
                            print(my_hand.__str__())
                            game_on = input('Do you want to keep playing? (Y)es or (N)o?').upper()
                            if game_on == 'N':
                                print('Game over')
                                flag2 = 'off'
                                break
                            else:
                                flag2 = 'on'
                                break

                        if flag2 == 'off':
                            break
                        elif flag == 'on':
                            break

                if choice == 'H':
                    flag2 = 'on'
                    continue

            if flag2 == 'off':
                break
            if flag2 == 'on':
                continue




print('Game Over!')
if my_account.total == 0:
    print('You lost all your money!')





