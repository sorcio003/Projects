import speech_recognition as Violet

from pyttsx3 import init

#inserimento file audio da esterno
#nome varriabile = sr.AudioFile("path")

#Inizializzo voce Violet

engine = init()
voce = engine.getProperty("voices")
engine.setProperty("voice", voce[0].id)

engine.say("Ciao, come stai")
engine.runAndWait()

#per qualunque messaggio, istanziaree una variabile che definisce
#la lunghezza max della pausa che il codice deve tener conto prima di chiudere
#l'analisi del messaggio in Input (Pausa, respiro o Silenzio)

recognizer_instance = Violet.Recognizer()

with Violet.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Sono in ascolto")
    audio = recognizer_instance.listen(source)
    print("Sto Elaboranddo...")

try:
    testo = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Violet ha capito: ", testo)
    if "Violet" in testo:
            engine.say("Sono Violet")
            engine.runAndWait()
except Exception as e:
    print(e)