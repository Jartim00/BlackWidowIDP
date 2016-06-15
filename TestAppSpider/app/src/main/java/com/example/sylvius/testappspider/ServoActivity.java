package com.example.sylvius.testappspider;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.widget.GridLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.utils.ColorTemplate;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


/**
 * Created by Sylvius on 9-5-2016.
 */
public class ServoActivity extends Activity {

    //SocketConnection connection class
    SocketConnection socketConnection;

    //Global variables
    Servo servo = new Servo();
    DebugHelper debugHelper = new DebugHelper();
    GridLayout gridView;
    List<LinearLayout> layoutList = new ArrayList<LinearLayout>() {};
    List<Servo> servoList = new ArrayList<Servo>();
    BarChart barChart;
    boolean FOCUSED;

    //{'servos': [{'load': {'H': 3, 'L': 2}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 11, 'temperature': 30}, {'load': {'H': 23, 'L': 23}, 'punch': {'H': 4, 'L': 3}, 'moving': 0, 'voltage': 50, 'position': {'H': 2, 'L': 1}, 'speed': {'H': 24, 'L': 33}, 'id': 12, 'temperature': 30}]}

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.servoview_layout);
        gridView = (GridLayout) findViewById(R.id.gridView);
        barChart = (BarChart) findViewById(R.id.chart);
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
                            Thread.sleep(500);
                        }
                    } catch (JSONException e1) {
                        e1.printStackTrace();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
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
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    });

    //Servo data
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
    private void CreateServos() throws JSONException, IOException {
        if(servoList.size() == 0) {
            socketConnection = new SocketConnection();
            if (socketConnection.ParseServoJSON() != null) {
                JSONArray j = socketConnection.ParseServoJSON();                                               //Get JSONArray from SocketConnection error
                if (j.length() > 0) {
                    for (int i = 0; i < j.length(); i++) {
                        try {
                            JSONObject jObject = j.getJSONObject(i);
                            Servo servo = new Servo(                                                 // Create a new servo Object
                                    jObject.getInt(TAG_ID),                                          // ID OR i if no ID is supplied.
                                    Float.parseFloat(jObject.getString(TAG_POSITION)),               // Get Position value
                                    Float.parseFloat(jObject.getString(TAG_LOAD)),                   // Get Load value
                                    Float.parseFloat(jObject.getString(TAG_TEMPERATURE)),            // Get Temperature value
                                    Float.parseFloat(jObject.getString(TAG_VOLTAGE)),                // Get Voltage value
                                    jObject.getInt(TAG_MOVING)                                       // IsMoving 1 or 0
                            );
                            servoList.add(servo);                                                    //Add servo to the List
                            AddToGridView(servo);                                                    //add servo to the view
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
        else {
            updateServos.start();
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
                    Thread.sleep(100);
                }
            } catch (JSONException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    });

    /*
    * Works basically the same as CreateServo class
    * This class will edit each Servo Object with the new
    * values from the JSON string.
    */
    private void UpdateServos() throws JSONException, IOException {
        try {
            if (socketConnection.ParseServoJSON() != null) {
                int i = 0;
                JSONArray j = socketConnection.ParseServoJSON();
                for (final Servo s : servoList) {
                    if (j.length() > 0) {
                        JSONObject jObject = j.getJSONObject(i);
                        s.setPosition(Float.parseFloat(jObject.getString(TAG_POSITION)));        //Get Position
                        s.setLoad(Float.parseFloat(jObject.getString(TAG_LOAD)));                //Get Load
                        s.setVoltage(Float.parseFloat(jObject.getString(TAG_VOLTAGE)));          //Get Voltage
                        s.setTemperature(Float.parseFloat(jObject.getString(TAG_TEMPERATURE)));  //Get Temperature
                        s.setMoving(jObject.getInt(TAG_MOVING));                                 //Get Moving boolean
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
        } catch (Exception ex){
        }
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                DrawGraph();
            }
        });
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

    /*
    * Creates a BarChart with values from every servo.
    * */
    private void DrawGraph(){ //float Position, float Load, float Temperature, float Voltage, int isMoving
        try {
            //Create new array for each value
            ArrayList<BarEntry> position = new ArrayList<>();
            ArrayList<BarEntry> load = new ArrayList<>();
            ArrayList<BarEntry> temperature = new ArrayList<>();
            ArrayList<BarEntry> voltage = new ArrayList<>();

            //For each servo add values to the arraylist.
            int count = 1;
            for(Servo s : servoList){
                position.add(new BarEntry(s.getPosition(), count));
                load.add(new BarEntry(s.getLoad(), count));
                temperature.add(new BarEntry(s.getTemperature(), count));
                voltage.add(new BarEntry(s.getVoltage(), count));
                count++;
            }

            //Initializing visual setting for each bar, also creates the legend.
            BarDataSet pos_set = new BarDataSet(position, "Position");
            pos_set.setColor(Color.RED);

            BarDataSet load_set = new BarDataSet(load, "Load");
            load_set.setColor(Color.BLUE);

            BarDataSet temp_set = new BarDataSet(temperature, "Temperature");
            temp_set.setColor(Color.GREEN);

            BarDataSet volt_set = new BarDataSet(voltage, "Voltage");
            volt_set.setColor(Color.YELLOW);

            //Add labels to organize data for every servo
            ArrayList<String> labels = new ArrayList<String>();
            for (int i = 1; i < 19; i++) {
                labels.add("Servo" + i);
            }

            ArrayList<BarDataSet> dataSets = new ArrayList<>();  // combined all dataset into an arraylist
            dataSets.add(pos_set);
            dataSets.add(load_set);
            dataSets.add(temp_set);
            dataSets.add(volt_set);

            BarData data = new BarData(labels, dataSets); // initialize the Bardata with argument labels and dataSet
            barChart.setData(data); // set the data and list of lables into chart
            barChart.setDescription("Servos");  // set the description

        } catch (Exception ex){
            //No data available.
        }
    }
}