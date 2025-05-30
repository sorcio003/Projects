from spellchecker import SpellChecker

spell = SpellChecker(language='it')  # Italiano

def correggi_parola(parola):
    parola = parola.replace(" ", "")  # Rimuove spazi involontari
    corretta = spell.correction(parola)
    return corretta if corretta else "Parola non trovata"

# Test
text = input('inserisci una parola: ')

text = text.split()

for parole in text:
    parola_input = parole
    parola_correggi = correggi_parola(parola_input)
    print(f"Parola corretta: {parola_correggi}")
