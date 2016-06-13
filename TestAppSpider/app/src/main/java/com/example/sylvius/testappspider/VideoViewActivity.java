package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class VideoViewActivity extends Activity {
    //Global variables
    private String httpLiveUrl = "http://10.1.1.1:5000"; //Video Feed from raspberry
    DebugHelper debugHelper = new DebugHelper();
    WebView videoStream;
    boolean FOCUSED;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView( R.layout.videoview_layout);
        videoStream = (WebView) findViewById(R.id.webView);
    }

    @Override
    protected void onPause(){
        super.onPause();
        videoStream.loadUrl("about:blank"); //Closes the webpage.
        FOCUSED = false;
    }

    @Override
    protected void onResume(){
        super.onResume();
        FOCUSED = true;
        SetupWebView();
    }

    private void SetupWebView(){
        if(FOCUSED) {
            try {
                videoStream.loadUrl(httpLiveUrl); // Load the webpage
                debugHelper.AddToList("DEBUG: VIDEOSTREAM LOADED");
            } catch (Exception ex) {
                debugHelper.AddToList("ERROR: NO VIDEOSTREAM FOUND");
            }
        }
    }
}
