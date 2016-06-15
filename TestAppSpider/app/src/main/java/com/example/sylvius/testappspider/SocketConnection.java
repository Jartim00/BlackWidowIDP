package com.example.sylvius.testappspider;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * Created by Sylvius on 9-6-2016.
 */
public class SocketConnection {
    //Connection Variables
    String serverAddress = "10.1.1.1";
    int port = 1337;
    Socket s;

    /*
    * Opens the socket connection when a new instance of this class is created
    */
    public SocketConnection() {
        try {
            s = new Socket(serverAddress, port);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*
    * Catches incoming Socket messages
    * Returns the message as a String
    */
    private String SocketListener() {
        try {
            BufferedReader input =
                    new BufferedReader(new InputStreamReader(s.getInputStream()));
            String answer = input.readLine();
            return answer;
        } catch (Exception ex){
            ex.printStackTrace();
            return null;
        }
    }

    //Public class to be called when getting servo data
    //returns data as a JSON array
    public JSONArray ParseServoJSON() throws JSONException, IOException {
        return ParseJSON("servos");
    }

    //Public class to be called when getting gyro data
    //returns data as a JSON array
    public JSONArray ParseGyroJSON() throws JSONException, IOException {
        return ParseJSON("gyro");
    }

    //Public class to be called when getting movement (controller input) data
    //returns data as a JSON array
    public JSONArray ParseMovementJSON() throws JSONException, IOException {
        return ParseJSON("joy_pos");
    }

    //Public class to be called when getting battery data
    //returns data as a JSON array
    public JSONArray ParseBatteryJSON() throws JSONException, IOException {
        return ParseJSON("spiderBattery");
    }

    /*
    * Class for Parsing JSON input
    * Input: Arrayname as String
    * Output: JSON data as JSON array
    */
    private JSONArray ParseJSON(String arrayName) throws IOException, JSONException {
        try {
            JSONObject jsonData = new JSONObject(SocketListener());             //For Webserver
            if (jsonData != null) {
                //arrayName = JSONArray to get
                return jsonData.optJSONArray(arrayName);
            } else {
                jsonData = new JSONObject("{'error':[{'error':'error'}]}");    //Debug to prevent crashes.
                return jsonData.optJSONArray(arrayName);
            }
        } catch (Exception ex){
            ex.printStackTrace();
            return null;
        }
    }

}
