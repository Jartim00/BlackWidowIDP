package com.example.sylvius.testappspider;

import java.util.Date;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class BatteryData {

    BatteryData(){

    }

    public String GetBatteryPercentage(){
        //stuff
        String s = "69% : Is het tijd voor bier? ";
        Date date = new Date();
        if(date.getHours() >= 15){
            s += "Ja";
        } else {
            s += "Nein";
        }
        return s;
    }
}
