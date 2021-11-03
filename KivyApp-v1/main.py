from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.graphics import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        Window.size = (405, 855)
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        with self.canvas.before:
            # MeetU logo bg = rbg[188, 239, 224]
            Color(188/255, 239/255, 224/255, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        self.title = 'MeetU'

        # image
        self.add_widget(Image(source="YESLogo.jpg",
                                    size_hint = (.3, .4),
                                    pos_hint = {'center_x': 0.5, 'center_y': 0.5}))
        # label
        self.log_in = Label(text="User Name",
                            font_size = 20,
                            color = '#115c41',
                            size_hint = (.4, .05),
                            pos_hint = {'x': 0.05, 'y': 0})
        self.add_widget(self.log_in)
        # textinput
        self.user = TextInput(multiline = False,
                            padding_y = (10, 10),
                            size_hint = (.8, .06),
                            pos_hint = {'x': 0.1, 'y': 0})
        self.add_widget(self.user)
        # space label
        self.add_widget(Label(text="", size_hint=(1, .02)))
        # password
        self.add_widget(Label(text = "Password",
                                    font_size = 20,
                                    color = "#115c41",
                                    size_hint = (.4, .05),
                                    pos_hint = {'x': 0.03, 'y': 0}))
        # password input field
        self.passwordInput = TextInput(multiline = False,
                                    padding_y = (10, 10),
                                    size_hint = (.8, .06),
                                    pos_hint = {'x': .1, 'y': 0},
                                    password = True)
        self.add_widget(self.passwordInput)
        # space text
        self.add_widget(Label(text = "", size_hint = (1, .1)))
        # button
        self.button = Button(text="SIGN IN",
                            size_hint=(.8, .08),
                            bold = True,
                            background_color = '#00FFCE',
                            pos_hint = {'center_x': .5})
        # self.button.bind(on_press=self.callback)
        self.button.bind(on_press=self.callback)
        self.add_widget(self.button)
        # space text
        self.add_widget(Label(text = "",
                                size_hint = (1, .5)))

    def callback(self, instance):
        the_app.screen_manager.current = 'Second'

class SecondWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(102/255, 102/255, 102/255, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        self.orientation = 'vertical'

        for i in range(20):
            self.person_label = Button(text='user0-4',
                                      font_size=20,
                                      color='#cccccc',
                                      size_hint=(None, .2),
                                      pos_hint={'x':.05, 'y':0})
            self.add_widget(self.person_label)

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.loginPage = LoginPage()
        screen = Screen(name='Login')
        screen.add_widget(self.loginPage)
        self.screen_manager.add_widget(screen)

        self.second_page = SecondWindow()
        screen = Screen(name='Second')
        screen.add_widget(self.second_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    the_app = MyApp()
    the_app.run()

'''
class MyApp(MDApp):
    def build(self):
        Window.size = (405, 855)
        return

MyApp().run()
'''