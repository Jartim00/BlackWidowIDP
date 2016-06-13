package com.example.sylvius.testappspider;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;


/*
MainActivity class for starting up the App. Starts the TabClass class.
 */
public class MainActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        setContentView(R.layout.activity_main);
        super.onCreate(savedInstanceState);
        Intent intent = new Intent(MainActivity.this, TabClass.class);
        startActivity(intent);
        finish();
    }
}
