package com.example.sylvius.testappspider;

import android.util.Log;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Sylvius on 11-5-2016.
 */
public class Servo {
    private int id;
    private String PresentPositionL, PresentPositionH, PresentSpeedL, PresentSpeedH,PresentLoadL,PresentLoadH, PresentVoltage, Temperature, PunchL, PunchH;
    private int IsMoving;
    private String[] allData = new String[]{id+"",PresentLoadL+"",PresentLoadH+"", PresentSpeedL+"", PresentSpeedH+"",
            PresentPositionL+"", PresentPositionH+"", PresentVoltage+"", Temperature+"", PunchL+"", PunchH+""}; //without IsMoving!

    public Servo(int id, String presentPositionL, String presentPositionH, String presentSpeedL, String presentSpeedH, String presentLoadL, String presentLoadH, String presentVoltage, String temperature, String punchL, String punchH, int isMoving) {
        this.id = id;
        PresentPositionL = presentPositionL;
        PresentPositionH = presentPositionH;
        PresentSpeedL = presentSpeedL;
        PresentSpeedH = presentSpeedH;
        PresentLoadL = presentLoadL;
        PresentLoadH = presentLoadH;
        PresentVoltage = presentVoltage;
        Temperature = temperature;
        PunchL = punchL;
        PunchH = punchH;
        IsMoving = isMoving;
    }

    public Servo(){

    }

    public int GetID(){
        return id;
    }

    public String getPresentPositionL() {
        return PresentPositionL;
    }

    public String getPresentPositionH() {
        return PresentPositionH;
    }

    public String getPresentSpeedL() {
        return PresentSpeedL;
    }

    public String getPresentSpeedH() {
        return PresentSpeedH;
    }

    public String getPresentLoadL() {
        return this.PresentLoadL;
    }

    public String getPresentLoadH() {
        return PresentLoadH;
    }

    public String getPresentVoltage() {
        return PresentVoltage;
    }

    public String getTemperature() {
        return Temperature;
    }

    public String getPunchL() {
        return PunchL;
    }

    public String getPunchH() {
        return PunchH;
    }

    public String[] getAllData(){
        allData = new String[]{this.GetID()+"",this.getPresentLoadL(),this.getPresentLoadH(), this.getPresentSpeedL(), this.getPresentSpeedH(),
                this.getPresentPositionL(), this.getPresentPositionH(), this.getPresentVoltage(), this.getTemperature(), this.getPunchL(), this.getPunchH()};
        return allData;
    }

    public int isMoving(){
        return IsMoving;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setPresentPositionL(String presentPositionL) {
        PresentPositionL = presentPositionL;
    }

    public void setPresentPositionH(String presentPositionH) {
        PresentPositionH = presentPositionH;
    }

    public void setPresentSpeedL(String presentSpeedL) {
        PresentSpeedL = presentSpeedL;
    }

    public void setPresentSpeedH(String presentSpeedH) {
        PresentSpeedH = presentSpeedH;
    }

    public void setPresentLoadL(String presentLoadL) {
        this.PresentLoadL = presentLoadL;
    }

    public void setPresentLoadH(String presentLoadH) {
        this.PresentLoadH = presentLoadH;
    }

    public void setPresentVoltage(String presentVoltage) {
        PresentVoltage = presentVoltage;
    }

    public void setTemperature(String temperature) {
        Temperature = temperature;
    }

    public void setPunchL(String punchL) {
        PunchL = punchL;
    }

    public void setPunchH(String punchH) {
        PunchH = punchH;
    }

    public void setMoving(int moving) {
        IsMoving = moving;
    }
}
