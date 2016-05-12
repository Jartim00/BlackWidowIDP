package com.example.sylvius.testappspider;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;

/**
 * Created by Sylvius on 9-5-2016.
 */
public class VideoViewActivity extends Activity {
    private String httpLiveUrl = "http://141.252.236.44:5000"; //Video Feed from raspberry
    DebugHelper debugHelper = new DebugHelper();
    WebView videoStream;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView( R.layout.videoview_layout);
        videoStream = (WebView) findViewById(R.id.webView);
        SetupWebView();
    }

    private void SetupWebView(){
        try {
            videoStream.loadUrl(httpLiveUrl);
            debugHelper.AddToList("DEBUG: VIDEOSTREAM LOADED");
        } catch (Exception ex){
            debugHelper.AddToList("ERROR: NO VIDEOSTREAM FOUND");
        }
    }
}
