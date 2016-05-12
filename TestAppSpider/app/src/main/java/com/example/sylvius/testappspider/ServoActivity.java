package com.example.sylvius.testappspider;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.GridLayout;
import android.widget.LinearLayout;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;


/**
 * Created by Sylvius on 9-5-2016.
 */
public class ServoActivity extends Activity {

    Servo servo = new Servo();
    DebugHelper debugHelper = new DebugHelper();

    GridLayout gridView;
    List<LinearLayout> layoutList = new ArrayList<LinearLayout>() {
    };
    List<Servo> servoList = new ArrayList<Servo>();

    //{'servos': [{'load': {'H': 3, 'L': 2}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 11, 'temperature': 30}, {'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 12, 'temperature': 30}]}
    private static String url = "http://141.252.236.44:5000/api";//Connection with Raspberry for json //\\ http://10.1.1.1:5000/api || http://141.252.236.44:5000/api

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        debugHelper.AddToList("DEBUG: SERVO ACTIVITY LOADED.");
        setContentView(R.layout.servoview_layout);
        gridView = (GridLayout) findViewById(R.id.gridView);
        Start.start();
    }

    Thread Start = new Thread(new Runnable() {
        @Override
        public void run() {
            createServos.start();
        }
    });

    Thread createServos = new Thread(new Runnable() {
        @Override
        public void run() {
            CreateServos();
        }
    });

    String tests = "{'servos':  [{'load': {'H': 3, 'L': 2}, 'punch': {'H': 4, 'L': 3}, 'moving': 1, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 11, 'temperature': 30}, " +
                                "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 12, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 13, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 21, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 22, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 23, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 31, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 32, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 33, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 41, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 42, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 43, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 51, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 52, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 53, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 61, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 62, 'temperature': 30}," +
            "{'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 63, 'temperature': 30}" +
            "]}";
    String TAG_ID = "id";
    String TAG_L = "L";
    String TAG_H = "H";
    String TAG_ARRAY_SPEED = "speed";
    String TAG_ARRAY_LOAD = "load";
    String TAG_ARRAY_PUNCH = "punch";
    String TAG_ARRAY_POSITION = "position";
    String TAG_MOVING = "moving";
    String TAG_VOLTAGE = "voltage";
    String TAG_TEMPERATURE = "temperature";

    private void CreateServos() {
        JSONParser jParser = new JSONParser();                  //Parser for webserver
        JSONObject jsonData = null;//jParser.getJSONFromUrl(url);      //For Webserver
        try {
            jsonData = new JSONObject(tests);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        JSONArray j = jsonData.optJSONArray("servos");          //TODO: get array final name.
        if (j.length() > 0) {
            for (int i = 0; i < j.length(); i++) {
                //int id, double PresentPositionL, double PresentPositionH, double PresentSpeedL, double PresentSpeedH, double PresentLoadL,
                //double PresentLoadH, double PresentVoltage, double Temperature, boolean IsMoving, double PunchL, double PunchH
                try {
                    Servo servo = new Servo(
                            j.getJSONObject(i).getInt(TAG_ID),                                                         //ID OR i if no ID is supplied.
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_POSITION).getString(TAG_L),     //PresentPosL
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_POSITION).getString(TAG_H),     //PresentPosH
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_SPEED).getString(TAG_L),     //PresentSpeedL
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_SPEED).getString(TAG_H),     //PresentSpeedH
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_LOAD).getString(TAG_L),     //PresentLoadL
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_LOAD).getString(TAG_H),     //PresentLoadH
                            j.getJSONObject(i).getString(TAG_VOLTAGE),     //PresentVoltage
                            j.getJSONObject(i).getString(TAG_TEMPERATURE),     //Temperature
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_PUNCH).getString(TAG_L),    //PunchL
                            j.getJSONObject(i).getJSONObject(TAG_ARRAY_PUNCH).getString(TAG_H),     //PunchH
                            j.getJSONObject(i).getInt(TAG_MOVING)    //IsMoving
                    );
                    servoList.add(servo);
                    AddToGridView(servo);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }//add them to the view
        updateServos.start();
    }

    Thread updateServos = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                while (true) {
                    UpdateServos();
                    updateServos.sleep(1000);
                }
            } catch (JSONException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    });

    private void UpdateServos() throws JSONException {
        JSONParser jParser = new JSONParser();                  //Parser for webserver
        JSONObject jsonData = null;//jParser.getJSONFromUrl(url);      //For Webserver
        try {
            jsonData = new JSONObject(tests);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        JSONArray j = jsonData.optJSONArray("servos");          //TODO: get array final name.
        int i = 0;
        for (final Servo s : servoList) {
            if (j.length() > 0) {
                //int id, double PresentPositionL, double PresentPositionH, double PresentSpeedL, double PresentSpeedH, double PresentLoadL,
                //double PresentLoadH, double PresentVoltage, double Temperature, boolean IsMoving, double PunchL, double PunchH
                //j.getInt(0),        //ID OR i if no ID is supplied. NOT NEEDED HERE
                s.setPresentPositionL("Position L: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_POSITION).getString(TAG_L));    //PresentPosL
                s.setPresentPositionH("Position H: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_POSITION).getString(TAG_H));    //PresentPosH
                s.setPresentSpeedL("Speed L: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_SPEED).getString(TAG_L));             //PresentSpeedL
                s.setPresentSpeedH("Speed H: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_SPEED).getString(TAG_H));             //PresentSpeedH
                s.setPresentLoadL("Load L: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_LOAD).getString(TAG_L));                //PresentLoadL
                s.setPresentLoadH("Load H: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_LOAD).getString(TAG_H));                //PresentLoadH
                s.setPresentVoltage("Voltage: " + j.getJSONObject(i).getString(TAG_VOLTAGE));                                     //PresentVoltage
                s.setTemperature("Temperature: " + j.getJSONObject(i).getString(TAG_TEMPERATURE));                                //Temperature
                s.setMoving(j.getJSONObject(i).getInt(TAG_MOVING));                                                               //IsMoving
                s.setPunchL("Punch L: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_PUNCH).getString(TAG_L));                    //PunchL
                s.setPunchH("Punch H: " + j.getJSONObject(i).getJSONObject(TAG_ARRAY_PUNCH).getString(TAG_H));                    //PunchH
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        EditGridView(s);
                    }
                });
            }
            i++;
        }
    }

    private void AddToGridView(Servo s) {
        final LinearLayout layout = new LinearLayout(this);     //Create new layout for each servo
        layout.setId(s.GetID());
        if (s.getAllData().length > 0) {
            if (s.isMoving() == 1) { //
                layout.setBackgroundColor(Color.parseColor("#99FF00"));
            } else {
                layout.setBackgroundColor(Color.parseColor("#FF0000"));
            }
            for (int i = 0; i < s.getAllData().length; i++) {
                TextView textView = new TextView(this);
                textView.setText(s.getAllData()[i]);
                layout.addView(textView);
            }
        }
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
                layout.setPadding(5, 5, 5, 5);
                layoutParams.setMargins(5,5,5,5);
                layoutParams.gravity = Gravity.TOP;
                layout.setLayoutParams(layoutParams);
                layout.setOrientation(LinearLayout.VERTICAL);           //Orientation
                gridView.addView(layout);
            }
        });
        layoutList.add(layout);
    }

    private void EditGridView(final Servo s) {
        LinearLayout ll = (LinearLayout) findViewById(s.GetID());
        if (s.getAllData().length > 0) {
            if (s.isMoving() == 1) { //
                ll.setBackgroundColor(Color.parseColor("#99FF00"));
            } else {
                ll.setBackgroundColor(Color.parseColor("#FF0000"));
            }
            for (int i = 0; i < s.getAllData().length; i++) {
                TextView textView = (TextView) ll.getChildAt(i);
                textView.setText(s.getAllData()[i]);
            }
        }
    }
}