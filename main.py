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
    def create_deck(self):
        deck = []
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        amounts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for suit in suits:
            for i in range(len(values)):
                deck.append([values[i], suit, amounts[i], 'boardgamepack/PNG/Cards/card' + suit + values[i] +'.png'])
        self.deck = deck

        random.shuffle(self.deck)
        print(self.deck)



if __name__ == '__main__':
    app = BlackjackApp()
    app.run()