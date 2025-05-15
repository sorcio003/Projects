#include "../DataManagement/DataFile.h"

int exp_manager = 1;

void ExpBar(int exp)
{
    char sign = 254;
    printf("\nExp: ");
    for (int i = 0; i < exp; i++)
    {
        printf("%c", sign);
    }
    
}

void Vite(CHARACTER player){
    printf("\nVite Residue: ");
    for (int i = 0; i < player.ViteSalvezza; i++)
    {
        printf("%c ", 1);
    }
}

void LevelUpgrade(CHARACTER *player)
{
    int soglia, livello, upgrade;
    int sign = 254;
    soglia = 12 *player->Level; 
    upgrade = (player->dadoVita)/2;

    if (player->exp >= soglia)
    {
        player->exp -= soglia;
        player->Level ++;
        printf("\n%c Livello del Giocatore e' CRESCIUTO %d ", sign, player->Level -1);

            printf("=");
            delay(1);
            printf("=");
            delay(1);
            printf(">");
            delay(1);
            delay(1);

        printf(" %d",player->Level);

        srand(time(NULL));
        player->Vita += rand()%upgrade +1;
        player->ATK += rand()%upgrade +1;

        if (player->Level%3 == 0)
        {
            player->Stamina += player->bonus_competenza;
        }

        for (int i = 0; i < player->number_Ability; i++)
        {
            if (player->Level == player->abilty[i].livello) printf("\nHai sbloccato l'Abilita' %s!!", player->abilty[i].nome);
        } 
        
    }  
    
}

void Gui_ShowCharacter(CHARACTER player, CHARACTER NPC)
{
    printf("//-------------------//");
    Spaziatura(player.Classe);
    printf("//-------------------//\n\n");
    printf("   Nome:      %s", player.Classe);
    Spaziatura(player.Classe);
    printf("   Nome:      %s\n", NPC.Classe);
    printf("   Vita:      %.2f", player.Vita);
    //il codice di spaziatura personalizzatto per i parametri float
    if (player.Vita > 10)
    {
        Spaziatura("44444");
    }
    else{
        Spaziatura("3333");
    }
    printf("   Vita:      %.2f\n", NPC.Vita);
    printf("   Stamina:   %.2f", player.Stamina);
    if (player.Stamina > 10)
    {
        Spaziatura("44444");
    }
    else{
        Spaziatura("3333");
    }

    printf("   Stamina:   %.2f\n", NPC.Stamina);
    printf("   ATK:       %.2f", player.ATK);

    if (player.ATK > 10)
    {
        Spaziatura("44444");
    }
    else{
        Spaziatura("3333");
    }
    
    printf("   ATK:       %.2f\n", NPC.ATK);
    printf("   Armor:     %.2f", player.Armor);
    if (player.Armor > 10)
    {
        Spaziatura("44444");
    }
    else{
        Spaziatura("3333");
    }
    printf("   Armor:     %.2f\n\n", NPC.Armor);
    printf("   Exp:     %.d", player.exp);
    if (player.exp > 10)
    {
        Spaziatura("44444");
    }
    else{
        Spaziatura("3333");
    }
    printf("        Exp:     %d\n\n", NPC.exp);
    printf("//-------------------//");
    Spaziatura(player.Classe);
    printf("//-------------------//\n\n");
}

int OutBattle(char direction[30]){
    int direzione = 0;

if(strcmp(direction, "Vai a Nord") == 0){
      direzione = 1;
}
if(strcmp(direction, "Vai a Sud") == 0){
      direzione = 2;
}
if(strcmp(direction, "Vai a Ovest") == 0){
      direzione = 3;
}
if(strcmp(direction, "Vai a Est") == 0){
      direzione = 4;
}
if(strcmp(direction, "Entra") == 0){
      direzione = 5;
}
if(strcmp(direction, "Esci") == 0){
      direzione = 6;
}
return direzione;
}

CHARACTER DamageCalculate(CHARACTER NPC, CHARACTER player, int D20)
{
    char sign = 254;
    int D6 = 0;
    float HIT;
    srand(time(NULL));

    printf("\n%c Hai fatto un:%d\n\n",sign, D20);
    delay(2);
    //missed hit
    if(D20<NPC.Armor) printf("Il colpo non e' andato a segno\n");
    delay(2);

    //critical damage
    if((D20==20))
    {
        printf("Il colpo e' Colpo Critico!!\nDue Tiri Danno a disposizione\n");
        delay(2);
        for (int i=0;i<2;i++)
        {
            printf("%d Tiro per infliggere un danno...\n\n", i+1);
            delay(2);
            D6=rand()%5 + 1;

            printf("Hai fatto :%d", D6);
            HIT=D6+(player.ATK/2);
            NPC.Vita=NPC.Vita-HIT;
            printf("\nDanno totale: %2.f\n", HIT);
            delay(2);
            if (NPC.Vita > 0) printf("Vita residua %s: %2.f\n\n", NPC.Classe, NPC.Vita);
            else printf("Vita residua %s: 0\n\n", NPC.Classe);
            delay(2);

        }
    }

    //Fallimento critico
    if(D20 == 1){
        printf("Hai Fatto un Fallimento Critico!!\nPerdi 2 punti vita\n");
        player.Vita -= 2;
        delay(2);
    }

    //hitted
    if(D20>=NPC.Armor && D20 <20)
    {
        printf("Il colpo e' andato a segno\n");
        delay(2);
        printf("Tiro per infliggere un danno...\n");
        delay(2);
        D6=rand()%5 + 1;

        printf("Hai fatto :%d", D6);
        delay(2);
        HIT=D6+(player.ATK/2);
        NPC.Vita=NPC.Vita-HIT;
        printf("\nDanno totale: %2.f\n", HIT);
        delay(2);
        if (NPC.Vita > 0) printf("Vita residua %s: %2.f\n\n", NPC.Classe, NPC.Vita);
        else printf("Vita residua %s: 0\n\n", NPC.Classe);
        delay(2);
    }
    return NPC;
}

CHARACTER DodgeAction(CHARACTER NPC, CHARACTER player)
{
    int D6 = 0, D20 = 0, schivata = 0;
    float HIT, CD;
    char sign = 254;

    printf("\n%c Hai deciso di schivare\nTiro per impostare la CD\n\n", sign);

    srand(time(NULL));
    schivata = rand()% 6 + 8;
    CD = (player.Armor/2) + schivata;
    player.Armor = CD;
    delay(2);

    printf("La tua CD (Classe Armatura Schivata) e': %.2f\nHai consumato 5 tacche di stamina\n", CD);
    player.Stamina = player.Stamina - 5;
    if (player.Stamina <= 0) player.Stamina = 0;

    return player;
}

void AbilityAction(CHARACTER *player, CHARACTER *NPC, CHARACTER *stat, int choose, char name_ability[], int *activated, int D20_Enemy)
{
    int D4, D6, D20;
    float HIT;
    char sign = 254;
    srand(time(NULL));

    D4 = rand()%3 + 1;
    D6 = rand()%5 +1;
    if (player->Stamina > 0)
    {
        for (int i = 0; i < player->number_Ability; i++)
        {
            if (choose == 0){ printf("\n%c nessuna Abilita Scelta", 254); delay(2); return;}
            if (choose == player->abilty[i].ID && player->Stamina >= player->abilty[i].costo && player->Level >= player->abilty[i].livello)
            {
    //ATTACCO EXTRA ABILITY (LV. 1)
                if (strcmp(player->abilty[i].Type, "Boost_Life") == 0 )  
                {
                    int dado_Vita = rand()% player->dadoVita + 1;
                    int Tot_Heal = 0;

                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    dado_Vita = rand()% player->dadoVita + 1;
                    Tot_Heal += dado_Vita;

                    player->Vita += Tot_Heal;
                    printf("\nVita Recuperata ");
                    delay(2);
                    printf("=");
                    delay(2);
                    printf("=");
                    delay(2);
                    printf(">");
                    delay(2);
                    printf(" %d", Tot_Heal);
                    delay(2);
                    printf("\nVita Player attuale e' di %d\n", player->Vita);
                }
                if (strcmp(player->abilty[i].nome, "AttaccoExtra") == 0)
            {
                player->Stamina -= player->abilty[i].costo;
                printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                delay(2);
                printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);
                D20=rand()%19 + 1;
                // calcolo danni
                *NPC = DamageCalculate(*NPC, *player, D20);             
            } 
                if (strcmp(player->abilty[i].nome, "Attacco_Incauto") == 0)
            {
                player->Stamina -= player->abilty[i].costo;
                printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                delay(2);
                printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);
                D20=rand()%19 + 1;

                // calcolo danni
                player->ATK = player->ATK *2;
                player->Armor = player->Armor/2;
                *NPC = DamageCalculate(*NPC, *player, D20);   

                player->ATK = stat->ATK;
                strcpy(name_ability, player->abilty[i].nome);         
            } 
                
                if (strcmp(player->abilty[i].nome, "Ira") == 0)
                {
                    player->Stamina -= player->abilty[i].costo;
                    if (player->Level >= 1  && player->Level <= 3) player->abilty[i].damage = 2;
                    if (player->Level >= 4  && player->Level <= 6) player->abilty[i].damage = 3;
                    if (player->Level >= 7  && player->Level <= 9) player->abilty[i].damage = 4;
                    if (player->Level >= 10 && player->Level <= 15) player->abilty[i].damage = 5;
                    if (player->Level >= 16 && player->Level <= 20) player->abilty[i].damage = 6;
                    if (player->Level >= 21 && player->Level <= 25) player->abilty[i].damage = 7;
                    if (player->Level >= 26 && player->Level <= 35) player->abilty[i].damage = 8;
                    if (player->Level >= 36 && player->Level <= 45) player->abilty[i].damage = 9;
                    if (player->Level >= 46) player->abilty[i].damage = 10;

                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    NPC->Vita -= player->abilty[i].damage;

                    if (NPC->Vita < 0)  NPC->Vita = 0;

                    printf("\nIl %s sprigiona tutta la sua Ira", player->Classe);
                    delay(1);
                    printf("\nDanno Inflitto ");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf(">");
                    delay(1);
                    printf(" %d", player->abilty[i].damage);
                    delay(1);
                    printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                    delay(1);

                }
                if (strcmp(player->abilty[i].nome, "Curare_Le_Ferite") == 0 )  
                {
                    if (player->Vita < stat->Vita)
                    {
                        int D20_TOT = 0;
                        int dado_Vita = player->dadoVita ;
                        int CD = 8 + player->bonus_competenza + D6;
                        int Tot_Heal = 0;

                        player->Stamina -= player->abilty[i].costo;
                        printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                        delay(2);
                        printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                        printf("\nImposto la CD del Giocatore a %d\n", CD);
                        delay(2);
                        printf("\nLancio Dado sulla CD");
                        for (int i = 0; i < 3; i++)
                        {
                            delay(1);
                            printf(". ");
                        }
                        
                        D20 = rand()% 20 + 1;
                        D20_TOT += D20;

                        if (D20 < CD) 
                        {
                            printf("\nHai Fatto: %d, Non hai superato la CD\n", D20_TOT);
                            delay(2);
                        }
                        else if (D20 >= CD)
                        {
                            printf("\nhai Fatto: %d, Hai superato la CD\n", D20_TOT);
                            delay(2);

                            if (player->dadoVita <= 8)
                            {
                                for (int i = 0; i < 2; i++)
                                {
                                    dado_Vita = rand()% player->dadoVita + 1;
                                    Tot_Heal += dado_Vita;
                                }
                            }
                            else
                            {
                                dado_Vita = rand()% player->dadoVita + 1 + player->bonus_competenza;
                                Tot_Heal += dado_Vita;
                            }
                            player->Vita += Tot_Heal;
                            printf("\nVita Recuperata ");
                            delay(2);
                            printf("=");
                            delay(2);
                            printf("=");
                            delay(2);
                            printf(">");
                            delay(2);
                            printf(" %d", Tot_Heal);
                            delay(2);
                            printf("\nVita Player attuale e' di %.0f\n", player->Vita);
                    }

                    }
                    else if (player->Vita >= stat->Vita)
                    { 
                        printf("\nNon puoi usare la Abilita di cura, la tua vita e' gia Full!!"); 
                        return; 
                    }
                    else if (player->Stamina < player->abilty[i].costo) printf("\nIl costo é troppo alto, non puoi usare questa abilita");
                }
                
                if (strcmp(player->abilty[i].nome, "Onda_Di_Tuono") == 0 )
                {
                    int D20_TOT = 0;
                    int dado_Vita = rand()% player->dadoVita + 1;
                    int CD = 8 + player->bonus_competenza + D6;
                    int Tot_Damage = 0;

                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nImposto la CD del Giocatore a %d\n", CD);
                    delay(2);
                    printf("\nLancio Dado sulla CD");
                    for (int i = 0; i < 3; i++)
                    {
                        delay(1);
                        printf(". ");
                    }
                    
                    D20 = rand()% 20 + 1;
                    D20_TOT += D20;

                    if (D20_TOT < CD) 
                    {
                        printf("\nHai Fatto: %d, Non hai superato la CD\n", D20_TOT);
                        delay(2);
                    }
                    else if (D20_TOT >= CD)
                    {
                        printf("\nhai Fatto: %d, Hai superato la CD\n", D20_TOT);
                        delay(2);
                        printf("\nLancio il Dado per i punti Ferita");
                        for (int i = 0; i < 5; i++)
                        {
                            printf(". ");
                            delay(1);
                        }
                        
                        Tot_Damage = player->bonus_competenza + rand()% dado_Vita + 1;
                        NPC->Vita -= Tot_Damage;

                        if (NPC->Vita < 0)  NPC->Vita = 0;

                        printf("\nDanno Inflitto ");
                        delay(1);
                        printf("=");
                        delay(1);
                        printf("=");
                        delay(1);
                        printf(">");
                        delay(1);
                        printf(" %d", Tot_Damage);
                        delay(1);
                        printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                        delay(1);
                    }
                }   
                if (strcmp(player->abilty[i].nome, "Armatura_Magica") == 0 )
                {
                    player->Stamina -= player->abilty[i].costo;
                    player->Armor = 13 + player->bonus_competenza;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nRicalibro la CA del Giocatore a %.0f per 3 Turni\n", player->Armor);
                    delay(2);
                    player->turni = 3;

                }
                if (strcmp(player->abilty[i].nome, "Dardo_Incantato") == 0)
                {
                    int Tot_Damage;
                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    Tot_Damage = D4 + (player->ATK - NPC->Armor);
                    NPC->Vita -= Tot_Damage;

                    printf("\nDardo Incantanto lanciato");
                    for (int i = 0; i < 5; i++)
                    {
                        delay(2);
                        printf(". ");
                    }

                    if (NPC->Vita < 0)  NPC->Vita = 0;

                    printf("\nDanno Inflitto ");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf(">");
                    delay(1);
                    printf(" %d", Tot_Damage);
                    delay(1);
                    printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                    delay(1);
                }
                if (strcmp(player->abilty[i].nome, "Percezione_Divina") == 0)
                {
                    player->Stamina -= player->abilty[i].costo;
                    int CD = 8 + player->bonus_competenza + D6;
                    
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nImposto la CD del Giocatore a %d\n", CD);
                    delay(2);
                    printf("\nLancio Dado sulla CD");
                    for (int i = 0; i < 3; i++)
                    {
                        delay(1);
                        printf(". ");
                    }
                    
                    D20 = rand()% 20 + 1;

                    if (D20 < CD) 
                    {
                        printf("\nHai Fatto: %d, Non hai superato la CD\n", D20);
                        delay(2);
                    }
                    else if (D20 >= CD)
                    {
                        printf("\nHai Fatto: %d, Hai superato la CD\n", D20);
                        delay(2);
                        printf("\nPredico la Prossima Mossa del Nemico");

                        for (int i = 0; i < 5; i++)
                        {
                            printf(". ");
                            delay(1);
                        }

                        printf("\nIl nemico effettuera un tiro 1d20 pari a %d", D20_Enemy);
                        delay(2);
                    }
                }

                //NewAbility_Here

                *activated = 1;
            }
        }
        if (!activated) { printf("\n%c Non puoi usare nessuna Abilita, la tua Stamina ==> %d e' inferiore al costo Abilita !!", sign, player->Stamina); }
    } 
    else 
    {
        printf("\n%c Non puoi usare nessuna Abilita, la tua Stamina e' a 0!!", sign);
    } 

    if (NPC->Vita <0) NPC->Vita = 0;
    delay(1);
    system("@cls||clear");
    LogoTitle();
    Gui_ShowCharacter(*player, *NPC); 
}

void AbilityActionEnemy(CHARACTER *player, CHARACTER *NPC, CHARACTER *stat, int choose, char name_ability[], int *activated, int D20_Enemy)
{
    int D4, D6, D20;
    float HIT;
    char sign = 254;
    srand(time(NULL));

    D4 = rand()%3 + 1;
    D6 = rand()%5 +1;
    if (player->Stamina > 0)
    {
        for (int i = 0; i < player->number_Ability; i++)
        {
            if (choose == 0){ printf("\n%c nessuna Abilita Scelta", 254); delay(2); return;}
            if (choose == player->abilty[i].ID && player->Stamina >= player->abilty[i].costo && player->Level >= player->abilty[i].livello)
            {
    //ATTACCO EXTRA ABILITY (LV. 1)
                if (strcmp(player->abilty[i].Type, "Boost_Life") == 0 )  
                {
                    int dado_Vita = rand()% player->dadoVita + 1;
                    int Tot_Heal = 0;

                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    dado_Vita = rand()% player->dadoVita + 1;
                    Tot_Heal += dado_Vita;

                    player->Vita += Tot_Heal;
                    printf("\nVita Recuperata ");
                    delay(2);
                    printf("=");
                    delay(2);
                    printf("=");
                    delay(2);
                    printf(">");
                    delay(2);
                    printf(" %d", Tot_Heal);
                    delay(2);
                    printf("\nVita Player attuale e' di %d\n", player->Vita);
                }
                                if (strcmp(player->abilty[i].nome, "AttaccoExtra") == 0)
            {
                player->Stamina -= player->abilty[i].costo;
                printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                delay(2);
                printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);
                D20=rand()%19 + 1;
                // calcolo danni
                *NPC = DamageCalculate(*NPC, *player, D20);             
            } 
                if (strcmp(player->abilty[i].nome, "Attacco_Incauto") == 0)
            {
                player->Stamina -= player->abilty[i].costo;
                printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                delay(2);
                printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);
                D20=rand()%19 + 1;

                // calcolo danni
                player->ATK = player->ATK *2;
                player->Armor = player->Armor/2;
                *NPC = DamageCalculate(*NPC, *player, D20);   

                player->ATK = stat->ATK;
                strcpy(name_ability, player->abilty[i].nome);         
            } 
                
                if (strcmp(player->abilty[i].nome, "Ira") == 0)
                {
                    player->Stamina -= player->abilty[i].costo;
                    if (player->Level >= 1  && player->Level <= 3) player->abilty[i].damage = 2;
                    if (player->Level >= 4  && player->Level <= 6) player->abilty[i].damage = 3;
                    if (player->Level >= 7  && player->Level <= 9) player->abilty[i].damage = 4;
                    if (player->Level >= 10 && player->Level <= 15) player->abilty[i].damage = 5;
                    if (player->Level >= 16 && player->Level <= 20) player->abilty[i].damage = 6;
                    if (player->Level >= 21 && player->Level <= 25) player->abilty[i].damage = 7;
                    if (player->Level >= 26 && player->Level <= 35) player->abilty[i].damage = 8;
                    if (player->Level >= 36 && player->Level <= 45) player->abilty[i].damage = 9;
                    if (player->Level >= 46) player->abilty[i].damage = 10;

                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    NPC->Vita -= player->abilty[i].damage;

                    if (NPC->Vita < 0)  NPC->Vita = 0;

                    printf("\nIl %s sprigiona tutta la sua Ira", player->Classe);
                    delay(1);
                    printf("\nDanno Inflitto ");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf(">");
                    delay(1);
                    printf(" %d", player->abilty[i].damage);
                    delay(1);
                    printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                    delay(1);

                }
                if (strcmp(player->abilty[i].nome, "Curare_Le_Ferite") == 0 )  
                {
                    if (player->Vita < stat->Vita)
                    {
                        int D20_TOT = 0;
                        int dado_Vita = player->dadoVita ;
                        int CD = 8 + player->bonus_competenza + D6;
                        int Tot_Heal = 0;

                        player->Stamina -= player->abilty[i].costo;
                        printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                        delay(2);
                        printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                        printf("\nImposto la CD del Giocatore a %d\n", CD);
                        delay(2);
                        printf("\nLancio Dado sulla CD");
                        for (int i = 0; i < 3; i++)
                        {
                            delay(1);
                            printf(". ");
                        }
                        
                        D20 = rand()% 20 + 1;
                        D20_TOT += D20;

                        if (D20 < CD) 
                        {
                            printf("\nHai Fatto: %d, Non hai superato la CD\n", D20_TOT);
                            delay(2);
                        }
                        else if (D20 >= CD)
                        {
                            printf("\nhai Fatto: %d, Hai superato la CD\n", D20_TOT);
                            delay(2);

                            if (player->dadoVita <= 8)
                            {
                                for (int i = 0; i < 2; i++)
                                {
                                    dado_Vita = rand()% player->dadoVita + 1;
                                    Tot_Heal += dado_Vita;
                                }
                            }
                            else
                            {
                                dado_Vita = rand()% player->dadoVita + 1 + player->bonus_competenza;
                                Tot_Heal += dado_Vita;
                            }
                            player->Vita += Tot_Heal;
                            printf("\nVita Recuperata ");
                            delay(2);
                            printf("=");
                            delay(2);
                            printf("=");
                            delay(2);
                            printf(">");
                            delay(2);
                            printf(" %d", Tot_Heal);
                            delay(2);
                            printf("\nVita Player attuale e' di %.0f\n", player->Vita);
                    }

                    }
                    else if (player->Vita >= stat->Vita)
                    { 
                        printf("\nNon puoi usare la Abilita di cura, la tua vita e' gia Full!!"); 
                        return; 
                    }
                    else if (player->Stamina < player->abilty[i].costo) printf("\nIl costo é troppo alto, non puoi usare questa abilita");
                }
                
                if (strcmp(player->abilty[i].nome, "Onda_Di_Tuono") == 0 )
                {
                    int D20_TOT = 0;
                    int dado_Vita = rand()% player->dadoVita + 1;
                    int CD = 8 + player->bonus_competenza + D6;
                    int Tot_Damage = 0;

                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nImposto la CD del Giocatore a %d\n", CD);
                    delay(2);
                    printf("\nLancio Dado sulla CD");
                    for (int i = 0; i < 3; i++)
                    {
                        delay(1);
                        printf(". ");
                    }
                    
                    D20 = rand()% 20 + 1;
                    D20_TOT += D20;

                    if (D20_TOT < CD) 
                    {
                        printf("\nHai Fatto: %d, Non hai superato la CD\n", D20_TOT);
                        delay(2);
                    }
                    else if (D20_TOT >= CD)
                    {
                        printf("\nhai Fatto: %d, Hai superato la CD\n", D20_TOT);
                        delay(2);
                        printf("\nLancio il Dado per i punti Ferita");
                        for (int i = 0; i < 5; i++)
                        {
                            printf(". ");
                            delay(1);
                        }
                        
                        Tot_Damage = player->bonus_competenza + rand()% dado_Vita + 1;
                        NPC->Vita -= Tot_Damage;

                        if (NPC->Vita < 0)  NPC->Vita = 0;

                        printf("\nDanno Inflitto ");
                        delay(1);
                        printf("=");
                        delay(1);
                        printf("=");
                        delay(1);
                        printf(">");
                        delay(1);
                        printf(" %d", Tot_Damage);
                        delay(1);
                        printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                        delay(1);
                    }
                }   
                if (strcmp(player->abilty[i].nome, "Armatura_Magica") == 0 )
                {
                    player->Stamina -= player->abilty[i].costo;
                    player->Armor = 13 + player->bonus_competenza;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nRicalibro la CA del Giocatore a %.0f per 3 Turni\n", player->Armor);
                    delay(2);
                    player->turni = 3;

                }
                if (strcmp(player->abilty[i].nome, "Dardo_Incantato") == 0)
                {
                    int Tot_Damage;
                    player->Stamina -= player->abilty[i].costo;
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    Tot_Damage = D4 + (player->ATK - NPC->Armor);
                    NPC->Vita -= Tot_Damage;

                    printf("\nDardo Incantanto lanciato");
                    for (int i = 0; i < 5; i++)
                    {
                        delay(2);
                        printf(". ");
                    }

                    if (NPC->Vita < 0)  NPC->Vita = 0;

                    printf("\nDanno Inflitto ");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf("=");
                    delay(1);
                    printf(">");
                    delay(1);
                    printf(" %d", Tot_Damage);
                    delay(1);
                    printf("\nVita %s attuale e' di %.2f\n",NPC->Classe, NPC->Vita);
                    delay(1);
                }
                if (strcmp(player->abilty[i].nome, "Percezione_Divina") == 0)
                {
                    player->Stamina -= player->abilty[i].costo;
                    int CD = 8 + player->bonus_competenza + D6;
                    
                    printf("Hai usato %d Stamina, Ti rimane Ancora %.0f Stamina\n\n", player->abilty[i].costo, player->Stamina);
                    delay(2);
                    printf("\n%c %s Attiva\n", 254, player->abilty[i].nome);

                    printf("\nImposto la CD del Giocatore a %d\n", CD);
                    delay(2);
                    printf("\nLancio Dado sulla CD");
                    for (int i = 0; i < 3; i++)
                    {
                        delay(1);
                        printf(". ");
                    }
                    
                    D20 = rand()% 20 + 1;

                    if (D20 < CD) 
                    {
                        printf("\nHai Fatto: %d, Non hai superato la CD\n", D20);
                        delay(2);
                    }
                    else if (D20 >= CD)
                    {
                        printf("\nHai Fatto: %d, Hai superato la CD\n", D20);
                        delay(2);
                        printf("\nPredico la Prossima Mossa del Nemico");

                        for (int i = 0; i < 5; i++)
                        {
                            printf(". ");
                            delay(1);
                        }

                        printf("\nIl nemico effettuera un tiro 1d20 pari a %d", D20_Enemy);
                        delay(2);
                    }
                }

            }
        }
        if (!activated) { printf("\n%c Non puoi usare nessuna Abilita, la tua Stamina ==> %d e' inferiore al costo Abilita !!", sign, player->Stamina); }
    } 
    else 
    {
        printf("\n%c Non puoi usare nessuna Abilita, la tua Stamina e' a 0!!", sign);
    } 

    if (NPC->Vita <0) NPC->Vita = 0;
    delay(1);
    system("@cls||clear");
    LogoTitle();
    Gui_ShowCharacter(*player, *NPC); 
}

//Battle function
CHARACTER BattleFunction_TrainingZone(CHARACTER player, char nomeFile[], int *lv_count)
{
    char sign = 254;
    char path[20] = {"Save Files\\"};
    char DADO[30];
    int randomID = 0;
    int activeted = 0; 
    int D20=0, D20_Enemy = 0; 
    int probabilita_abilita_nemico = 0;
    CHARACTER NPC;
    CHARACTER Stat;
    CHARACTER enemy;
    Stat = player;

//import data of enemy   
    FILE *file;
    Stringa name_file_abilty[10];
    int Number_ability = 0;

    file = fopen("DataBase_Files/CharacterInfoEnemy.txt", "r");

    if (file == NULL)
    {
        printf("\nError Code 216: Cannot Open File");
        exit(1);
    }
    
    srand(time(NULL));
    randomID = rand()%player.Level +1;
    //printf("%d", randomID);
    
    while ( NPC.ID != randomID )
    {
            fscanf(file, "%d", &NPC.ID);
            fscanf(file, "%d", &NPC.Level);
            fscanf(file, "%d", &NPC.dadoVita);
            fscanf(file, "%d", &NPC.bonus_competenza);
            fscanf(file, "%s", NPC.Classe);
            fscanf(file, "%f", &NPC.Vita);
            fscanf(file, "%f", &NPC.Stamina);
            fscanf(file, "%f", &NPC.ATK);
            fscanf(file, "%f", &NPC.Armor);
            fscanf(file, "%d", &NPC.exp);
    }

     Number_ability = ReadAbilitiesEnemy(NPC.Classe, name_file_abilty);

        NPC.number_Ability = Number_ability;
        for (int i = 0; i < NPC.number_Ability; i++)
        {
            char path[70] = {"DataBase_Files//Enemy//"};
            strcat(path, NPC.Classe);
            strcat(path, "//Ability//");
            strcat(path, name_file_abilty[i]);
            //printf("\n%s\n", path);

            file = fopen(path, "r");

            if (file == NULL){ printf("il File non esiste"); exit(-1);}

            NPC.abilty[i].descrip = NULL;

            while (!feof(file))
            {
                Create_Abilita(file, &NPC.abilty[i]);
            }
            fclose(file); 
        }
//                                           //
    enemy = NPC;
do{      
    char name_ability[20];
    delay(1);
    clrscr();
    LogoTitle();
    
    Gui_ShowCharacter(player, NPC);

    if (activeted) printf("%c Abilita Gia' Attivata per questo Turno....\n", 254);

    printf("Comandi Gioco:\n\n%c Per Attaccare digita 'Attacca'\n%c Per Schivare digita 'Schiva'\n%c Per Usare le Abilita' digita 'Abilita'\n\n", 254, 254, 254);
    printf("//---------KeyWords:       ");
    scanf("%s", DADO);

    srand(time(NULL)); //randomizzazione
    if (!activeted)
    {
        D20=rand()%19 + 1;
        D20_Enemy =rand()%19 + 1;
    }

    //Ability Action --> After use ability, pass Automaticly at Normal Attack
    if ((strcmp(DADO, "Abilita") == 0)||(strcmp(DADO, "abilita") == 0) && !activeted && player.Stamina >0)
    {
        int choose;
        clrscr();
        LogoTitle();
    
        Gui_ShowCharacter(player, NPC);
        printf("\nChoose Ability (Choose [ID]):\n\n");

        for (int i = 0; i < player.number_Ability; i++)
        {
            if (player.Level >= player.abilty[i].livello) printf("%c ID: [%d] %s\n", 254, player.abilty[i].ID, player.abilty[i].nome);
        }
        printf("\n//---------KeyWords:       ");
        scanf("%d", &choose);
//  -- ABILITY       
        AbilityAction(&player, &NPC, &Stat, choose, name_ability, &activeted, D20_Enemy);
        if((player.Vita<=0)||(NPC.Vita<=0)){break;}
    }
    else if ((strcmp(DADO, "Abilita") == 0)||(strcmp(DADO, "abilita") == 0) && ( activeted || player.Stamina <= 0))
    { printf("\n%c Non puoi Attivare le Abilita per Questo Turno", 254); delay(2); }


// ATTACK ACTION - Calculate Damage
    if((strcmp(DADO, "Attacca") == 0)||(strcmp(DADO, "attacca") == 0))
    {
        printf("\nAttacco Normale\n");  

        activeted = 0; 

        // calcolo danni
        NPC = DamageCalculate(NPC, player, D20);

        if((player.Vita<=0)||(NPC.Vita<=0)){break;}

        {   //ENEMY TURN
            printf("\n%c Turno del nemico\n\n", sign);
            delay(2);
            printf("Il nemico prova ad attaccare\n");
            delay(2);
            
            if (NPC.Stamina >0){
                probabilita_abilita_nemico = rand() %99 + 1;

                if (probabilita_abilita_nemico >= 50  )
                {
                    printf("Il nemico usa una Abilita\n");
                    delay(2);
                    probabilita_abilita_nemico = rand() %NPC.number_Ability +1;

                    AbilityActionEnemy(&NPC, &player, &enemy, probabilita_abilita_nemico, name_ability, &activeted, D20_Enemy);
                    if((player.Vita<=0)||(NPC.Vita<=0)){break;}
                    printf("Il nemico prova ad attaccare\n");
                    delay(2);
                }
            } 
            
            player = DamageCalculate(player, NPC, D20_Enemy);
        }
        if((player.Vita<=0)||(NPC.Vita<=0)){break;}
    }
    //DODGE ACTION - Damage Calculate

    if(((strcmp(DADO, "Schiva") == 0)||(strcmp(DADO, "schiva") == 0))&&(player.Stamina<=5))
    {
        printf("\n%c Non puoi usare la funzione di 'Schivata', la tua Stamina e' inferiore!!", sign);
        delay(2);
    }

    if( ((strcmp(DADO, "Schiva") == 0)||(strcmp(DADO, "schiva") == 0))&&(player.Stamina>=5))
    {
        activeted = 0; 
        player = DodgeAction(NPC, player);

        {   //ENEMY TURN
            printf("\n%c Turno del nemico\n\n", sign);
            delay(2);
            printf("Il nemico prova ad attaccare\n");
            delay(2);

            player = DamageCalculate(player, NPC, D20_Enemy);
        }
        if((player.Vita<=0)||(NPC.Vita<=0)){break;}
    }

//  -- FIX CHANGE STAT OF PLAYER MODIFIED BY ABILITY
    if (player.turni < 0) player.Armor = Stat.Armor;
    else player.turni --;

    if (player.Armor != Stat.Armor && player.turni == 0) player.Armor = Stat.Armor;
    if (NPC.Armor != enemy.Armor) NPC.Armor = enemy.Armor;
//  --
    if((player.Vita<=0)||(NPC.Vita<=0)){break;}
}
while(NPC.Vita>=0);
        if(player.Vita<=0){

            Stat.ViteSalvezza --;
            if (Stat.ViteSalvezza == 0)
            {
                printf("Hai Esaurito tutte le vite a Disposizione :(\nPartite Persa, Eliminazione del salvataggio Caricamento Main Menu in corso\n");
                for (int i = 0; i < 10; i++)
                    {
                        printf("%c ", sign);
                        delay(1);
                    } 
                strcat(path, nomeFile);
                remove(path);
                delay(1);
                main();
            }
            else
            {
            printf("\nHai perso :(\nTi rimangono ancora %d Vite\n\nCaricamento Game-Mode Menu in Corso (Ricalibrazione Gioco)....\n", Stat.ViteSalvezza);
        
            for (int i = 0; i < 10; i++)
                    {
                        printf("%c ", sign);
                        delay(1);
                    }
            
            return Stat;
            }
        }
        if(NPC.Vita<=0){

            Stat.exp = Stat.exp + NPC.exp;
            LevelUpgrade(&Stat);
            printf("\n\nHai sconfitto il nemico!!!!\n");
            printf("\n\nCaricamento Game-Mode Menu in Corso....");
            delay(5);
            return Stat;
        }

}
