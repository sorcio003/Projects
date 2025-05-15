//library used to open directory/folder
#include "../DataManagement/CreationFile.h"

//For Randomize Play
int MaxValue_Player(CHARACTER value)
{
    float max = 0;

        if (max < value.Vita)
        {
            max = value.Vita;
        }
        if (max < value.Stamina)
        {
            max = value.Stamina;
        }
        if (max < value.ATK)
        {
            max = value.ATK;
        }
        if (max < value.Armor)
        {
            max = value.Armor;
        }
        
    return max;
    
}

void ChangeCaseOfWords(char words[])
{
    int len = strlen(words);

    if (words[0] >= 97 && words[0] <= 122) words[0] -= 32;

    for (int i = 1; i < len; i++)
    {
        if(words[i] >= 65 && words[i] <= 90)
        {
            words[i] += 32;
        }
    }
      
}

void ExitMode()
{
     clrscr();
     LogoTitle();
     printf("\n\n\n\n\n\n\n\n\n\n\n\n\n//-----------GoodBye Player-----------//");
     exit(1);
}
