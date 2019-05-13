from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BlackJackApp(App):
    def build(self):
        return BlackJackLayout()

class BlackJackLayout(BoxLayout):
    pass

if __name__ == '__main__':
    app = BlackJackApp()
    app.run()