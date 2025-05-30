from random import choice
import json
from datetime import datetime

with open('Voice_Line_Output.json', 'r') as V:
    Voice_Line = json.load(V)
    
def VioletOnHearing(testo):
    answerGave = False


    if any(richiesta in testo for richiesta in Voice_Line['possibleNameRequest']):       
        answerViolet = choice(Voice_Line['possibleVioletAnswerName'])
        print(answerViolet)
        answerGave = True

            
