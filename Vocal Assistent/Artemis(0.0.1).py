'''from pyttsx3 import init
from speech_recognition import Recognizer, Microphone


engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)



engine.say("Ciao, come stai")
engine.runAndWait()
r = Recognizer()

while True:
    with Microphone() as source:
        print("pronto ad ascoltare...")
        audio = r.listen(source)
        testo = r.recognize_google(audio, language="it-IT")
        print(testo)
        if "Artemis" in testo:
            engine.say("Sono Artemis")
            engine.runAndWait()'''


import speech_recognition as Artemis

from pyttsx3 import init

#inserimento file audio da esterno
#nome varriabile = sr.AudioFile("path")


#Inizializzo voce Artemis

engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("Ciao, come stai")
engine.runAndWait()

#per qualunque messaggio, istanziaree una variabile che definisce
#la lunghezza max della pausa che il codice deve tener conto prima di chiudere
#l'analisi del messaggio in Input (Pausa, respiro o Silenzio)

recognizer_instance = Artemis.Recognizer()

with Artemis.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Sono in ascolto")
    audio = recognizer_instance.listen(source)
    print("Sto Elaboranddo...")

try:
    testo = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Artemis ha capito: ", testo)
    if "Artemis" in testo:
            engine.say("Sono Artemis")
            engine.runAndWait()
except Exception as e:
    print(e)
    
        
        
            
