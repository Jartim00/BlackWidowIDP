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
        connection.start();
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
        GetControllerData();
    }

    Thread connection = new Thread(){
        public void run() {
            socket = new SocketConnection();
        }
    };

    //Rotates the Image according to the Gyroscope data
    private  void Rotate(final float x, final float y){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                img_animation.setRotationX(x);
                img_animation.setRotationY(y);
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
                        JSONArray j = socket.ParseGyroJSON();//Get JSONArray from SocketConnection class
                        if (j.length() > 0) {
                            float[] values = new float[j.length()];
                            for (int i = 0; i < j.length(); i++) {
                                values[i] = Float.parseFloat(j.getString(i));
                            }
                            x = values[0];
                            y = values[1];
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
                    } catch (Exception ex){

                    }
                }
            }
        };
        thread.start();
    }

    private void GetControllerData() throws IllegalThreadStateException{
        thread = new Thread() {
            public void run() {
                float x = 0; //Assign x and y to 0
                float y = 0;
                while (FOCUSED) {
                    try {
                        JSONArray j = socket.ParseMovementJSON();//Get JSONArray from SocketConnection class
                        if (j.length() > 0) {
                            float[] values = new float[j.length()];
                            for (int i = 0; i < j.length(); i++) {
                                values[i] = Float.parseFloat(j.getString(i));
                            }
                            x = values[0];
                            y = values[1];
                        }
                        final float finalX = x; //Temporary store variables in a final variable
                        final float finalY = y;
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                SetMovementNeutral();
                                if(finalX > 5){
                                    Right.setVisibility(View.VISIBLE);
                                } if(finalX < 5) {
                                    Left.setVisibility(View.VISIBLE);
                                } if(finalY > 5) {
                                    Forward.setVisibility(View.VISIBLE);
                                } if(finalY < 5) {
                                    Backward.setVisibility(View.VISIBLE);
                                }
                            }
                        });
                        Thread.sleep(100);
                    } catch (InterruptedException e) {

                    } catch (JSONException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (Exception ex){

                    }
                }
            }
        };
        thread.start();
    }

    private void SetMovementNeutral(){
        Right.setVisibility(View.INVISIBLE);
        Left.setVisibility(View.INVISIBLE);
        Forward.setVisibility(View.INVISIBLE);
        Backward.setVisibility(View.INVISIBLE);
    }
}
