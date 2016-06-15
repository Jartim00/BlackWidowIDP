package com.example.sylvius.testappspider;

import android.app.TabActivity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TabHost;
import android.widget.TextView;

import org.json.JSONArray;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class TabClass extends TabActivity {
    //Global variables
    BatteryData b_data = new BatteryData();
    Thread thread;
    TabHost tabHost;
    ImageView connectionView;
    boolean CONNECTED = false;
    SocketConnection s;
    String battery;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tabs_layout);

        // create the TabHost that will contain the Tabs
        tabHost = (TabHost)findViewById(android.R.id.tabhost);
        connectionView = (ImageView)findViewById(R.id.Connection);

        TabHost.TabSpec tab1 = tabHost.newTabSpec("Servo Data");
        TabHost.TabSpec tab2 = tabHost.newTabSpec("Video View");
        TabHost.TabSpec tab3 = tabHost.newTabSpec("Slope");
        TabHost.TabSpec tab4 = tabHost.newTabSpec("Activity Log");

        // Set the Tab name and Activity
        // that will be opened when particular Tab will be selected
        tab1.setIndicator("Servo Activity");
        tab1.setContent(new Intent(this,ServoActivity.class).addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY));

        tab2.setIndicator("Video View");
        tab2.setContent(new Intent(this,VideoViewActivity.class).addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY));

        tab3.setIndicator("Slope Data");
        tab3.setContent(new Intent(this,SlopeActivity.class).addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY));

        tab4.setIndicator("Activity Log");
        tab4.setContent(new Intent(this,ActivityLogActivity.class).addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY));

        /** Add the tabs  to the TabHost to display. */
        tabHost.addTab(tab1);
        tabHost.addTab(tab2);
        tabHost.addTab(tab3);
        tabHost.addTab(tab4);
        UpdateBatteryStatus();
        tr.start();
    }

    Thread tr = new Thread(){
        public void run(){
           s  = new SocketConnection();
        }
    };

    /*
     * Update method for battery status and connection status.
     * Class has a infinite loop in a thread.
     * TODO: connection status always returns false, rewrite ConnectionAvailable class
     * */
    private void UpdateBatteryStatus(){
        thread = new Thread() {
            public void run() {
                while (true) {
                    try {
                        try {
                            JSONArray j = s.ParseBatteryJSON();//Get JSONArray from SocketConnection class
                            float[] values = new float[j.length()];
                            if (j.length() > 0) {
                                CONNECTED = true;
                                for (int i = 0; i < j.length(); i++) {
                                    values[i] = Float.parseFloat(j.getString(i));
                                }
                                battery = values[0]+ "";
                            }
                        } catch (Exception ex){
                            CONNECTED = false;
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                TextView tv = (TextView) findViewById(R.id.battery_health);
                                tv.setText(battery);
                                if(CONNECTED) {
                                    connectionView.setImageResource(R.mipmap.img_connection);
                                } else {
                                    connectionView.setImageResource(R.mipmap.img_noconnection);
                                }
                            }
                        });
                        Thread.sleep(5000);
                    } catch (InterruptedException e) {
                    }
                }
            }
        };
        thread.start();
    }

    /*
    * Class will check if there is a valid connection between the app and
    * the web server.
    * input: None
    * output: boolean
    */

    private void ConnectionAvailable() {
        Thread connection = new Thread() {
            public void run() {
                    try {
                        JSONArray j = s.ParseBatteryJSON();//Get JSONArray from SocketConnection class
                        float[] values = new float[j.length()];
                        if (j.length() > 0) {
                            CONNECTED = true;
                            for (int i = 0; i < j.length(); i++) {
                                values[i] = Float.parseFloat(j.getString(i));
                            }
                            battery = values[0]+ "";
                        }
                    } catch (Exception ex){
                        CONNECTED = false;
                    }
            }
        };
        connection.start();
    }
}
