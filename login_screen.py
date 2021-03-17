
from kivy.config import Config 

Config.set("graphics", "resizable", False) 

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
from kivy.animation import Animation
import sqlite3

Window.size = (530, 248)

class Manager(ScreenManager):
    pass
    
class LoginScreen(Screen):

    def login(self):
        connection = sqlite3.connect("table.db")

        cursor = connection.cursor()

        self.data = ("SELECT * FROM dados WHERE name = ? AND password = ?")

        cursor.execute(self.data, [( self.ids.username_login.text), (self.ids.password_login.text)])

        self.result = cursor.fetchall()

        if self.result:

            self.alert("Signed in")

        else:

            self.alert("Acess denied")     

    def alert(self, str):
        
        alert = self.ids.alert

        self.animate = Animation(pos=(275, 15), duration=0.2, opacity=1)

        self.ids.alert_text.text = str

        self.animate.start(alert)
        
    def close_alert(self):

        alert = self.ids.alert

        self.animate = Animation(pos=(275, -50), duration=0.2, opacity=0)

        self.animate.start(alert)

class RegisterScreen(Screen):
    
    def data_base(self):

        connection = sqlite3.connect("table.db")

        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS dados (name text, password text, email text)")

        if self.ids.email.text != "" and self.ids.username.text != "" and self.ids.password.text != "":

            cursor.execute(f"INSERT INTO dados VALUES('{self.ids.username.text}', '{self.ids.password.text}', '{self.ids.email.text}')")

            cursor.execute("SELECT * FROM dados")

            connection.commit()

            self.manager.current = "login_screen"

        else:
            self.alert("fill in all fields")

    def alert(self, str):

        alert = self.ids.alert

        self.animate = Animation(pos=(275, 15), duration=0.2, opacity=1)

        self.ids.alert_text.text = str

        self.animate.start(alert)

    def close_alert(self):

        alert = self.ids.alert

        self.animate = Animation(pos=(275, -50), duration=0.2, opacity=0)

        self.animate.start(alert)

class Login(App):

    def build(self):
        
        return Manager()

Login().run()