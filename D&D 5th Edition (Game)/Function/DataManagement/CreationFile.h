#include "../DataType/Skills.h"

void CreationFile()
{
    CHARACTER player;
    player.ID = 0;

    FILE *file;
    DIR *director;

    int id = 0;
    int check;
    int rangeValues;
    int firstCreation = 0;
    char exitCommand[10], folder[10], Exit[10];
    char class[30];

while ((strcmp(exitCommand, "Enemy") != 0) && (strcmp(exitCommand, "Player") != 0))
{
    printf("Do you want open Enemy file or player file (No to exit)? "); scanf("%s", exitCommand); 
    ChangeCaseOfWords(exitCommand);
    // Exit Mode
    if ( (strcmp(exitCommand, "No") == 0) ) { system("@cls||clear"); return ; } 
}

    strcpy(folder, exitCommand);
    clrscr();
    printf("Updating File...\n");
do{
        id++;
        char path[70] = {"DataBase_Files/"};
        srand(time(NULL));

        printf("Insert Character on database File\n\nFirst Insert name: ");
        scanf("%s", player.Classe);
        ChangeCaseOfWords(player.Classe);
        printf("Give me range of combat values (Dice to calculate life): ");
        scanf("%d", &rangeValues);

//  --  Starting from here Create new directiry for each Enemy
        strcat(path, folder); strcat(path, "/"); strcat(path, player.Classe);

//----------------------------------------------------// 
//                     directory                      //
        struct dirent *entry;
        director = opendir(path);
//SE LA DIRECTORY ESISTE< CONTO I FILE ALL'INTERNO, E PASSO ID == NUMERO ELEMENTI
    if (director != NULL)
    {
        int i = 0;
        firstCreation = 1;
        while (entry=readdir(director)) { i++; }
        if(strcmp(exitCommand, "Player") == 0 ) Write_Abilita(path, i, firstCreation);
        closedir(director);
    }
//SE LA DIRECTORY NON ESITSE --> LA CREO CON ID == 1
    if (director == NULL)
    {
        printf("\nCreating Directory %s", player.Classe);
        for (int i = 0; i < 5; i++)
        {
            delay(1);
            printf(" .");
        }
        printf("\n");
        
        //mkdir --> Used to Create new directory
        check = mkdir(path);

        if (!check) printf("Directory Created\n");
        else{ printf("Unable to Create\n"); exit(-1); }
//                 End Create Directory               //    
//----------------------------------------------------//        
        if(strcmp(exitCommand, "Player") == 0 ) Write_Abilita(path, id, firstCreation);
        closedir(director);
    }
//----------------------------------------------------//  

        int vita;
        player.ID += 1; 
        player.Level = 1;
        if (strcmp(folder, "Player") == 0)
        {
            player.bonus_competenza = 3;
            player.dadoVita = rangeValues;
            player.Vita =    12 + rand()%rangeValues +1;
            player.ViteSalvezza = 3;
            player.exp = 1;
        }
        if (strcmp(folder, "Enemy") == 0) player.Vita =  rangeValues;
        
        player.Stamina = rand()%rangeValues + 1 + 5;
        player.ATK =     rand()%rangeValues + 1 + 5;
        player.Armor =   rand()%rangeValues + 1 + 5;
        vita = player.Vita/2;

        if (strcmp(exitCommand, "Player") == 0 && !firstCreation) fprintf(file, "\n%d %s %d %d %d %.2f %.2f %.2f %.2f %d %d",player.ID,player.Classe, player.Level, player.bonus_competenza, player.dadoVita, player.Vita, player.Stamina, player.ATK, player.Armor, player.exp, player.ViteSalvezza);

        if (strcmp(exitCommand, "Enemy") == 0 && !firstCreation) fprintf(file, "\n%d %s %.2f %.2f %.2f %.2f %d",player.ID,player.Classe, player.Stamina, player.ATK, player.Armor, player.exp);
        
        printf("\nDo you want Insert Another Character ?");
        scanf("%s", Exit);
        system("@cls||clear");
}
while( (strcmp(Exit, "NO") != 0) && (strcmp(Exit, "no") != 0));

fclose(file);


//  -- Info Player
char words[20];
char percorso[30] = "Database_Files//";
FILE *info;

LogoTitle();
printf("\nInserisci Info personaggio:  (Digit 0 to Exit)\n\n");

strcat(percorso, exitCommand);
strcat(percorso, "//");
strcat(percorso, player.Classe);
strcat(percorso, "//info.bin");

info = fopen(percorso, "wb+");

do
{   
    scanf("%s", words);
    if(strcmp(words, "0") != 0)
    {
        fwrite(words, sizeof(char), sizeof(words), info);
    }
}while (strcmp(words, "0") != 0);
fclose(info);

}
