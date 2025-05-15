#include "../Display.h"

list InsertIntoList(list Lista, char words[])
{
    list temp = (list) malloc(sizeof(NODO));
    strcpy(temp->words, words);
    temp->next = Lista;

    return temp;
}

void ShowList(list lista)
{
    if (lista != NULL)
    {   
        ShowList(lista->next); 
        if (strcmp(lista->words, ";") == 0) printf("\n");
        else printf("%s ", lista->words);    
    }
}
