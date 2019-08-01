import deck

class HandProbability:
    def __init__(self):
        self.deck = deck.Deck()

    def probabilityPreFlop(self, nbr_players, hand):
        if hand[0].value == hand[1].value:
            probability_for_three_of_a_kind = 2 / (52 - 2*nbr_players)
            probability_for_four = 2 / (52 - 2*nbr_players) * 1 / (51 - 2*nbr_players)

            print(f"Probability of brelan : {format(probability_for_three_of_a_kind * 100, '.4f')} %")
            print(f"Probability of four : {format(probability_for_four * 100, '.4f')} %")

        else:
            probability_for_pair = 3 / (52 - 2*nbr_players)

            print(f"Probability of pair : {format(probability_for_pair * 100, '.4f')} %")

        if hand[0].suit == hand[1].suit:
            probability_for_flush = 11 / (52 - 2*nbr_players)
            print(f"Probability of flush : {format(probability_for_flush * 100, '.6f')} %")

    def ProbabilityFlop(self, nbr_players, hand, table):
        cards = hand.copy() + table.copy()
