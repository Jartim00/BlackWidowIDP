package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ImageView;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class SlopeActivity extends Activity {
    ImageView img_animation;
    DebugHelper debugHelper = new DebugHelper();
    Thread thread;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView( R.layout.slopeview_layout);
        img_animation = (ImageView) findViewById(R.id.spider);
        GetSlopeData_Loop();
    }

    private void Animate(final float xx, final float yy){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                img_animation.setX((float) (img_animation.getX() + xx));
                img_animation.setY((float) (img_animation.getY() + yy));
            }
        });
    }

    private  void Rotate(final float xrot, final float yrot){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                img_animation.setRotationX((float)(img_animation.getRotationX()) + xrot);
                img_animation.setRotationY((float)(img_animation.getRotationY()) + yrot);
            }
        });
    }

    private void GetSlopeData_Loop(){
        thread = new Thread() {
            public void run() {
                while (true) {
                    try {
                        Animate(GetSpiderX(),GetSpiderY());
                        Rotate(GetSpiderRotX(), GetSpiderRotY());
                        Thread.sleep(6);
                    } catch (InterruptedException e) {

                    }
                }
            }
        };
        thread.start();
    }
    private float GetSpiderX(){return 0f;}
    private float GetSpiderY(){return 0f;}
    private float GetSpiderRotX(){return -1f;}
    private float GetSpiderRotY(){return 0.1f;}
}
