#include "MyFunction.h"

void DataSave_Loader(CHARACTER player[], char nomeFile[], char nome[], int *choose, int *closeCicle)
{
    FILE *DataSave;
    DIR *director;
    
    int i = 0;
    char path[100] = {"Save Files/"};
    
    // struttura di defualt della libreria dirent.h che serve per leggere tutta una  cartella fino alla fine (comando simile a feof)

    struct dirent *entry;

//directory
    director = opendir("Save Files");

system("@cls||clear");
LogoTitle();
printf("\nElenco File All'interno del Folder:\n\n");


//col ciclo while dico al compiler di eseguire il ciclo
//finche' la struttura dirent viene riempita
    while (entry=readdir(director))
    {
        printf("-- File %d:   %s\n", i+1, entry->d_name);
        i++;
    }
    
    closedir(director);
//              directory                   //

//  Se non ci sono file, ritorno al menu   //
    if (i == 2)
    {
        delay(2);
        printf("\nNon ci sono File Di salvataggio nella Cartella");
        delay(2);
        printf("\nRicaricamento Menu.....");
        delay(3);
        return;
    }
// ----------------------------------------//   
 
    
    printf("\nInserisci Nome del File (SenzaSpazi con Estensione .bin):    ");
    scanf("%s", nomeFile);
    strcat(path,nomeFile);

    DataSave = fopen(path, "rb");

    if (DataSave == NULL)
    {
        printf("\nError Code 216: Cannot Open File");
        delay(2);
        fclose(DataSave);
        strcpy(nomeFile, "0");
        return;
    }
    
    fread(nome, sizeof(char), sizeof(nome), DataSave);
    fread(player, sizeof(CHARACTER), sizeof(&player), DataSave);

    printf("\nCaricamento DataSave '%s' in Corso.....", nomeFile);
    delay(3);

    (*choose) = player->ID;
    (*closeCicle) = 1;

    fclose(DataSave);
}

void DataSave_Writer(CHARACTER player, char nomeFile[], char nome[])
{
    FILE *DataSave;
    char path[100] = {"Save Files/"};
    char extensione[10] = {".bin"};
    char newName[100];

    if (strcmp(nomeFile, "0") == 0)
    {
        printf("\nInserisci Nome del File (Senza Spazi):    ");
        scanf("%s", nomeFile);
        strcat(nomeFile, extensione);
        strcat(path,nomeFile);

        DataSave = fopen(path, "wb+");
    } 
    else
    {
        printf("\nSovrascrivo il File '%s':    ", nomeFile);
        strcat(path,nomeFile);
        DataSave = fopen(path, "wb+");
    } 

//Se il file non esiste, chiude il linker, e lo riapre in modalita append
    if (DataSave == NULL)
    {
        fclose(DataSave);
        printf("\nNuovo File Di Salvataggio:      %s", nomeFile);
        delay(1);

        DataSave = fopen(path, "awb");
        printf("\n\nCompiling SaveData File....");
        delay(3);
        fwrite(nome, sizeof(char), sizeof(nome), DataSave);
        fwrite(&player, sizeof(CHARACTER), sizeof(&player), DataSave);
        printf("\nAlready Compiled");
        delay(1.5);

        fclose(DataSave);

    }
    else{
        printf("\n\nCompiling SaveData File....");
        delay(3);
        fwrite(nome, sizeof(char), sizeof(nome), DataSave);
        fwrite(&player, sizeof(CHARACTER), sizeof(&player), DataSave);
        printf("\nAlready Compiled");
        delay(1.5);

        fclose(DataSave);
    }
    
}

void ChangeName(char nome[])
{
    printf("\n\nInserisci il Nuovo nome:         ");
    scanf("%s", nome);
    printf("\nRicaricamento Personaggio");
    for (int i = 0; i < 5; i++)
    {
        printf(" .");
        delay(1);
    }
    
    clrscr();
}
