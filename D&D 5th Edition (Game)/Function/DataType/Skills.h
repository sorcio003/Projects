#include "list.h"

int ReadAbilities(char classe[], Stringa array[])
{
    DIR *director;

    char path[30] = {"DataBase_Files/Player/"};
    int i = 0, j = 0;
    
    strcat(path, classe);
    strcat(path, "/Ability");
    printf("\n\nPath: %s\n", path);

    struct dirent *entry;

    //directory
    director = opendir(path);

    printf("\nCarico Abilita' Nel Personaggio");   
    for (int i = 0; i < 5; i++)
    {
        delay(1);
        printf(".");
    }
    printf("\n\n");     

    while (entry=readdir(director))
    {

    if (i >=2)
    {
        printf("-- Abilty %d:   %s\n", j+1, entry->d_name);
        strcpy(array[j], entry->d_name);
        j++;
        delay(1);
    }
        i++;
    }
    
    closedir(director);
//              directory                   //
return j;

}

int ReadAbilitiesEnemy(char classe[], Stringa array[])
{
    DIR *director;

    char path[30] = {"DataBase_Files/Enemy/"};
    int i = 0, j = 0;
    
    strcat(path, classe);
    strcat(path, "/Ability");

    struct dirent *entry;

    //directory
    director = opendir(path);   

    while (entry=readdir(director))
    {

    if (i >=2)
    {
        strcpy(array[j], entry->d_name);
        j++;
    }
        i++;
    }
    
    closedir(director);
//              directory                   //
return j;

}


void Write_Abilita(char path[], int id, int firstCreation)
{
    DIR *director;
    FILE* file;
    FILE* battle_skill;
    char backup[50];
    char name_Ability[20];
    char type_Ability[20];
    char words[20];
    int var = 0;
    int check;

    struct dirent *entry;

    strcat(path, "/Ability");

    director = opendir(path);

//SE LA DIRECTORY NON ESITSE --> LA CREO CON ID == 1
    if (director == NULL)
    {
        printf("\nCreating Directory Ability");
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
    }
    closedir(director);

if (!firstCreation)
{
    //  -- Creating Automaticly Attacco_extra Ability
            { 
                printf("\nCreo Abilita' Standard \"Attacco Extra\"");
                for (int i = 0; i < 5; i++)
                {
                    printf(". ");
                    delay(1);
                }
                strcpy(backup, path); strcat(backup, "/Attacco_Extra.txt");
                file = fopen(backup, "w+");

                fprintf(file, "ID: 1 ;\n\n");
                fprintf(file, "Nome: AttaccoExtra ;\n\n");
                fprintf(file, "Description: \"Durante la Battaglia, Azione Bonus concessa Ad Ogni Classe del Gioco\" ;\n\n");
                fprintf(file, "HowToUse: \"E' una azione Bonus che costa 3 tacche di Stamina, Il giocatore tenta un'altro attacco (stesse dinamiche dell'Attacco Normale)\" ;\n\n");
                fprintf(file, "Cost: 3 ;\n\n");
                fprintf(file, "Level: 1 ;\n\n");
                fprintf(file, "Danno: 0 ;\n\n");
                fprintf(file, "\"Il Damage Viene calcolato in Battaglia\" ;\n\n");        

                fclose(file);
            }
    //  --                                      -- //
}

do
{
    strcpy(backup, path);
    clrscr();
    printf("Creo Le Abilita del PG\nInserisci Il Nome dell'Abilita' (SenzaSpazi) (Use '0' to Exit): ");
    scanf("%s", name_Ability);

    if (strcmp(name_Ability, "0") != 0) 
    {
        char pathSkills[30] = "Skills/";
        int costo = 0;
        int damage = 0;
        for (int i = 0; i < 5; i++) { printf("%c ", 254); delay(1); } printf("\n");

        strcat(backup, "/");
        strcat(backup, name_Ability);
        strcat(backup, ".txt");

        file = fopen(backup, "w+");
        

        fprintf(file, "ID: %d ;\n", id);
        fprintf(file, "\nNome: %s ;\n", name_Ability);

        printf("\nInserisci Tipologia di Abilita':\n - normal (attacco fisico)\n - magic \n - Recovery_Heal\n - Damage_Boost\n - Shield_Boost\n --------:  ");
        scanf("%s", type_Ability);
        fprintf(file, "\nType: %s ;\n", type_Ability);

    //  Description
        fprintf(file, "\nDescription: ");
        printf("\nInserisci Descrizione (Use \";\" to Exit):\n\n");

        do
        {
            scanf("%s", words);
            fprintf(file, "%s ", words);
        }while (strcmp(words, ";") != 0);

        fprintf(file, "\n");
    //  HowToUse
        fprintf(file, "\nHowToUse: ");
        printf("\nInserisci HowToUse (Use \";\" to Exit):\n\n");

        do
        {
            scanf("%s", words);
            fprintf(file, "%s ", words);
        }while (strcmp(words, ";") != 0);

        fprintf(file, "\n"); 
    //  Cost
        printf("\nInserisci Costo Ability:  ");
        scanf("%d", &costo);
        fprintf(file, "\nCost: %d ;", costo);
    //  Level
        printf("\nInserisci Livello da Raggiungere per usare la Ability:  ");
        scanf("%d", &var);
        fprintf(file, "\nLevel: %d ;", var);
    //  Damage
        printf("\nInserisci Danno (0 se il danno e' calcolato in battaglia):  ");
        scanf("%d", &damage);
        fprintf(file, "\nDanno: %d ;", damage);

        if (var == 0){ fprintf(file, "\n\n\"Il Damage Viene calcolato in Battaglia\";");  }
        
        fclose(file); 

        //Creazione file Skill --------------------------
        /*
        stract(pathSkills, name_Ability);
        stract(pathSkills, ".h")

        file = fopen(pathSkills, "w+");

        if (file == NULL){
            printf("Error. File not found");
            exit(-1);
        }
        if (strcmp(type_Ability, "Boost") == 0){
            fprintf(file, "
            #include \"list.h\"\n\n
            void Ability_%s(CHARACTER *player, int i, CHARACTER *NPC, CHARACTER *stat){
            \n
            player->Stamina -= player->abilty[i].costo;\n
                    printf(\"Hai usato %s Stamina, Ti rimane Ancora %s Stamina\n\n\", player->abilty[i].costo, player->Stamina);\n
                    delay(2);\n
                    printf(\"\n%s %s Attiva\n\", 254, player->abilty[i].nome);\n
                    D20=rand()%c19 + 1;\n
            ", name_Ability, "%d", "%.0f", "%c", "%s", '%');

            if (damage != 0){
                 fprintf(file, "
                \n//Calcolo danni\n\n
                player->ATK += player->ATK + player->ability[i].damage;\n
                *NPC = DamageCalculate(*NPC, *player, D20);  \n\n 

                //Reset Damage\n
                player->ATK = stat->ATK;\n
                strcpy(name_ability, player->abilty[i].nome);\n    ");
            }
        }

        fclose(file);
        */
        /// ----------------------------------------------
        
        id++;
    }

} while (strcmp(name_Ability, "0") != 0);
    printf("\nChiudo la Directory %s", backup);
    delay(1);
}

void Create_Abilita(FILE *file, ABILITA *abilita)
{
        char words[30];        
            fscanf(file, "%s", words);
            abilita->descrip = InsertIntoList(abilita->descrip, words);
            if (strcmp(words, "ID:") == 0)
            {
                fscanf(file, "%d", &abilita->ID);
                sprintf(words, "%d", abilita->ID);
                abilita->descrip = InsertIntoList(abilita->descrip, words);
            }
            if (strcmp(words, "Nome:") == 0)
            {
                fscanf(file, "%s", abilita->nome);
                abilita->descrip = InsertIntoList(abilita->descrip, abilita->nome);
            }
            if (strcmp(words, "Type:") == 0)
            {
                fscanf(file, "%s", abilita->Type);
                abilita->descrip = InsertIntoList(abilita->descrip, abilita->Type);
            }
            /*
            if (strcmp(words, "Description:") == 0)
            {
                while (strcmp(words, ";") != 0)
                {
                    fscanf(file, "%s", words);
                    abilita->descrip = InsertIntoList(abilita->descrip, words);
                }  
            } 
            */           
            if (strcmp(words, "Cost:") == 0)
            {
                fscanf(file, "%d", &abilita->costo);
                sprintf(words, "%d", abilita->costo);
                abilita->descrip = InsertIntoList(abilita->descrip, words);
            }
            if (strcmp(words, "Level:") == 0)
            {
                fscanf(file, "%d", &abilita->livello);
                sprintf(words, "%d", abilita->livello);
                abilita->descrip = InsertIntoList(abilita->descrip, words);                
            }
            if (strcmp(words, "Danno:") == 0)
            {
                fscanf(file, "%d", &abilita->damage);
                sprintf(words, "%d", abilita->damage);
                abilita->descrip = InsertIntoList(abilita->descrip, words);               
            }         
}

void ShowAbilita(ABILITA mosse)
{
        printf("Nome: %s\n", mosse.nome);
        printf("Costo: %d\n", mosse.costo);
        printf("Livello: %d\n", mosse.livello);
        printf("Damage: %d", mosse.damage);
}
