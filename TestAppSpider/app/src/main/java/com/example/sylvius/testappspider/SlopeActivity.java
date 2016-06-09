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
    ImageView img_animation;
    LinearLayout Forward;
    LinearLayout Backward;
    LinearLayout Left;
    LinearLayout Right;

    String serverAddress = "10.1.1.1";
    int port = 1337;

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

    private void Animate(final float xx, final float yy){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                img_animation.setX(img_animation.getX() + xx);
                img_animation.setY(img_animation.getY() + yy);
            }
        });
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
                float x = 0;
                float y = 0;
                while (FOCUSED) {
                    try {
                        JSONObject jsonData = new JSONObject(SocketListener());                                                  //For Webserver
                        if (jsonData != null) {
                            JSONArray j = jsonData.optJSONArray("gyro");                                                  //"servos" = jsonArray name
                            if (j.length() > 0) {
                                for (int i = 0; i < j.length(); i++) {
                                    x = Float.parseFloat(j.getJSONObject(i).getString("X"));
                                    y = Float.parseFloat(j.getJSONObject(i).getString("Y"));
                                }
                            }
                        } else {
                            jsonData = new JSONObject("{'servos':[{'error':'error'}]}");                                    //Debug to prevent crashes.
                        }
                        //Animate(GetSpiderX(),GetSpiderY());
                        final float finalX = x;
                        final float finalY = y;
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Rotate(finalX, finalY);
//                                if(IsMovingForward()){Forward.setVisibility(View.VISIBLE);} else {Forward.setVisibility(View.INVISIBLE)}
//                                if(IsMovingBackward()){Backward.setVisibility(View.VISIBLE);} else {Forward.setVisibility(View.INVISIBLE)}
//                                if(IsMovingLeft()){Left.setVisibility(View.VISIBLE);} else {Forward.setVisibility(View.INVISIBLE)}
//                                if(IsMovingRight()){Right.setVisibility(View.VISIBLE);} else {Forward.setVisibility(View.INVISIBLE)}
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

    private String SocketListener() throws IOException {
        Socket s = new Socket(serverAddress, port);
        BufferedReader input =
                new BufferedReader(new InputStreamReader(s.getInputStream()));
        String answer = input.readLine();
        return answer;
    }
//
//    private float GetSpiderX(){return 0f;} //Don't use this one
//    private float GetSpiderY(){return 0f;} //Nor this one
//    private float GetSpiderRotX(){return -1f;}  //Use this one instead
//    private float GetSpiderRotY(){return 0.1f;} //Add this one
//    private boolean IsMovingForward(){return true;} //Add real value
//    private boolean IsMovingBackward(){return false;}
//    private boolean IsMovingRight(){return true;}
//    private boolean IsMovingLeft(){return false;}
}
