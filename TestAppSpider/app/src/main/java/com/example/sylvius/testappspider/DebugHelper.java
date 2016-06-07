package com.example.sylvius.testappspider;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Sylvius on 10-5-2016.
 * Object class for the activity log
 */
public class DebugHelper {
    public static List<String> list = new ArrayList<String>();

    public void AddToList(String s){
        list.add(s);
    }

    public List<String> GetList(){
        return list;
    }
}
