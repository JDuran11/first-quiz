package org.velezreyes.quiz.question6;

public class VendingMachineDrinks implements VendingMachine {

    private double money; 

    public VendingMachineDrinks(){
        this.money = 0;
    }

    @Override
    public void insertQuarter(){
        this.money += 0.25;
    }

    @Override
    public Drink pressButton(String drink) throws NotEnoughMoneyException, UnknownDrinkException{
        
        if (drink.equals("KarenTea")){
            
            KarenTea selectdrink = new KarenTea();

            if (this.money < selectdrink.price){
                throw new NotEnoughMoneyException();
            }else if (this.money >= selectdrink.price){
                this.money -= selectdrink.price;
                return new KarenTea();
            }
        }else if (drink.equals("ScottCola")){

            ScottCola selectdrink = new ScottCola();

            if (this.money < selectdrink.price){
                throw new NotEnoughMoneyException();
            }else if (this.money >= selectdrink.price){
                this.money -= selectdrink.price;
                return new ScottCola();
            }
        }


        throw new UnknownDrinkException();

    }
}