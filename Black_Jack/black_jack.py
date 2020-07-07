# Command to format python file according to the pycodestyle
# autopep8 --in-place --aggressive --aggressive <filename>
import random
import os


# <TODO: compare the list with user total to the dealer and declare the result>


# Creating the Deck
decks_cards = []
for i in range(52):
    decks_cards.append(i)


CLAMPING_CARD = 13
JACK = 11
QUEEN = 12
KING = 13
ACE = 1


class Black_Jack:
    # def __init__(self):
    #    self.globalvariable_is_this = []

    # This function will select two cards for each User in the game in the
    # beginning
    def deal(self):
        hand = []
        for i in range(2):
            random.shuffle(decks_cards)
            card = decks_cards.pop()
            #  print(f"Popped Card without clamp {card}")
            if card > 12:
                # Clamping the value in range of 0 to 12
                card = (card % CLAMPING_CARD)
                #  print(f"Card with clamp is {card}")
            hand.append(card)   # Saving the hand
        return(hand)

# This function will give the total sum of the Players Hand
    def total(self, hand):
        total = 0
        flag = 0
        for card in hand:
            if card == JACK or card == QUEEN or card == KING:
                total += 10
            elif card == ACE:
                flag += 1
            else:
                total += card

        # Covering all the corner cases for the ACE
        #  print(f"Value of the flag is {flag}")
        if flag == 1:
            if total >= 11:
                total += 1
            else:
                total += 11

        elif flag == 2:
            for i in range(2):
                if total >= 11:
                    total += 1
                else:
                    total += 11

        elif flag == 3:
            for i in range(3):
                if total >= 11:
                    total += 1
                else:
                    total += 11

        elif flag == 4:
            for i in range(4):
                if total >= 11:
                    total += 1
                else:
                    total += 11

        #  print(f"Total of the rebased Hand {hand} is {total}")
        return total

    def convert_to_card_value(self, hand):
        hand_rebase = []
        for card in hand:
            card += 1
            hand_rebase.append(card)
        return(hand_rebase)


# This function will handle User's play


    def user(self):
        user_hand = self.deal()
        #  print(f"Hand before doing rebase {user_hand}")
        user_hand = self.convert_to_card_value(user_hand)
        print(
            f"User's Hand after doing rebase {user_hand} with the total of {self.total(user_hand)}")
        while(1):
            choice = input("Do you want to [H]it or [S]tand: ").lower()
            if choice == 'h':
                user_hand = self.hit(user_hand)
                print(
                    f"User's Hand {user_hand} with the Updated total of {self.total(user_hand)}")
                if (self.total(user_hand) > 21):
                    print("User is Busted")
                    break
            else:
                print(f"Final Total of the user is {self.total(user_hand)}")
                break
        return(user_hand)


# This function will be called when user wants to draw 1 more card again


    def hit(self, user_hand):
        card = decks_cards.pop()
        print(f"New Card is {card}")
        if card > 12:
            # Clamping the value in range of 0 to 12
            card = (card % CLAMPING_CARD)
        card += 1
        print(f"Card after doing rebase in hit {card}")
        user_hand.append(card)          # Updating the Hand
        return(user_hand)

# This is the function which will take care of the dealer's  game
    def dealer(self, dealers_hand):
        print(
            f"************Dealer reveals  his/her Hand:{dealers_hand}****************")
        print(f"Total of the Dealer is {self.total(dealers_hand)}")
        while self.total(dealers_hand) < 17:
            dealers_hand = self.hit(dealers_hand)
            print(
                f"Dealer's Hand {dealers_hand} with the Updated total of {self.total(dealers_hand)}")
        return(dealers_hand)

# This function will check the Score and print final verdict of the game
    def score_check(self, final_data):
        h_value = 0
        h_key = 0
        for (key, value) in final_data.items():
            if (self.total(value) > h_value and self.total(value) <= 21):
                h_value = self.total(value)
                h_key = key
                print(key, " :: ", value)
        if (h_value == 21 and h_key == 'Dealer'):
            print(f'{h_key} got Black Jack Users lost the game')
        elif (h_value == 21):
            print(f'{h_key} got Black Jack and won the game')
        print(f'Player who won the game is {h_key} with total of {h_value}')


def game():
    print("--------------Welcome to BLACK_JACK Game-----------------")
    # Total number of player's going to play the game
    players = int(input("Number of User going to play: "))
    dealers_hand = []
    final_data = {}
    count = 0   # To keep count on number of player's playing the game
    object = Black_Jack()
    dealers_hand = object.deal()
    # print(f"Dealer's Hand before rebase is {dealers_hand}")
    dealers_hand = object.convert_to_card_value(dealers_hand)
    # print(f"Dealer's Hand after rebase is {dealers_hand}")
    while (players != 0):
        count += 1
        print("Dealer's First Card is", dealers_hand[0])
        print(
            f"******************* USER-{count} in play ***********************")
        final_data.update({f'User {count}': object.user()})
        players += -1

    dealers_hand = object.dealer(dealers_hand)
    final_data.update({f'Dealer': dealers_hand})
    object.score_check(final_data)
    print(final_data)


if __name__ == '__main__':
    game()
