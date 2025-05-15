package events;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import events.root.root;

public class boss extends root{

    private String boss_name;
    private int life;
    private int attack;
    private int def;
    private List<String> Ability;

    public boss(String name_events, String boos_name, int exp, int life, int attack, int def){
        super("boss", name_events, exp);
        this.boss_name = boos_name;
        this.life = life;
        this.attack = attack;
        this.def = def;
        this.Ability = new ArrayList<String>();
    }

    public boss(String name_events, String boos_name, int exp){
        super("boss", name_events, exp);
        this.boss_name = boos_name;
        this.life = 150 + (int)( new Random().nextDouble() * 150 );                  // Base life at 150 points + add points up to 300 with random generation
        this.attack = ( this.life / 4 ) + (int)( new Random().nextDouble() * 20 );   // Base Attack at life/4 points + add points up to life/4 + 20 with random generation
        this.def = 15 + (int)( new Random().nextDouble() * 5 );                     // Base Def at 15 points + add points up to 20 with random generation
        this.Ability = new ArrayList<String>();
    }

    public boss(String name_events, String boos_name){
        super("boss", name_events, 51 + new Random().nextInt(50));   // Base exp at 15 points + add points up to 100 with random generation
        this.boss_name = boos_name;
        this.life = 150 + (int)( new Random().nextDouble() * 150 );                  // Base life at 150 points + add points up to 300 with random generation
        this.attack = ( this.life / 2 ) + (int)( new Random().nextDouble() * 20 );   // Base Attack at life/2 points + add points up to life/2 + 20 with random generation
        this.def = 10 + (int)( new Random().nextDouble() * 10 );                     // Base Def at 10 points + add points up to 20 with random generation
        this.Ability = new ArrayList<String>();
    }

    /* Getter */

    public String getBossName(){
        return boss_name;
    }

    public int getBossLife(){
        return life;
    }

    public int getBossAttack(){
        return attack;
    }

    public int getBossDef(){
        return def;
    }

    /* Ability List Modifier */

    public void AddElementToAbilityList(String ability){
        this.Ability.add(ability);
    }

    public void RemoveElementToAbilityListByElement(String ability){
        this.Ability.remove(ability);
    }
    
    public void RemoveElementToAbilityListByID(int id){
        if (id >= 0){
            this.Ability.remove(id);
        }
        else{
            System.out.println("Index must be greater or equal than 0");
        }
    }

    /* Setter */

    public void setBossName(String boss_name){
        this.boss_name = boss_name;
    }

    public void setBossAttack(int attack){
        this.attack = attack;
    }

    public void setBossDef(int def){
        this.def = def;
    }

    public void setBossLife(int life){
        this.life = life;
    }

    public void IncrementBossLife(){
        this.life ++;
    }

    /* Also actepted for decrement with -val */
    public void IncrementBossLife(int val){
        this.life += val;
    }

    public String toString(){
        return "Boss Name: "+boss_name+
             "\nLife     : "+life+
             "\nAttack   : "+attack+
             "\nDef      : "+def+
             "\nAbility  : "+Ability+
             "\n----------------Info Events----------------\n"+super.toString();
    }
}
