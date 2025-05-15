#include "Function/D&D/DNDFunction.h"

int main()
{
    char keyWords[20], nomeFile[20] = {"0"}, nome[60];
    int choose = 0, dim, firstCreation = 0, lv_count = 0;
    CHARACTER player[20];
    
    MainMenu(keyWords, nomeFile, nome, player, &choose, &dim);
    if (strcmp(keyWords, "Continue") == 0) firstCreation = 1;

    StartingGame_CreatingCharacter(player, choose, dim, keyWords, firstCreation); 
    while(strcmp(keyWords, "Exit") != 0)
    {
        VisualizzazionePersonaggio(player[choose], keyWords, nome, nomeFile);

        if (strcmp(keyWords, "Salva") == 0)
        {
            DataSave_Writer(player[choose], nomeFile, nome);

        }
        if (strcmp(keyWords, "Campain") == 0)
        {
            printf("Campain is Actually not Available!!!");
            delay(2);
        }
        if (strcmp(keyWords, "Details") == 0) 
        {
            Details(player[choose], nome);
        }
        if (strcmp(keyWords, "Training") == 0) { player[choose] = BattleFunction_TrainingZone(player[choose], nomeFile, &lv_count); }
        if (strcmp(keyWords, "Name_Change") == 0){ ChangeName(nome);}
    }
    ExitMode();
    

}