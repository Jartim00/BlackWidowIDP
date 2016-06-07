package com.example.sylvius.testappspider;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
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
    //Global variables
    Servo servo = new Servo();
    DebugHelper debugHelper = new DebugHelper();
    GridLayout gridView;
    List<LinearLayout> layoutList = new ArrayList<LinearLayout>() {};
    List<Servo> servoList = new ArrayList<Servo>();
    boolean FOCUSED;

    //{'servos': [{'load': {'H': 3, 'L': 2}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 11, 'temperature': 30}, {'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 12, 'temperature': 30}]}
    private static String url = "http://10.1.1.1:5000/api";//Connection with Raspberry for json //\\ http://10.1.1.1:5000/api || http://141.252.236.44:5000/api

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.servoview_layout);
        gridView = (GridLayout) findViewById(R.id.gridView);
        Start.start();
    }

    @Override
    protected void onPause() {
        super.onPause();
        if(updateServos != null){
            Thread moribund = updateServos;
            updateServos = null;
            moribund.interrupt();
        }
        FOCUSED = false;
    }

    @Override
    protected void onResume() {
        super.onResume();
        debugHelper.AddToList("DEBUG: SERVO ACTIVITY LOADED.");
        FOCUSED = true;
            updateServos = new Thread()
            {
                @Override
                public void run() {
                    try {
                        while (FOCUSED) {
                            UpdateServos();
                            Thread.sleep(1000);
                        }
                    } catch (JSONException e1) {
                        e1.printStackTrace();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            };
        updateServos.start();
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
            try {
                CreateServos();
            } catch (JSONException e) {
            }
        }
    });

    //Adding tags to retrieve data from jsondata
    String TAG_ID = "id";
    String TAG_POSITION = "position";
    String TAG_LOAD = "load";
    String TAG_VOLTAGE = "voltage";
    String TAG_TEMPERATURE = "temperature";
    String TAG_MOVING = "moving";

    /*
    * Class will get JSON String, parses it and creates a new servo for each
    * of the servos in the JSON string.
    * Then a call to AddToGridView will be made to visually add them on the screen.
    */
    private void CreateServos() throws JSONException {
        JSONParser jParser = new JSONParser();                                                              //Parser for webserver
        JSONObject jsonData = jParser.getJSONFromUrl(url);                                                  //For Webserver
        if (jsonData != null) {
            JSONArray j = jsonData.optJSONArray("servos");                                                  //"servos" = jsonArray name
            if (j.length() > 0) {
                for (int i = 0; i < j.length(); i++) {
                    try {
                        Servo servo = new Servo(                                                            // Create a new servo Object
                                j.getJSONObject(i).getInt(TAG_ID),                                          // ID OR i if no ID is supplied.
                                Float.parseFloat(j.getJSONObject(i).getString(TAG_POSITION)),               // Get Position value
                                Float.parseFloat(j.getJSONObject(i).getString(TAG_LOAD)),                   // Get Load value
                                Float.parseFloat(j.getJSONObject(i).getString(TAG_TEMPERATURE)),            // Get Temperature value
                                Float.parseFloat(j.getJSONObject(i).getString(TAG_VOLTAGE)),                // Get Voltage value
                                j.getJSONObject(i).getInt(TAG_MOVING)                                       // IsMoving 1 or 0
                        );
                        servoList.add(servo);                                                               //Add servo to the List
                        AddToGridView(servo);                                                               //add servo to the view
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
            }
        } else {
            jsonData = new JSONObject("{'servos':[{'error':'error'}]}");                                    //Debug to prevent crashes.
        }
    }

    /*
    * Infinite Thread to update servo data
    */
    Thread updateServos = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                while (FOCUSED) {   // if ServoActivity is visible, update servos.
                    UpdateServos();
                    Thread.sleep(1000);
                }
            } catch (JSONException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    });

    /*
    * Works basically the same as CreateServo class
    * This class will edit each Servo Object with the new
    * values from the JSON string.
    */
    private void UpdateServos() throws JSONException {
        JSONParser jParser = new JSONParser();                  //Parser for webserver
        JSONObject jsonData = jParser.getJSONFromUrl(url);      //For Webserver
        if (jsonData != null) {
            JSONArray j = jsonData.optJSONArray("servos");          //array name
            int i = 0;
            for (final Servo s : servoList) {
                if (j.length() > 0) {
                    s.setPosition(Float.parseFloat(j.getJSONObject(i).getString(TAG_POSITION)));    //PresentPosL
                    s.setLoad(Float.parseFloat(j.getJSONObject(i).getString(TAG_LOAD)));
                    s.setVoltage(Float.parseFloat(j.getJSONObject(i).getString(TAG_VOLTAGE)));                                     //PresentVoltage
                    s.setTemperature(Float.parseFloat(j.getJSONObject(i).getString(TAG_TEMPERATURE)));                                //Temperature
                    s.setMoving(j.getJSONObject(i).getInt(TAG_MOVING));                                                               //IsMoving
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            EditGridView(s);
                        }
                    });
                }
                i++;
            }
        } else {
            jsonData = new JSONObject("{'servos':[{'error':'error'}]}");
        }
    }

    /*
    * Visually adds the servos, with data, to the gridlayout.
    * Add a lime green background if the servo is moving,
    * or a red background if the servo is not moving.
     */
    private void AddToGridView(Servo s) {
        final LinearLayout layout = new LinearLayout(this);     //Create new layout for each servo
        layout.setId(s.getId());
        if (s.getAllData().length > 0) {
            if (s.isMoving() == 1) { //
                layout.setBackgroundColor(Color.parseColor("#99FF00")); //Lime Green
            } else {
                layout.setBackgroundColor(Color.parseColor("#FF0000")); //Red
            }
            for (int i = 0; i < s.getAllData().length; i++) {
                TextView textView = new TextView(this);
                textView.setTextSize(11);
                textView.setText(s.getAllData()[i]); //get all data from a servo
                layout.addView(textView);
            }
        }
        // Add them to the screen
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
                layout.setPadding(15, 15, 15, 15);
                layoutParams.gravity = Gravity.TOP;
                layout.setLayoutParams(layoutParams);
                layout.setOrientation(LinearLayout.VERTICAL);           //Orientation
                gridView.addView(layout);
            }
        });
        layoutList.add(layout);
    }

    /*
    * Edit each of the servo layouts with the new data
     */
    private void EditGridView(final Servo s) {
        LinearLayout ll = (LinearLayout) findViewById(s.getId());
        if (s.getAllData().length > 0 && ll != null) {
            if (s.isMoving() == 1) { //red color if a servo is not moving, lime green for a moving servo
                ll.setBackgroundColor(Color.parseColor("#99FF00"));
            } else {
                ll.setBackgroundColor(Color.parseColor("#FF0000"));
            }
            for (int i = 0; i < s.getAllData().length; i++) { //get the new servo data from the list.
                TextView textView = (TextView) ll.getChildAt(i);
                textView.setText(s.getAllData()[i]);
            }
        }
    }
}