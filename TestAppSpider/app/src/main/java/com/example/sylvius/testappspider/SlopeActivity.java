package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class SlopeActivity extends Activity {
    //SocketConnection connection
    SocketConnection socket;

    ImageView img_animation;
    LinearLayout Forward;
    LinearLayout Backward;
    LinearLayout Left;
    LinearLayout Right;

    DebugHelper debugHelper = new DebugHelper();
    Thread thread;

    boolean FOCUSED;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView( R.layout.slopeview_layout);
        img_animation = (ImageView) findViewById(R.id.spider);
        Forward = (LinearLayout) findViewById(R.id.Forward);
        Backward = (LinearLayout) findViewById(R.id.Backward);
        Left = (LinearLayout) findViewById(R.id.Left);
        Right = (LinearLayout) findViewById(R.id.Right);
    }

    @Override
    protected void onPause(){
        super.onPause();
        FOCUSED = false;
    }

    @Override
    protected void onResume(){
        super.onResume();
        FOCUSED = true;
        GetSlopeData_Loop();
    }

    //Rotates the Image according to the Gyroscope data
    private  void Rotate(final float x, final float y){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                img_animation.setRotationX(img_animation.getRotationX() + x);
                img_animation.setRotationY(img_animation.getRotationY() + y);
            }
        });
    }

    private void GetSlopeData_Loop() throws IllegalThreadStateException{
        thread = new Thread() {
            public void run() {
                float x = 0; //Assign x and y to 0
                float y = 0;
                while (FOCUSED) {
                    try {
                        socket = new SocketConnection();
                        if(socket.ParseGyroJSON() != null) {
                            JSONArray j = socket.ParseGyroJSON();                            //Get JSONArray from SocketConnection class
                            if (j.length() > 0) {
                                for (int i = 0; i < j.length(); i++) {
                                    x = Float.parseFloat(j.getJSONObject(i).getString("X")); //Set x and y to the data from JSON string
                                    y = Float.parseFloat(j.getJSONObject(i).getString("Y"));
                                }
                            }
                        }
                        final float finalX = x; //Temporary store variables in a final variable
                        final float finalY = y;
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Rotate(finalX, finalY);
                            }
                        });
                        Thread.sleep(100);
                    } catch (InterruptedException e) {

                    } catch (JSONException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        };
        thread.start();
    }
}
