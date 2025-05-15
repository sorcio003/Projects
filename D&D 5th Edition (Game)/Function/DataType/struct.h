#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <dirent.h>
#define MAX_ABILTY 10

// LISTA
typedef struct nodo
{
    char words[20];
    struct nodo *next;
}NODO;
typedef NODO *list;

//ABILITA
typedef struct mossa
{
    int ID;
    char nome[20];
    list descrip;
    char Type[20];
    int costo;
    int livello;
    int damage;
}ABILITA;

//ARRAY DI STRNGHE
typedef char Stringa[20];

//STRUTTURA PERSONAGGIO
typedef struct 
{
    int ID;
    char Classe[30];
    int Level;
    int dadoVita;
    int bonus_competenza;
    float Vita;
    float Stamina;
    float ATK;
    float Armor;
    int exp;
    int ViteSalvezza;
    int number_Ability;
    int turni;
    ABILITA abilty[MAX_ABILTY];
}CHARACTER;

//LOGO
typedef struct 
{
    char Stringa[500];
}LOGO;
