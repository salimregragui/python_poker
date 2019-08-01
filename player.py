import deck

class Player:
    """Player Class"""
    def __init__(self, money, name):
        self.hand = []
        self.money = money
        self.name = name
        self.state = "Playing"
        self.status = ""
        self.current_call = 0

    def calling(self, money_to_call):
        if self.money - money_to_call > 0:
            self.money = self.money - money_to_call
            return "Called"
        elif self.money - money_to_call == 0:
            self.money = self.money - money_to_call
            return "All in"
        else:
            return "Invalid"

    def raising(self, money_bet, money_to_raise):
        if self.money - money_to_raise >= 0:
            self.money = self.money - money_to_raise
            return ("Raised", money_to_raise)
        else:
            self.calling(money_bet)

    def folding(self):
        self.hand = []
        self.state = "Folded"

    def checking(self):
        return "Checked"

    def pay_small_blind(self, value):
        if self.money - value >= 0:
            self.money -= value
            return value
        else:
            self.folding()

    def pay_big_blind(self, value):
        if self.money - value >= 0:
            self.money -= value
            return value
        else:
            self.folding()

    def show_hand(self, state):
        status = "NONE" if self.status == "" else self.status
        if state == "Hidden" or status == "Folded": #if we are not in a showdown or the player has folded we don't show his cards
            print("-------  -------")
            print(f"|     |  |     | PLAYER : {self.name}")
            print(f"|     |  |     | MONEY : {self.money}")
            print(f"|     |  |     | STATUS : {status}")
            print("-------  -------")

        elif state == "Shown" and status != "Folded": #if we are in a showdown and the player hasn't folded we show his cards
            card1 = f"{self.hand[0].value} " if self.hand[0].value < 10 else f"{self.hand[0].value}"
            card2 = f"{self.hand[1].value} " if self.hand[1].value < 10 else f"{self.hand[1].value}"

            cards = [card1, card2]

            for i in range(2): #for each card from the two if it's an 11 a 12 a 13 or a 1 we turn it to it's showing value
                if(cards[i] == "11"):
                    cards[i] = "J "
                elif(cards[i] == "12"):
                    cards[i] = "Q "
                elif(cards[i] == "13"):
                    cards[i] = "K "
                elif(cards[i] == "1 "):
                    cards[i] = "A "

            print("-------  -------")
            print(f"|{cards[0]}   |  |{cards[1]}   | PLAYER : {self.name}")
            print(f"|  {self.hand[0].suit[0]}  |  |  {self.hand[1].suit[0]}  | MONEY : {self.money}")
            print(f"|   {cards[0]}|  |   {cards[1]}| STATUS : {status}")
            print("-------  -------")

    def hand_power(self, table):
        if self.status != "Folded":
            list_of_cards = self.hand + table
            suits = [suit.suit for suit in list_of_cards] #we get all the suits of the cards
            values = [value.value for value in list_of_cards] #we get all the values of the card
            best_hand = [] #best hand of the player

            values.sort() #we sort the values

            #booleans to check wich hand the player has
            check_brelan = False
            check_pair = False
            check_four_kind = False
            check_double_pair = False
            check_full_house = False
            check_flush = False
            check_straight = False
            check_royal_straight = False
            check_straight_flush = False
            check_royal_flush = False
            check_pair_value = 0

            straight_list = list(dict.fromkeys(values)) #removing duplicates from the values

            if straight_list[0] == 1: #as the As can be both one and 14 we add it to the list
                straight_list.append(14)

            straight_counter = 1 #the counter of followed numbers
            current_number = straight_list[0]  #the number that we check
            best_hand.append(current_number)

            for i in range(len(straight_list)):

                if straight_counter == 5 and straight_list[i] != current_number + 1: #if we found 5 followed numbers
                    break
                elif straight_list[i] == current_number + 1 and i != 0: #if the number is equal to +1 the number before (exp 2=> 3)
                    straight_counter += 1
                    current_number = straight_list[i]
                    best_hand.append(current_number)

                elif straight_list[i] != current_number + 1:#if the number is different from the number before +1 exp(2=>4)
                    straight_counter = 1
                    current_number = straight_list[i]
                    best_hand.clear()
                    best_hand.append(current_number)

            if straight_counter >= 5 and current_number != 14:
                check_straight = True
            elif straight_counter >= 5 and current_number == 14:
                check_royal_straight = True
            elif straight_counter < 5:
                best_hand = []

            if check_royal_straight: #if we have a possible royal straight we check the color of the suit
                royal_flush_check = [card for card in list_of_cards]
                royal_check_counter = 1
                color_check = max(suits, key=suits.count) #checking the most predominant color

                for card in reversed(royal_flush_check):
                    if card.value == 10 and card.suit == color_check or card.value == 11 and card.suit == color_check or card.value == 12 and card.suit == color_check or card.value == 13 and card.suit == color_check:
                        royal_check_counter += 1

                if royal_check_counter >= 5:
                    check_royal_flush = True
                else:
                    check_royal_flush = False
                    check_straight = True

            #checking if it's a straight flush
            if check_straight:
                straight_flush_check = [card for card in list_of_cards]
                straight_flush_check = sorted(straight_flush_check, key=lambda card: card.value)
                straight_flush_counter = 0
                current_straight_num = straight_list[0]
                color_check = max(suits, key=suits.count) #checking the most predominant color

                for i in range(len(straight_flush_check)):

                    if straight_flush_counter == 5 and straight_flush_check[i].value != current_straight_num + 1: #if we found 5 followed numbers
                        break
                    elif straight_flush_check[i].value == current_straight_num + 1 and straight_flush_check[i].suit == color_check and i != 0: #if the number is equal to +1 the number before (exp 2=> 3)
                        straight_flush_counter += 1
                        current_straight_num = straight_flush_check[i].value

                    elif straight_flush_check[i].value != current_straight_num + 1:
                        straight_flush_counter = 0
                        current_straight_num = straight_flush_check[i].value

                if straight_flush_counter >= 5:
                    check_straight_flush = True

            #checking if it's a flush
            for j in range(len(suits)):
                if suits.count(suits[j]) == 5:
                    check_flush = True
                    flush_color = suits[j]

            if check_flush:
                for i,card in enumerate(list_of_cards):
                    if(card.suit == flush_color):
                        best_hand.append(card.value)

            if not best_hand:
                check_hand = True
            else:
                check_hand = False

            for i in range(len(values)):
                if values.count(values[i]) == 2 and check_pair_value == 0:
                    check_pair = True
                    check_pair_value = values[i]
                    if check_hand and not best_hand:
                        best_hand.append(values[i])
                        best_hand.append(values[i])

                elif values.count(values[i]) == 2 and check_pair_value != values[i]:
                    check_double_pair = True
                    if check_hand and len(best_hand) == 2:
                        best_hand.append(values[i])
                        best_hand.append(values[i])

                elif values.count(values[i]) == 3 and not check_pair:
                    check_brelan = True
                    if check_hand and not best_hand:
                        best_hand.append(values[i])
                        best_hand.append(values[i])
                        best_hand.append(values[i])

                elif values.count(values[i]) == 4:
                    check_four_kind = True
                    if check_hand and not best_hand:
                        best_hand.append(values[i])
                        best_hand.append(values[i])
                        best_hand.append(values[i])
                        best_hand.append(values[i])

                elif values.count(values[i]) == 3 and check_pair:
                    check_full_house = True
                    if check_hand and len(best_hand) == 2:
                        best_hand.append(values[i])
                        best_hand.append(values[i])
                        best_hand.append(values[i])

                elif values.count(values[i]) == 2 and check_brelan:
                    check_full_house = True
                    if check_hand and len(best_hand) == 3:
                        best_hand.append(values[i])
                        best_hand.append(values[i])

            if self.hand[0].value not in best_hand:
                best_hand.append(self.hand[0].value)

            if self.hand[1].value not in best_hand:
                best_hand.append(self.hand[1].value)

            best_hand = [14 if x == 1 else x for x in best_hand]

            if check_royal_flush:
                return ("Royal Flush", 1.0 * 100, best_hand)
            elif check_straight_flush:
                return ("Straight Flush", 0.9 * 100, best_hand)
            elif check_four_kind:
                return ("Four of a kind", 0.8 * 100, best_hand)
            elif check_full_house:
                return ("Full House", 0.7 * 100, best_hand)
            elif check_flush:
                return ("Flush", 0.6 * 100, best_hand)
            elif check_straight:
                return ("Straight", 0.5 * 100, best_hand)
            elif check_brelan:
                return ("Three of a kind", 0.4 * 100, best_hand)
            elif check_double_pair:
                return ("Double Pair", 0.3 * 100, best_hand)
            elif check_pair:
                return ("Pair", 0.2 * 100, best_hand)
            else:
                best = [14 if x.value == 1 else x.value for x in self.hand]

                best_hand.clear()
                best_hand.append(max(best))
                return ("High Card", 0.1 * 100, best_hand)

        else:
            return 0
