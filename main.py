from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
import random

class BlackjackApp(App):
    def build(self):
        return BlackjackLayout()

class BlackjackLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deck = []
        self.my_hand = [[], [], [], [], []]
        self.dealer_hand = [[], [], [], [], []]
        deck = []
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        amounts = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.dealer_count = 0
        self.user_count = 0
        self.user_bet = 0
        self.bank_account = int(self.money.text[1:])


        for suit in suits:
            for i in range(len(values)):
                deck.append([values[i], suit, amounts[i], 'boardgamepack/PNG/Cards/card' + suit + values[i] + '.png'])
        self.deck = deck

        random.shuffle(self.deck)


        self.name_text = 'BLACKJACK (DEAL TO START)'
    def create_deck(self):

        self.user_bet = int(self.bet.text)
        self.my_hand[0] = self.deck.pop(0)
        self.my_hand[1] = self.deck.pop(0)
        card_1_image = self.my_hand[0][3]
        card_1_value = self.my_hand[0][2]
        card_2_image = self.my_hand[1][3]
        card_2_value = self.my_hand[1][2]

        self.dealer_hand[0] = self.deck.pop(0)
        self.dealer_hand[1] = self.deck.pop(0)
        '''
        self.dealer_hand[2] = self.deck.pop(0)
        self.dealer_hand[3] = self.deck.pop(0)
        self.dealer_hand[4] = self.deck.pop(0)
        '''
        self.dealer_count = self.dealer_hand[0][2]
        self.dealer_number.text = str(self.dealer_count)

        self.card1.image_file = self.dealer_hand[0][3]
        self.card2.image_file = "boardgamepack/PNG/Cards/cardBack_red5.png"
        self.card3.image_file = "greybackground.png"
        self.card4.image_file = "greybackground.png"
        self.card5.image_file = "greybackground.png"

        self.user_card3.image_file = "greybackground.png"
        self.user_card3.card_value = 0
        self.user_card4.image_file = "greybackground.png"
        self.user_card4.card_value = 0
        self.user_card5.image_file = "greybackground.png"
        self.user_card5.card_value = 0

        self.user_card1.card_value = card_1_value
        self.user_card1.image_file = card_1_image
        self.user_card2.card_value = card_2_value
        self.user_card2.image_file = card_2_image

        self.user_count = self.my_hand[0][2] + self.my_hand[1][2]
        self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2])

        self.name_text = 'BLACKJACK'



        if len(self.deck) <= 10:
            self.deck = []
            self.my_hand = [[], [], [], [], []]
            deck = []
            suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
            values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            amounts = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

            for suit in suits:
                for i in range(len(values)):
                    deck.append(
                        [values[i], suit, amounts[i], 'boardgamepack/PNG/Cards/card' + suit + values[i] + '.png'])
            self.deck = deck

            random.shuffle(self.deck)
            self.my_hand[0] = self.deck.pop(0)
            self.my_hand[1] = self.deck.pop(0)
            card_1_image = self.my_hand[0][3]
            card_1_value = self.my_hand[0][2]
            card_2_image = self.my_hand[1][3]
            card_2_value = self.my_hand[1][2]

            self.user_card3.image_file = "greybackground.png"
            self.user_card3.card_value = 0
            self.user_card4.image_file = "greybackground.png"
            self.user_card4.card_value = 0
            self.user_card5.image_file = "greybackground.png"
            self.user_card5.card_value = 0

            self.user_card1.card_value = card_1_value
            self.user_card1.image_file = card_1_image
            self.user_card2.card_value = card_2_value
            self.user_card2.image_file = card_2_image

            self.user_count = self.my_hand[0][2] + self.my_hand[1][2]
            self.count.text = str(self.user_count)

            self.name_text = 'SHUFFLE'


    def hit(self):
        if self.user_card3.card_value == 0:
            self.my_hand[2] = self.deck.pop(0)
            self.user_card3.image_file = self.my_hand[2][3]
            self.user_card3.card_value = self.my_hand[2][2]
            self.user_count = self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2]
            self.count.text = str(self.user_count)
            if self.user_count > 21:
                for card in range(0, 3):
                    card_count = 0
                    if self.my_hand[card][0] == 'A':
                        card_count += 1
                        for i in range(card_count):
                            self.user_count -= 10
                            self.count.text = str(self.user_count)
                            if self.user_count < 12:
                                self.user_count += 10
                                self.count.text = str(self.user_count)




        elif self.user_card4.card_value == 0:
            self.my_hand[3] = self.deck.pop(0)
            self.user_card4.image_file = self.my_hand[3][3]
            self.user_card4.card_value = self.my_hand[3][2]
            self.user_count = self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2] + self.my_hand[3][2]
            self.count.text = str(self.user_count)
            if self.user_count > 21:
                for card in range(0, 4):
                    card_count = 0
                    if self.my_hand[card][0] == 'A':
                        card_count += 1
                        for i in range(card_count):
                            self.user_count -= 10
                            self.count.text = str(self.user_count)
                            if self.user_count < 12:
                                self.user_count += 10
                                self.count.text = str(self.user_count)
        elif self.user_card5.card_value == 0:
            self.my_hand[4] = self.deck.pop(0)
            self.user_card5.image_file = self.my_hand[4][3]
            self.user_card5.card_value = self.my_hand[4][2]
            self.user_count = self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2] + self.my_hand[3][2] + self.my_hand[4][2]
            self.count.text = str(self.user_count)
            if self.user_count > 21:
                for card in range(0, 5):
                    card_count = 0
                    if self.my_hand[card][0] == 'A':
                        card_count += 1
                        for i in range(card_count):
                            self.user_count -= 10
                            self.count.text = str(self.user_count)
                            if self.user_count < 12:
                                self.user_count += 10
                                self.count.text = str(self.user_count)
        if self.user_count > 21:
            self.name_text = 'BUST'
            self.card2.image_file = self.dealer_hand[1][3]
            self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2]
            self.bank_account -= self.user_bet
            self.money.text = '$' + str(self.bank_account)



    def stay(self):
        '''
        done = False
        while done is False:
            if len(self.dealer_hand) == 5:
                done = True
                break
            self.card2.image_file = self.dealer_hand[1][3]
            for card in self.dealer_hand:
                self.dealer_count = sum(self.dealer_hand[card][2])
                print(self.dealer_count)
        '''
        self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2]
        if self.dealer_count > 21:
            for card in range(0, 2):
                card_count = 0
                if self.dealer_hand[card][0] == 'A':
                    card_count += 1
                    for i in range(card_count):
                        self.dealer_count -= 10
                        print(self.dealer_count)
                        self.dealer_number.text = str(self.dealer_count)
                        if self.dealer_count < 12:
                            self.dealer_count += 10
                            self.dealer_number.text = str(self.dealer_count)
        self.card2.image_file = self.dealer_hand[1][3]
        if self.dealer_hand[0][2] + self.dealer_hand[1][2] < 17:
            self.dealer_hand[2] = self.deck.pop(0)
            self.card3.image_file = self.dealer_hand[2][3]
            self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2]
            if self.dealer_count > 21:
                for card in range(0, 3):
                    card_count = 0
                    if self.dealer_hand[card][0] == 'A':
                        card_count += 1
                        for i in range(card_count):
                            self.dealer_count -= 10
                            print(self.dealer_count)
                            self.dealer_number.text = str(self.dealer_count)
                            if self.dealer_count < 12:
                                self.dealer_count += 10
                                self.dealer_number.text = str(self.dealer_count)
            if self.dealer_count < 17:
                self.dealer_hand[3] = self.deck.pop(0)
                self.card4.image_file = self.dealer_hand[3][3]
                self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] + self.dealer_hand[3][2]
                if self.dealer_count > 21:
                    for card in range(0, 4):
                        card_count = 0
                        if self.dealer_hand[card][0] == 'A':
                            card_count += 1
                            for i in range(card_count):
                                self.dealer_count -= 10
                                print(self.dealer_count)
                                self.dealer_number.text = str(self.dealer_count)
                                if self.dealer_count < 12:
                                    self.dealer_count += 10
                                    self.dealer_number.text = str(self.dealer_count)
                if self.dealer_count < 17:
                    self.dealer_hand[4] = self.deck.pop(0)
                    self.card5.image_file = self.dealer_hand[4][3]
                    self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] + self.dealer_hand[3][2] + self.dealer_hand[4][2]
                    self.dealer_number.text = str(self.dealer_count)
                    if self.dealer_count > 21:
                        for card in range(0, 5):
                            card_count = 0
                            if self.dealer_hand[card][0] == 'A':
                                card_count += 1
                                for i in range(card_count):
                                    self.dealer_count -= 10
                                    print(self.dealer_count)
                                    self.dealer_number.text = str(self.dealer_count)
                                    if self.dealer_count < 12:
                                        self.dealer_count += 10
                                        self.dealer_number.text = str(self.dealer_count)
                else:
                    self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] + self.dealer_hand[3][2]
                    self.dealer_number.text = str(self.dealer_count)

            else:
                self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2]
                self.dealer_number.text = str(self.dealer_count)
        else:
            self.dealer_count = self.dealer_hand[0][2] + self.dealer_hand[1][2]
            self.dealer_number.text = str(self.dealer_count)

        if self.dealer_count > self.user_count and self.dealer_count <=21:
            self.name_text = 'LOSE'
            self.bank_account -= self.user_bet
            self.money.text = '$' + str(self.bank_account)


        elif self.dealer_count < self.user_count or self.dealer_count > 21:
            self.name_text = 'WIN'
            self.bank_account += self.user_bet
            self.money.text = '$' + str(self.bank_account)

        elif self.dealer_count == self.user_count:
            self.name_text = 'DRAW'






if __name__ == '__main__':
    app = BlackjackApp()
    app.run()