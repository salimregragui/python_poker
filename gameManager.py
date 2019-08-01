import os
import player
import table
import deck
import handProbability

class GameManager:
    """Class that manages all the game including the states"""
    def __init__(self):
        #initialize game
        self.players = [player.Player(1000, "MAX"), player.Player(1000, "TOM"),
                        player.Player(1000, "JOHN")]
        self.state = "Pre-Flop"
        self.current_dealer = 0
        self.small_blind = self.current_dealer + 1
        self.big_blind = self.small_blind + 1
        self.table = table.Table()
        self.deck = deck.Deck()
        self.pot = 0
        self.hands_played = 0
        self.probability_calculator = handProbability.HandProbability()

    def set_dealer(self):
        """Function that sets the dealer of the current hand"""
        if self.hands_played == 0: #if it's the first hand of the game the current dealer is the first player in the array of players
            self.current_dealer = 0
        else:
            if self.current_dealer + 1 < len(self.players): #if the next dealer's index is over the length of the array
                self.current_dealer += 1
            else:
                self.current_dealer = 0

    def set_small_blind(self):
        """Function that sets the small blind of the current hand"""
        if self.current_dealer + 1 < len(self.players): #if the small blind is over the array length
                self.small_blind = self.current_dealer + 1
        else:
            self.small_blind = 0

    def set_big_blind(self):
        """Function that sets the big blind of the current hand"""
        if self.current_dealer + 2 < len(self.players): #if the big blind is over the array length
                self.big_blind = self.current_dealer + 2
        else:
            self.big_blind = 0

    def deal_cards(self):
        """Function that give 2 cards to each player in the game and remvoes them from the deck"""
        self.deck.shuffle_deck()
        for i in range(len(self.players)): #for each player we give two cards
            self.players[i].hand.append(self.deck.cards.pop(0))
            self.players[i].hand.append(self.deck.cards.pop(0))

    def update_state(self):
        """Function that update's the state of the game depending on the play"""
        if self.state == "Pre-Flop":
            self.state = "Flop"
        elif self.state == "Flop":
            self.state = "Turn"
        elif self.state == "Turn":
            self.state = "River"
        elif self.state == "River":
            self.state = "Showdown"
        elif self.state == "Showdown":
            self.state = "Cleanup"
        elif self.state == "Cleanup":
            self.state = "Pre-Flop"

    def bets(self):
        players = self.players.copy() #we copy the array of players in the game
        finished_state = False #boolean that determines if we are still in play in the current state
        current_player = self.big_blind #the first player to start his choice of calling or raising
        current_call = 20 #the current total of calls from the players it's first value is the value of the big blind

        folded_players = 0 #the number of players that are folded

        for i in range(len(players)): #loop that counts how many players have folded in pervious states
            if(players[i].status == "Folded"):
                folded_players += 1
        if self.state == "Pre-Flop":
            max_plays = len(players) - 1 #the big blind is not counted
        else:
            max_plays = len(players) - folded_players #the number of plays in order to stop the loop

        counter_of_plays = 0 #counter that counts how many players have called
        choice = 0

        while not finished_state:
            current_player = current_player + 1 if current_player + 1 < len(players) else 0

            # for i in range(len(players)):
            #     print(f"{players[i].name} : {players[i].current_call} | {players[i].money}")

            if players[current_player].state != "Folded": #if the player is still playing
                self.show("Shown")
                print(f"{players[current_player].name} WHAT WOULD YOU LIKE TO DO ?")
                print(f"1. CALL ON {current_call}")
                print(f"2. RAISE TO {current_call + 10}")
                print(f"3. FOLD")

                choices = ["1","2","3"]
                choice = input("What ? ")

                while choice not in choices:
                    if choice not in choices:
                        print("PLEASE CHOOSE A VALID CHOICE !")
                        choice = input("What ? ")

                if choice == "1":
                    players[current_player].calling(current_call - players[current_player].current_call) #player adds to the call from his already betted money
                    players[current_player].current_call = current_call #we set the players betted money to the current call
                    counter_of_plays += 1 #we add one to the counter of plays in order to stop the loop

                elif choice == "2":
                    players[current_player].raising(current_call, (current_call + 10) - players[current_player].current_call)
                    current_call = current_call + 10 #current call is added by 10 each raise
                    players[current_player].current_call = current_call #we set the players betted money to the current call
                    counter_of_plays = 0 #we reset the counter because each player has to restart his choice of calling or raising or folding

                elif choice == "3":
                    players[current_player].folding()
                    players[current_player].status = "Folded" #we set the players status to folded so we don't count him again
                    max_plays = len(players) - 1 #we remove 1 from the max plays because there is one less player

                if counter_of_plays == max_plays: #if all players have called or folded
                    finished_state = True #we stop the loop

        for i, p in enumerate(players): #for each player
            self.pot += p.current_call #we add to the pot the money that player has bet
            p.current_call = 0 #we restart the bet of each player

    def check_winner(self):
        hand_powers = [] #the hand power of every single player
        for i, p in enumerate(self.players):
            hand_powers.append(p.hand_power(self.table.cards)) #we add the hand power of every player to the array

        winners = [] #array that stocks the winning hands
        playersIndexes = [] #array that stocks the indexes of winning players

        for i,hand in enumerate(hand_powers):
            if i == 0: #if it's the first hand
                m = max(hand_powers, key=lambda item:item[1]) #we put the best hand in a variable based on the win %
                max_index = hand_powers.index(max(hand_powers, key=lambda item:item[1])) #we get the index of the max hand
                playersIndexes.append(max_index) #we put that max index in an array of players indexes
                winners.append(m) #we add the max to the array of winners

            if hand[1] > m[1]:
                m = max(hand_powers) #we change m to the max hand
                winners.clear()
                winners.append(m) #we add the max to the array of winners
                playersIndexes.append(i) #we add the max to the array of winners

            elif hand[1] == m[1] and i != max_index: #if it's another max and it's not the same as we put in i==0
                m = hand #we change m to the max hand
                winners.append(m) #we add the max to the array of winners
                playersIndexes.append(i) #we add the max to the array of winners

        print(winners)
        if len(winners) == 1:
            print(f"The winner is : {self.players[playersIndexes[0]].name}")

        else: #if multiple players have the same hand power
            best = sum(winners[0][2]) #we do the sum of all the cards in the best hand of the player
            win = 0 #the winner of the hand
            for i, hand in enumerate(winners):
                if sum(hand[2]) > best:
                    best = sum(hand[2])
                    win = i

            print(f"The winner is : {self.players[playersIndexes[win]].name}")

    def pre_flop(self):
        self.deck.shuffle_deck()

        self.set_dealer()
        self.set_small_blind()
        self.set_big_blind()
        self.deal_cards()

        self.players[self.small_blind].pay_small_blind(10)
        self.players[self.big_blind].pay_big_blind(20)

        self.players[self.big_blind].status = "BIG BLIND"
        self.players[self.big_blind].current_call = 20
        # self.pot += 20

        self.players[self.small_blind].status = "SMALL BLIND"
        self.players[self.small_blind].current_call = 10
        # self.pot += 10

        self.players[self.current_dealer].status = "DEALER"

        # print("-------------------------------")
        # print("PLAYER 1 :")
        # for i in range(2):
        #     print(f"\t{self.players[0].hand[i].value} | {self.players[0].hand[i].suit}")

        # self.probability_calculator.probabilityPreFlop(6, self.players[0].hand)
        # print("-------------------------------")
        # print("PLAYER 1 :")
        # for i in range(2):
        #     print(f"\t{self.players[1].hand[i].value} | {self.players[1].hand[i].suit}")

        # self.probability_calculator.probabilityPreFlop(6, self.players[1].hand)
        # print("-------------------------------")
        # for i in range(2):
        #     print(f"\t{self.players[2].hand[i].value} | {self.players[2].hand[i].suit}")

        # self.probability_calculator.probabilityPreFlop(6, self.players[2].hand)

        self.bets()

    def flop(self):
        for i in range(3):
            self.table.add_card(self.deck.cards.pop(0))
        self.bets()

    def turn(self):
        self.table.add_card(self.deck.cards.pop(0))
        self.bets()

    def river(self):
        self.table.add_card(self.deck.cards.pop(0))
        self.bets()

    def show(self, type_of_show):
        os.system("cls")
        print(f"CURRENT STATE OF PLAY : {self.state}")
        for i in range(len(self.players)):
            self.players[i].show_hand(type_of_show)
            print(self.players[i].hand_power(self.table.cards))

        print("TABLE :")
        self.table.show_table()
        print(f"THE POT IS : {self.pot} $")

    def cleanup(self):
        self.table.cards = []
        for i in range(len(self.players)):
            self.players[i].hand = []

        self.deck.deck_restart()
        self.hands_played += 1
        self.pot = 0

    def playing(self):
        while self.players[0].money > 0:
            self.pre_flop()
            self.show("Shown")

            self.update_state()
            self.flop()
            self.show("Shown")

            self.update_state()
            self.turn()
            self.show("Shown")

            self.update_state()
            self.river()
            self.show("Shown")

            self.update_state()
            self.show("Shown")
            self.check_winner()

            self.update_state()
            self.cleanup()

            # self.update_state()
            # self.pre_flop()
            # self.show("Shown")
