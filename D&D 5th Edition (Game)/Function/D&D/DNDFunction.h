#include "Battle.h"

void MainMenu(char keyWords[], char nomeFile[], char nome[], CHARACTER player[], int *scelta, int *DIM)
{
    int choose = 0, dim, closeCicle = 0;
    int j;
    Stringa array[10];
    ABILITA mosse[10];

    while( (strcmp(keyWords, "Start") != 0) && (strcmp(keyWords, "Random") != 0) && (closeCicle != 1))
    {
        system("@cls||clear");
        LogoTitle();
        printf("//-----------Benvenuto Giocatore----------//\n\n// -- Avvio Gioco          (Digit 'Start')\n// -- Continua Partita     (Digit 'Continue')\n// -- Random Mode          (Digit 'Random')\n\n\n\n\n\n// -- Istruzioni di gioco  (Digit 'Guide')\n// -- Exit                 (Digit 'Exit')\n\n\n// -- Command              (Secret Password)\n\n");
        printf("//---------KeyWords:       ");
        scanf("%s", keyWords);
        if (strcmp(keyWords, "iron03dc") != 0) ChangeCaseOfWords(keyWords);

        if(strcmp(keyWords, "Continue") == 0){ DataSave_Loader(player, nomeFile, nome, &choose, &closeCicle); }
        if(strcmp(keyWords, "iron03dc") == 0){ CreationFile(); }
        if(strcmp(keyWords, "Exit") == 0){ ExitMode(); }

    }

if ( (strcmp(keyWords, "Start") == 0) || (strcmp(keyWords, "Random") == 0))
{
    ChoosingCharacter(player,nome, &choose, &dim);
}

    (*scelta) = choose;
    (*DIM) = dim;

}

void ChoosingCharacter(CHARACTER player[], char nome[], int *scelta, int *dim)
{
    FILE *file;
    int id = 0, choose = 0;

    file = fopen("DataBase_Files/CharacterInfoPlayer.txt", "r");

    if (file == NULL)
    {
        printf("File Inesistente!!");
        exit(1);
    }
    
    system("@cls||clear");
    LogoTitle();
    printf("Personaggi disponibili all'interno del Rooster:\n\n\n");
    delay(2);

    while (!feof(file))
    {
        fscanf(file, "%d", &player[id].ID);
        fscanf(file, "%s", player[id].Classe);
        fscanf(file, "%d", &player[id].Level);
        fscanf(file, "%d", &player[id].bonus_competenza);
        fscanf(file, "%d", &player[id].dadoVita);
        fscanf(file, "%f", &player[id].Vita);
        fscanf(file, "%f", &player[id].Stamina);
        fscanf(file, "%f", &player[id].ATK);
        fscanf(file, "%f", &player[id].Armor);
        fscanf(file, "%d", &player[id].exp);
        fscanf(file, "%d", &player[id].ViteSalvezza);

        printf("[ID]: 0%d    Classe:  %s\n",player[id].ID, player[id].Classe);
        id++;
    }

    printf("\nInserisci il numero del Personaggio che vuoi Usare (Codice||ID[0] == Personaggio Random): ");
    scanf("%d", &choose);
    srand(time(NULL));
    if (choose == 0){ choose = (rand ()% id) + 1;}
    else{choose -= 1;}

    printf("Inserisci il Nome del Personaggio:    ");
    scanf("%s", nome);
    ChangeCaseOfWords(nome);

    (*scelta) = choose;
    (*dim) = id;
    fclose(file);

}

void StartingGame_CreatingCharacter(CHARACTER player[], int id, int dim, char keyWords[], int firstCreation)
{
    FILE *file;

    int luckLunch, multipler, randomRange = 0, Number_ability = 0;
    Stringa name_file_abilty[10];

    system("@cls||clear");
    delay(1);
    LogoTitle();
    if (firstCreation == 0)
    {
        printf ("Creazione Personaggio in Corso");
        for (int i = 0; i < 7; i++)
        {
            printf(".");
            delay(1);
        }
    }
    //Charging Abilty
        Number_ability = ReadAbilities(player[id].Classe, name_file_abilty);

        player[id].number_Ability = Number_ability;
        for (int i = 0; i < player[id].number_Ability; i++)
        {
            char path[70] = {"DataBase_Files//Player//"};
            strcat(path, player[id].Classe);
            strcat(path, "//Ability//");
            strcat(path, name_file_abilty[i]);
            //printf("\n%s\n", path);

            file = fopen(path, "r");

            if (file == NULL){ printf("il File non esiste"); exit(-1);}

            player[id].abilty[i].descrip = NULL;

            while (!feof(file))
            {
                Create_Abilita(file, &player[id].abilty[i]);
            }
            fclose(file); 
        }
           

    // Play Game with random stat's player (when you digit 'Random')
    if (strcmp(keyWords, "Random") == 0)
    {

        randomRange = MaxValue_Player(player[id]);
        srand(time(NULL));

        luckLunch = rand()% randomRange + 5;
        multipler = rand()% 10 + 1; 

        
        player[id].Vita    = rand()% luckLunch + multipler;
        player[id].Stamina = rand()% luckLunch + multipler;
        player[id].ATK     = rand()% luckLunch + multipler;
        player[id].Armor   = rand()% luckLunch + multipler;
    }
    

}

void VisualizzazionePersonaggio(CHARACTER player, char keyWords[], char nome[], char nomeFile[])
{
    int spazio;
    system("@cls||clear");
    LogoTitle();
    if (strcmp(nomeFile, "0") == 0) printf("\nPartita Ancora non salvata :(\n");
    else printf("\nNome del Salvataggio '%s'\n\n\n", nomeFile);
    PlayerTitle();
    printf("                          Lv:        %d\n                          Nome:      %s\n                          Classe:    %s\n                          Vita:      %.2f\n                          Stamina:   %.2f\n                          ATK:       %.2f\n                          Armor:     %.2f\n                          Exp:       %d\n                          Vite:      %d\n\n                      //-------------------//\n",player.Level,nome, player.Classe, player.Vita, player.Stamina,player.ATK,player.Armor, player.exp, player.ViteSalvezza);
  //printf("                          Exp:       %d\n   Vita:      %.2f\n   Stamina:   %.2f\n   ATK:       %.2f\n   Armor:     %.2f\n\n", player.Classe, player.Vita, player.Stamina,player.ATK,player.Armor);

    ExpBar(player.exp);
    Vite(player);    
    
    //Menu Chooses
    printf("\n\n\n// -- Starting Campain         (Digit 'Campain')\n// -- Starting Training Zone   (Digit 'Training')\n// -- Save Play                (Digit 'Salva')\n// -- Change Name              (Digit 'Name_Change')\n// -- Menu                     (Digit 'Menu')\n// -- Info Personggio          (Digit 'Details')\n// -- Exit                     (Digit 'Exit')");
    printf("\n\n\n//---------KeyWords:           ");
    scanf("%s", keyWords);
    
    if (strcmp(keyWords, "Name_Change")!=0)
    {
        ChangeCaseOfWords(keyWords);
    }

    if (strcmp(keyWords, "Menu")==0)
    {
        printf("Stai per tornare al Menu del Gioc, Perderi tutti i Progressi se non hai salvato\nSei Sicuro/a di proseguire? ");
        scanf("%s", keyWords);
        ChangeCaseOfWords(keyWords);

        char sign = 254;

        if (strcmp(keyWords, "Si")==0)
        {
            printf("\nCaricamento Main Menu in Corso (Ricalibrazione Gioco)....\n");

                for (int i = 0; i < 10; i++)
                    {
                        printf("%c ", sign);
                        delay(1);
                    }
                main();
        }
        
    }
    
}

void Details(CHARACTER player, char nome[])
{
            FILE *file;
            char path[70] = "Database_Files//Player//"; 
            char words[20];
            int i = 0;

            strcat(path, player.Classe);
            strcat(path, "//info.bin");

            clrscr();
            LogoTitle();
            printf("Info sul Personaggio \"%s\":\n\n - Classe %s\n\n - Info:\n", nome, player.Classe);

            file = fopen(path, "rb"); if (file == NULL){ printf("File Inesistente Error 124"); exit(-1);} 

            while (!feof(file))
            {
                fread(words, sizeof(char), sizeof(words), file);
                printf(" %s", words);
                i++;
                if (i == 10){ printf("\n"); i = 0;}
            }
            fclose(file);

            printf("\n\n~ Abilita' Personaggio ~\n");   
            for (int j = 0; j < player.number_Ability; j++)
                {
                    printf("\n~ Ability %d ~ Nome: %s", j+1, player.abilty[j].nome);
                } 
                printf("\n\nDigita 0 per uscire // Digita \"Nome\" della Abilita per mostrare Info: "); 
            scanf("%s", words);    

            while (strcmp(words, "0") != 0)
            {
                i = 0;
                clrscr();
                LogoTitle();
                while (strcmp(words, player.abilty[i].nome) != 0) i++;
                
                ShowList(player.abilty[i].descrip);
                printf("\n\n");
                for (int j = 0; j < player.number_Ability; j++)
                {
                    printf("\n~ Ability %d ~ Nome: %s", j+1, player.abilty[j].nome);
                } 
                printf("\n\nDigita 0 per uscire // Digita \"Nome\" della Abilita per mostrare Info: "); 
                scanf("%s", words);
            }
}