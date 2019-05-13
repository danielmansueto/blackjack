from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BlackjackApp(App):
    def build(self):
        return BlackjackLayout()

class BlackjackLayout(BoxLayout):
    def create_deck(self):
        for i in range(1, 14):
            for x in range(4):
                cards = x, i
                deck = []
                deck.append(cards)
                print(deck)




if __name__ == '__main__':
    app = BlackjackApp()
    app.run()