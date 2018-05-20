
//
//  Android AsyncTask Client Sample Program
//
//  Author: Gwo-Chuan Lee
//          Date: 2018.05.13
//
//  使用 AsyncTask 建立 Android Client 的背景執行程式
//  呼叫 SinginActivity 將主程式的輸入資料傳給 SininActivity.java
//     的 AsyncTask 物件
//

package com.tom.loginpi;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText num1Field,num2Field;
    private TextView resultField;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1Field = (EditText)findViewById(R.id.editText);
        //num2Field = (EditText)findViewById(R.id.editText2);
        resultField = (TextView)findViewById(R.id.textView2);
    }

    public void AddTwoNumber(View view){
        new SigninActivity(this,num1Field,num2Field,resultField).execute();
    }

    public void CloseApp(View view){
        System.exit(0);
    }
}
