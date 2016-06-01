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
        String s = "88% ";
        Date date = new Date();
        if(date.getHours() >= 17){
            s = s + "Wtf are you on school?";
        }
        return s;
    }
}
