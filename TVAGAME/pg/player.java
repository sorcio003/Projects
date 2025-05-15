package pg;

import java.util.ArrayList;
import java.util.List;

public class player{

    private String name;
    private String class_player;
    private int exp;
    private int life;
    private int attack;
    private int def;
    private List<String> Ability;

    public player(String name){
        this.name = name;
        this.class_player = "Detective";
        this.exp = 1;
        this.life = 50;
        this.attack = 25;
        this.def = 12;
        this.Ability = new ArrayList<String>();
    }

    /* Getter */

    public String getName(){
        return this.name;
    }

    public String getClassPlayer(){
        return this.class_player;
    }

    public int getEXP(){
        return this.exp;
    }

    public int getLife(){
        return this.life;
    }

    public int getAttack(){
        return this.attack;
    }

    public int getDef(){
        return this.def;
    }

    public List<String> getAbilityList(){
        return this.Ability;
    }

    /* Ability List Modifier */

    public void AddElementToAbilityList(String ability){
        Ability.add(ability);
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

    /* Experience */

    public void IncrementEXP(){
        this.exp ++;
    }

    public void IncrementEXP(int exp){
        if (exp < 0){
            this.exp = -exp;
        }
        else{
            this.exp = exp;
        }
    }

    /* Setter */

    public void setName(String name){
        this.name = name;
    }

    public void setClassPlayer(String class_player){
        this.class_player = class_player;
    }

    public void setLife(int life){
        this.life = life;
    }

    public void setAttack(int attack){
        this.attack = attack;
    }

    public void setDef(int def){
        this.def = def;
    }

    public String toString(){
        String expString = "";
        for (int i = 0; i < this.exp; i++) {
            expString += "-";
        };


        return    "Name   : "+name+
                "\nClass  : "+class_player+
                "\nATK    : "+attack+
                "\nDEF    : "+def+
                "\nLIFE   : "+life+
                "\nEXP    : " +expString+
                "\nAbility: "+Ability.toString();
    }
}