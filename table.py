import deck

class Table:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def reset_table(self):
        self.cards = []

    def show_table(self):
        if len(self.cards) < 3:
            print("EMPTY TABLE")
        elif len(self.cards) == 3:
            card1 = f"{self.cards[0].value} " if self.cards[0].value < 10 else f"{self.cards[0].value}"
            card2 = f"{self.cards[1].value} " if self.cards[1].value < 10 else f"{self.cards[1].value}"
            card3 = f"{self.cards[2].value} " if self.cards[2].value < 10 else f"{self.cards[2].value}"

            cards = [card1, card2, card3]

            for i in range(3):
                if(cards[i] == "11"):
                    cards[i] = "J "
                elif(cards[i] == "12"):
                    cards[i] = "Q "
                elif(cards[i] == "13"):
                    cards[i] = "K "
                elif(cards[i] == "1 "):
                    cards[i] = "A "

            print("-------  -------  -------")
            print(f"|{cards[0]}   |  |{cards[1]}   |  |{cards[2]}   |")
            print(f"|  {self.cards[0].suit[0]}  |  |  {self.cards[1].suit[0]}  |  |  {self.cards[2].suit[0]}  |")
            print(f"|   {cards[0]}|  |   {cards[1]}|  |   {cards[2]}|")
            print("-------  -------  -------")

        elif len(self.cards) == 4:
            card1 = f"{self.cards[0].value} " if self.cards[0].value < 10 else f"{self.cards[0].value}"
            card2 = f"{self.cards[1].value} " if self.cards[1].value < 10 else f"{self.cards[1].value}"
            card3 = f"{self.cards[2].value} " if self.cards[2].value < 10 else f"{self.cards[2].value}"
            card4 = f"{self.cards[3].value} " if self.cards[3].value < 10 else f"{self.cards[3].value}"

            cards = [card1, card2, card3, card4]

            for i in range(4):
                if(cards[i] == "11"):
                    cards[i] = "J "
                elif(cards[i] == "12"):
                    cards[i] = "Q "
                elif(cards[i] == "13"):
                    cards[i] = "K "
                elif(cards[i] == "1 "):
                    cards[i] = "A "

            print("-------  -------  -------  -------")
            print(f"|{cards[0]}   |  |{cards[1]}   |  |{cards[2]}   |  |{cards[3]}   |")
            print(f"|  {self.cards[0].suit[0]}  |  |  {self.cards[1].suit[0]}  |  |  {self.cards[2].suit[0]}  |  |  {self.cards[3].suit[0]}  |")
            print(f"|   {cards[0]}|  |   {cards[1]}|  |   {cards[2]}|  |   {cards[3]}|")
            print("-------  -------  -------  -------")

        elif len(self.cards) == 5:
            card1 = f"{self.cards[0].value} " if self.cards[0].value < 10 else f"{self.cards[0].value}"
            card2 = f"{self.cards[1].value} " if self.cards[1].value < 10 else f"{self.cards[1].value}"
            card3 = f"{self.cards[2].value} " if self.cards[2].value < 10 else f"{self.cards[2].value}"
            card4 = f"{self.cards[3].value} " if self.cards[3].value < 10 else f"{self.cards[3].value}"
            card5 = f"{self.cards[4].value} " if self.cards[4].value < 10 else f"{self.cards[4].value}"

            cards = [card1, card2, card3, card4, card5]

            for i in range(5):
                if(cards[i] == "11"):
                    cards[i] = "J "
                elif(cards[i] == "12"):
                    cards[i] = "Q "
                elif(cards[i] == "13"):
                    cards[i] = "K "
                elif(cards[i] == "1 "):
                    cards[i] = "A "

            print("-------  -------  -------  -------  -------")
            print(f"|{cards[0]}   |  |{cards[1]}   |  |{cards[2]}   |  |{cards[3]}   |  |{cards[4]}   |")
            print(f"|  {self.cards[0].suit[0]}  |  |  {self.cards[1].suit[0]}  |  |  {self.cards[2].suit[0]}  |  |  {self.cards[3].suit[0]}  |  |  {self.cards[4].suit[0]}  |")
            print(f"|   {cards[0]}|  |   {cards[1]}|  |   {cards[2]}|  |   {cards[3]}|  |   {cards[4]}|")
            print("-------  -------  -------  -------  -------")