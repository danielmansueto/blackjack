from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BlackjackApp(App):
    def build(self):
        return BlackjackLayout()

class BlackjackLayout(BoxLayout):
    pass

if __name__ == '__main__':
    app = BlackjackApp()
    app.run()