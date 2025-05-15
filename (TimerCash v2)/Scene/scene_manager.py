from kivy.uix.screenmanager import Screen, ScreenManager

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
