package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Adapter;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.List;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class ActivityLogActivity extends Activity {
    ListView listView;
    DebugHelper debugHelper = new DebugHelper();
    private ArrayAdapter<String> debugAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView( R.layout.activitylogview_layout);
        LoadList();
    }

    @Override
    protected void onResume(){
        super.onResume();
        setContentView( R.layout.activitylogview_layout);
        LoadList();
    }

    private void LoadList(){
        try {
            listView = (ListView) findViewById(R.id.debug_log);
            List<String> list = debugHelper.GetList(); //get the list
            debugAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, list);
            listView.setAdapter(debugAdapter);
        } catch (Exception ex){

        }
    }
}
