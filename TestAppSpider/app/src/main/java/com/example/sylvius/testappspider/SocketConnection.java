package com.example.sylvius.testappspider;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by Sylvius on 9-6-2016.
 */
public class SocketConnection {
    //Connection Variables
    String serverAddress = "10.1.1.1";
    int port = 1337;

    public SocketConnection(){

    }

    private String SocketListener() throws IOException {
        java.net.Socket s = new java.net.Socket(serverAddress, port);
        BufferedReader input =
                new BufferedReader(new InputStreamReader(s.getInputStream()));
        String answer = input.readLine();
        return answer;
    }

    public JSONArray ParseServoJSON() throws JSONException, IOException {
        return ParseJSON("gyro");
    }

    public JSONArray ParseGyroJSON() throws JSONException, IOException {
        return ParseJSON("gyro");
    }

    private JSONArray ParseJSON(String arrayName) throws IOException, JSONException {
        JSONObject jsonData = new JSONObject(SocketListener());             //For Webserver
        if (jsonData != null) {
            //arrayName = JSONArray to get
            return jsonData.optJSONArray(arrayName);
        } else {
            jsonData = new JSONObject("{'error':[{'error':'error'}]}");    //Debug to prevent crashes.
            return jsonData.optJSONArray(arrayName);
        }
    }

}
