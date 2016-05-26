package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class SlopeActivity extends Activity {
    ImageView img_animation;
    LinearLayout Forward;
    LinearLayout Backward;
    LinearLayout Left;
    LinearLayout Right;

    DebugHelper debugHelper = new DebugHelper();
    Thread thread;

    boolean FOCUSSED;

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
        FOCUSSED = false;
    }

    @Override
    protected void onResume(){
        super.onResume();
        FOCUSSED = true;
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
                while (FOCUSSED) {
                    try {
                        //Animate(GetSpiderX(),GetSpiderY());
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Rotate(GetSpiderRotX(), GetSpiderRotY());
                                if(IsMovingForward()){Forward.setVisibility(View.VISIBLE);}
                                if(IsMovingBackward()){Backward.setVisibility(View.VISIBLE);}
                                if(IsMovingLeft()){Left.setVisibility(View.VISIBLE);}
                                if(IsMovingRight()){Right.setVisibility(View.VISIBLE);}
                            }
                        });
                        Thread.sleep(6);
                    } catch (InterruptedException e) {

                    }
                }
            }
        };
        thread.start();
    }

    private float GetSpiderX(){return 0f;} //Don't use this one
    private float GetSpiderY(){return 0f;} //Nor this one
    private float GetSpiderRotX(){return -1f;}  //Use this one instead
    private float GetSpiderRotY(){return 0.1f;} //Add this one
    private boolean IsMovingForward(){return true;} //Add real value
    private boolean IsMovingBackward(){return false;}
    private boolean IsMovingRight(){return true;}
    private boolean IsMovingLeft(){return false;}
}
