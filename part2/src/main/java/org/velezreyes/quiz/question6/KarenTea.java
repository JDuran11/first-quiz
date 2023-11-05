package org.velezreyes.quiz.question6;

public class KarenTea implements Drink {

    private String name;
    private boolean fizzy;
    public double price;

    public KarenTea() {
        this.name = "KarenTea";
        this.fizzy = false;
        this.price = 1;
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