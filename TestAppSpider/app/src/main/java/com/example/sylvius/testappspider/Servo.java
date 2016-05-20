package com.example.sylvius.testappspider;

/**
 * Created by Sylvius on 11-5-2016.
 */
public class Servo {
    private int id;
    private float Position,Load, Voltage, Temperature;
    private int IsMoving;
    private String[] allData = new String[]{"ID: "+id,"Position: "+Position+"","Load: "+Load+"","Temperature: "+Temperature+"","Voltage: "+Voltage+""}; //without IsMoving!

    public Servo(int id, float Position, float Load, float Temperature, float Voltage, int isMoving) {
        this.id = id;
        this.Position = Position;
        this.Load = Load;
        this.Temperature = Temperature;
        this.Voltage = Voltage;
        this.IsMoving = isMoving;
    }

    public Servo(){}

    public int getId() {
        return id;
    }

    public float getPosition() {
        return Position;
    }

    public void setPosition(float position) {
        Position = position;
    }
    public float getLoad(){
        return Load;
    }
    public void setLoad(float load){
        Load = load;
    }
    public float getVoltage() {
        return Voltage;
    }
    public void setVoltage(float voltage) {
        Voltage = voltage;
    }
    public float getTemperature() {
        return Temperature;
    }
    public void setTemperature(float temperature) {
        Temperature = temperature;
    }
    public int isMoving() {
        return IsMoving;
    }

    public void setMoving(int moving) {
        IsMoving = moving;
    }

    public String[] getAllData(){
        allData = new String[]{"ID: "+this.getId(),"Position: "+this.getPosition()+"","Load: "+this.getLoad()+"","Temperature: "+this.getTemperature()+"","Voltage: "+this.getVoltage()+""};
        return allData;
    }
}
