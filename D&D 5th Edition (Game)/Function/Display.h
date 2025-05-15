#include "DataType/struct.h"

//FOR GUI 
void clrscr()
{
    system("@cls||clear");
}
void delay(int secondi){
    int milli_secondi = 1000 * secondi;

    clock_t start_time = clock();

    while (clock() < start_time + milli_secondi);
}
void Spaziatura(char nome[])
{
    for (int i = 0; i < 15 - strlen(nome); i++)
    {
        printf(" ");
    }
    
}

void LogoTitle()
{
    FILE *file;
    LOGO logo[500];
    int j = 0;

    file = fopen("Assets/Logo.txt", "rt");

    if (file == NULL)
    {
        printf("File Doesn't Exits");
        exit(-1);
    }
    while (!feof(file))
    {
        //funciton fgets, gte string with space, specification of where string will goes, dim, file pointer
        
        fgets(logo[j].Stringa, 500, file);     
        
        j++;
    }

    fclose(file);

    for (int i = 0; i < j; i++)
    {
        printf("%s", logo[i].Stringa);
    }
        printf("\n\n");
}
int PlayerTitle()
{
    FILE *file;
    LOGO logo[500];
    int j = 0;

    file = fopen("Assets/PlayerStatisticBox.txt", "rt");

    if (file == NULL)
    {
        printf("File Doesn't Exits");
        exit(-1);
    }
    while (!feof(file))
    {
        //funciton fgets, gte string with space, specification of where string will goes, dim, file pointer
        
        fgets(logo[j].Stringa, 500, file);     
        
        j++;
    }

    fclose(file);

    for (int i = 0; i < j; i++)
    {
        printf("%s", logo[i].Stringa);
    }
        printf("\n");
    return strlen(logo[j].Stringa);
}
