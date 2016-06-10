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

    public SocketConnection() {
        try {
            s = new Socket(serverAddress, port);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String SocketListener() {
        try {
            BufferedReader input =
                    new BufferedReader(new InputStreamReader(s.getInputStream()));
            String answer = input.readLine();
            Log.w("KEKLE", answer);
            return answer;
        } catch (Exception ex){
            ex.printStackTrace();
            return null;
        }
    }

    public JSONArray ParseServoJSON() throws JSONException, IOException {
        return ParseJSON("servos");
    }

    public JSONArray ParseGyroJSON() throws JSONException, IOException {
        return ParseJSON("gyro");
    }

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
