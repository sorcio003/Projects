# 🎲 D&D 5th Edition – C Version

Un simulatore ispirato alla **quinta edizione di Dungeons & Dragons**, sviluppato interamente in **C**.  
Il progetto offre un'esperienza immersiva tra **giocatore e CPU**, con meccaniche che includono **combattimenti a turni**, **gestione delle abilità**, **progressione del personaggio**, e **salvataggi permanenti** in stile roguelike.

> ⚔️ _"Benvenuto avventuriero. Le tue scelte contano, ma il dado è sovrano."_

---

## 🧠 Descrizione

Il gioco gestisce:
- **Combattimenti a turni** contro nemici predefiniti
- Tiri di dado per calcolare **attacchi, schivate e danni**
- Scelta iniziale di una classe tra **6 personaggi giocabili**
- Randomizzazione delle **statistiche base** (Forza, Difesa, Stamina...)
- **Sistema di esperienza e livelli** con sblocco abilità
- **Nemici con difficoltà crescente**, fino al Boss finale
- **Permadeath**: alla perdita di 3 vite, i file di salvataggio `.bin` vengono cancellati e si ricomincia da capo

---

## 🧾 Giocatori disponibili

| ID | Classe     | Livello | Bonus Comp. | Dado Vita | Vita  | Stamina | ATK   | Armor | Exp | Vite Salvezza |
|----|------------|---------|-------------|-----------|--------|---------|-------|--------|-----|----------------|
| 1  | Barbaro    | 1       | 3           | 12        | 13.00 | 6.00    | 10.00 | 9.00   | 1   | 3              |
| 2  | Mago       | 1       | 3           | 6         | 11.00 | 9.00    | 8.00  | 7.00   | 1   | 3              |
| 3  | Druido     | 1       | 3           | 8         | 13.00 | 6.00    | 8.00  | 9.00   | 1   | 3              |
| 4  | Paladino   | 1       | 3           | 10        | 16.00 | 6.00    | 8.00  | 12.00  | 1   | 3              |
| 5  | Stregone   | 1       | 3           | 6         | 12.00 | 9.00    | 10.00 | 11.00  | 1   | 3              |

---

## 👾 Nemici affrontabili

| ID | Nome                | HP    | ATK   | ARMOR | STAMINA | EXP |
|----|---------------------|-------|-------|--------|----------|-----|
| 1  | Wolf                | 12.00 | 5.00  | 10.00 | 6.00     | 6   |
| 2  | Skeleton            | 16.00 | 14.00 | 14.00 | 9.00     | 10  |
| 3  | Armored Skeleton    | 8.00  | 21.00 | 20.00 | 12.00    | 12  |
| 4  | Knigth              | 12.00 | 14.00 | 18.00 | 15.00    | 15  |
| 5  | Gigant              | 15.00 | 9.00  | 11.00 | 11.00    | 17  |
| 6  | Boos (Name_Unknow)  | 29.00 | 6.00  | 13.00 | 19.00    | 30  |

---

## 🗂️ Struttura del progetto

\`\`\`
📁 DnD-C-Version/
├── Game.c / Game.o
├── Assets/
├── DATABASE_FILE/
│   ├── CharacterInfoEnemy.txt
│   ├── CharacterInfoPlayer.txt
├── FUNCTION/
├── SAVE FILES/
│   ├── savegame.bin
├── Player/
│   └── <NomePersonaggio>/
│       └── Ability/
│           ├── AttaccoExtra.txt
│           └── info.bin
├── Enemy/
│   └── <NomeNemico>/
│       └── Ability/
│           └── ...
├── README.md
\`\`\`

---

## 📌 Compilazione ed esecuzione

# per WINDOWS
Basta eseguire il file GAME.exe
# per LINUX
\`\`\`bash
gcc Game.c -o dnd_simulator
./dnd_simulator
\`\`\`

---

## 🛠️ Tecnologie

- Linguaggio: **C**
- File `.txt` per la definizione di personaggi, nemici e abilità
- File `.bin` per salvataggi e dati runtime
- Librerie standard C (`stdio.h`, `stdlib.h`, `time.h`, ecc.)

---

## 📍 TODO

- [ ] Espansione abilità e classi
- [ ] Modalità storia
- [ ] Supporto grafico base (es. `ncurses`)
- [ ] Sistema di eventi randomici durante la partita

---

> _"Nel mondo di D&D, anche un semplice file `.txt` può contenere la leggenda di un eroe."_