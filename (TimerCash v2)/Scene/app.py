from Scene import scene_manager
from Scene.KV.scene import screen_helper
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from Scene.KV.menu import *
from Scene.KV.profile import *
from Function.worker import Worker
from Function.contact_form import SendEmail, SendEmailCliente, pdf
from Function.clock import startTime
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import os
from datetime import datetime

screen_helper += menu_helper
screen_helper += profile_helper

class APP(MDApp):
    
    def on_start(self):
        self.worker = []
        
        self.name_receiver = ""
        self.surname = ""
        self.paga = ""
        self.email = ""
        self.email_cliente = ""
        self.type_work = ""
        self.start_time_str = ""
        self.end_time_str = ""
        
        if os.path.exists("Database/save.txt"):
    # Apri il file in modalità lettura
            with open("Database/save.txt", "r") as file:
                # Leggi le righe dal file e rimuovi i caratteri di newline
                self.name_receiver = file.readline().strip()
                self.surname = file.readline().strip()
                self.paga = file.readline().strip()
                self.type_work = file.readline().strip()

                self.root.get_screen('profile').ids.nome.text = self.name_receiver
                self.root.get_screen('profile').ids.cognome.text = self.surname
                self.root.get_screen('profile').ids.paga.text = self.paga
                self.root.get_screen('profile').ids.type_work.text = self.type_work
                
        return super().on_start()
    
    def build(self):
        self.screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Light"        
        
        self.started = False
    
        return self.screen
        
    def add_worker(self):

        self.name_receiver = self.root.get_screen('profile').ids.nome.text
        self.surname = self.root.get_screen('profile').ids.cognome.text
        self.paga = self.root.get_screen('profile').ids.paga.text
        self.type_work = self.root.get_screen('profile').ids.type_work.text
        
        temp = Worker(self.name_receiver, self.surname, self.email, "", self.paga, self.type_work)
        
        if not self.worker:
        
            self.worker.append(temp.lista)
        
        else:
            self.worker[0] = temp.lista
            
        file = open("Database/save.txt", "w")
        
        file.write(self.name_receiver + "\n")
        file.write(self.surname + "\n")
        file.write(self.paga + "\n")
        file.write(self.type_work + "\n")
        file.close() 
        
        print(self.worker)
        
    def start(self):
        self.email = self.root.get_screen('menu').ids.lavoratore.text
        self.email_cliente = self.root.get_screen('menu').ids.datore.text
        
        temp = Worker(self.name_receiver, self.surname, self.email, self.email_cliente, self.paga, self.type_work)
        
        if not self.worker:
            self.worker.append(temp.lista)
        else:
            self.worker[0] = temp.lista
        
        if not self.started:
        
            SendEmail(False, self.worker[0], 0)
            SendEmailCliente(False, self.worker[0], 0)

            self.start_time = startTime()
            self.start_time_str = datetime.now().strftime("%H:%M:%S")
            
            self.started = True
        else:
            print("Already Started")
        
    def stop(self):
        
        if self.started:
        
            self.end_time = startTime()
            self.end_time_str = datetime.now().strftime("%H:%M:%S")
            
            total_time = self.end_time - self.start_time
            
            total_time = total_time / 3600.0
            
            pay = ( (self.end_time - self.start_time) / 3600 ) * float(self.worker[0][4])
            
            pdf(self.worker[0], round(pay, 2), datetime.now(), self.start_time_str, self.end_time_str, round(total_time, 3))
            
            SendEmail(True, self.worker[0], pay)
            SendEmailCliente(True, self.worker[0], pay)
            
            self.started = False
        else:
            print("Not Started Yet")
        
    