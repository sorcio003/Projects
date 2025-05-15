package events.root;

public class root {
    private String type;
    private String name;
    private int exp;

    public root(String type, String name, int exp){
        this.type = type;
        this.name = name;
        this.exp = exp;
    }

    /* Getter */

    public String getType(){
        return this.type;
    }

    public String getName(){
        return this.name;
    }

    public int getExp(){
        return this.exp;
    }

    /* Setter */

    public void setName(String name){
        this.name = name;
    }

    public void setType(String type){
        this.type = type;
    }

    public String toString(){
        return "Name: "+name+
             "\nType: "+type+
             "\nEXP : "+exp;
    }
}
