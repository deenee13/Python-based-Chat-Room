CLAMPING_CARD = 13
JACK = 11
QUEEN = 12
KING = 13
ACE = 1


# This function will give the total sum of the Players Hand
def total(hand):
    total = 0
    flag = 0
    print(f"Hand before doing rebase {hand}")
    hand = convert_to_card_value(hand)
    print(f"Hand after doing rebase {hand}")
    for card in hand:
        if card == JACK or card == QUEEN or card == KING:
            total += 10
        elif card == ACE:
            flag += 1
        else:
            total += card

    # Covering all the corner cases for the ACE
    print(f"Value of the flag is {flag}")
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

    print(f"Total of the Hand {hand} is {total}")
    return total


def convert_to_card_value(hand):
    hand_rebase = []
    for card in hand:
        card += 1
        hand_rebase.append(card)
    return(hand_rebase)
    print(hand)

# This function will check the Score and print final verdict of the game
def score_check(final_data):
            for (key, value) in final_data.items() :
                print(key , " :: ", value )


if __name__ == '__main__':
    hand = {'User 1': [1, 2, 3] , 'User 2' : [4, 5, 6] , 'User 3' : [7, 8, 9]}
    score_check(hand)
