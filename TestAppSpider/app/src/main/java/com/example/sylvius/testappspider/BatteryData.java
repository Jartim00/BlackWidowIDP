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
        String s = "69% ";
        Date date = new Date();
        if(date.getHours() >= 17){
            s = s + "Is het tijd voor bier?";
        }
        return s;
    }
}
