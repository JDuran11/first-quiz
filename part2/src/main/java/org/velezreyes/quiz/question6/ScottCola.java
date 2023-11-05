package org.velezreyes.quiz.question6;

public class ScottCola implements Drink {
    private String name;
    private boolean fizzy;
    public double price;

    public ScottCola(){
        this.name = "ScottCola";
        this.fizzy = true;
        this.price = 0.75;
    }

    @Override
    public String getName(){
        return this.name;
    }

    @Override
    public boolean isFizzy(){
        return this.fizzy;
    }
}