from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.scrollview import ScrollView
from kivy.lang import Builder
from tutorial.input_field import username_helper

class NeuralRandom(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        
        scroll = ScrollView()
        
        item = OneLineListItem(text='Item 1')
        item_2 = OneLineListItem(text='Item 2')
        
        list = MDList()
        
        scroll.add_widget(list)
        
        list.add_widget(item)
        list.add_widget(item_2)

        btn_flat = MDFloatingActionButton(icon='language-python', 
                                pos_hint={'center_x':0.5, 'center_y':0.5})

        # user_input = MDTextField(text="Enter username", pos_hint = {'center_x':0.5, 'center_y':0.5}, size_hint = (0.5, 1))
        
        username = Builder.load_string(username_helper)
        # screen.add_widget(btn_flat)
        screen.add_widget(username)
        screen.add_widget(scroll)
        

        label = MDLabel(text="Hello World!",halign='center')
        
        icon_label = MDIcon(icon='language-python', halign='center')

        return screen
    

neuralRandom = NeuralRandom()
neuralRandom.run()