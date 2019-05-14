from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BlackjackApp(App):
    def build(self):
        return BlackjackLayout()

class BlackjackLayout(BoxLayout):
    def create_deck(self):
        deck = []
        suits = ['H', 'C', 'D', 'S']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        amounts = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for suit in suits:
            for value in values:
                if value == 'A':
                    amount = amounts[0]
                    deck.append([value, suit, amount])
                if value == '2':
                    amount = amounts[1]
                    deck.append([value, suit, amount])
                if value == '3':
                    amount = amounts[2]
                    deck.append([value, suit, amount])
                if value == '4':
                    amount = amounts[3]
                    deck.append([value, suit, amount])
                if value == '5':
                    amount = amounts[4]
                    deck.append([value, suit, amount])
                if value == '6':
                    amount = amounts[5]
                    deck.append([value, suit, amount])
                if value == '7':
                    amount = amounts[6]
                    deck.append([value, suit, amount])
                if value == '8':
                    amount = amounts[7]
                    deck.append([value, suit, amount])
                if value == '9':
                    amount = amounts[8]
                    deck.append([value, suit, amount])
                if value == '10':
                    amount = amounts[9]
                    deck.append([value, suit, amount])
                if value == 'J':
                    amount = amounts[9]
                    deck.append([value, suit, amount])
                if value == 'Q':
                    amount = amounts[9]
                    deck.append([value, suit, amount])
                if value == 'K':
                    amount = amounts[9]
                    deck.append([value, suit, amount])

        print(deck)








if __name__ == '__main__':
    app = BlackjackApp()
    app.run()