from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
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

        for suit in suits:
            for i in range(len(values)):
                deck.append([values[i], suit, amounts[i], 'boardgamepack/PNG/Cards/card' + suit + values[i] + '.png'])
        self.deck = deck

        random.shuffle(self.deck)
        self.my_hand[0] = self.deck.pop(0)
        self.my_hand[1] = self.deck.pop(0)
        card_1_image = self.my_hand[0][3]
        card_1_value = self.my_hand[0][2]
        card_2_image = self.my_hand[1][3]
        card_2_value = self.my_hand[1][2]

        self.dealer_hand[0] = self.deck.pop(0)
        self.dealer_hand[1] = self.deck.pop(0)

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

        self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2])

        self.name_text = 'BLACKJACK'
    def create_deck(self):
        self.my_hand[0] = self.deck.pop(0)
        self.my_hand[1] = self.deck.pop(0)
        card_1_image = self.my_hand[0][3]
        card_1_value = self.my_hand[0][2]
        card_2_image = self.my_hand[1][3]
        card_2_value = self.my_hand[1][2]

        self.dealer_hand[0] = self.deck.pop(0)
        self.dealer_hand[1] = self.deck.pop(0)

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

        self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2])

        self.name_text = 'BLACKJACK'
        print(len(self.deck))

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

            self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2])

            self.name_text = 'BLACKJACK'


    def hit(self):
        if self.user_card3.card_value == 0:
            self.my_hand[2] = self.deck.pop(0)
            self.user_card3.image_file = self.my_hand[2][3]
            self.user_card3.card_value = self.my_hand[2][2]
            self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2])
        elif self.user_card4.card_value == 0:
            self.my_hand[3] = self.deck.pop(0)
            self.user_card4.image_file = self.my_hand[3][3]
            self.user_card4.card_value = self.my_hand[3][2]
            self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2] + self.my_hand[3][2])
        elif self.user_card5.card_value == 0:
            self.my_hand[4] = self.deck.pop(0)
            self.user_card5.image_file = self.my_hand[4][3]
            self.user_card5.card_value = self.my_hand[4][2]
            self.count.text = str(self.my_hand[0][2] + self.my_hand[1][2] + self.my_hand[2][2] + self.my_hand[3][2] + self.my_hand[4][2])
        if int(self.count.text) > 21:
            self.name_text = 'BUST'
            if self.name_text == 'BUST':
                self.card2.image_file = self.my_hand[1][3]
                if self.dealer_hand[0][2] + self.dealer_hand[1][2] < 17:
                    self.dealer_hand[2] = self.deck.pop(0)
                    self.card3.image_file = self.dealer_hand[2][3]
                    if self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] < 17:
                        self.dealer_hand[3] = self.deck.pop(0)
                        self.card4.image_file = self.dealer_hand[3][3]
                        if self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] + \
                                self.dealer_hand[3][2] < 17:
                            self.dealer_hand[4] = self.deck.pop(0)
                            self.card5.image_file = self.dealer_hand[4][3]

    def stay(self):
        self.card2.image_file = self.my_hand[1][3]
        if self.dealer_hand[0][2] + self.dealer_hand[1][2] < 17:
            self.dealer_hand[2] = self.deck.pop(0)
            self.card3.image_file = self.dealer_hand[2][3]
            if self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] < 17:
                self.dealer_hand[3] = self.deck.pop(0)
                self.card4.image_file = self.dealer_hand[3][3]
                if self.dealer_hand[0][2] + self.dealer_hand[1][2] + self.dealer_hand[2][2] + self.dealer_hand[3][2] < 17:
                    self.dealer_hand[4] = self.deck.pop(0)
                    self.card5.image_file = self.dealer_hand[4][3]



if __name__ == '__main__':
    app = BlackjackApp()
    app.run()