
// Android 將 Main Thread用來處理UI,
// 因此需要使用Thread讓大量運算在背景跑, 卻不影響使用者操作的畫面,
// 而如果需要畫面更新, 則會透過Handler機制去更新

package com.tom.loginpi;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Handler;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Button;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import android.app.Activity;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    private EditText num1Field,num2Field;
    private TextView resultField;
    private Button btnStart,btnClose;

    private Thread thread;                //執行緒
    private Socket clientSocket;          //客戶端的socket
    private BufferedWriter out;           //取得網路輸出串流
    private BufferedReader in;            //取得網路輸入串流
    private String line;                  //做為接收時的緩存

    private Handler handler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1Field = (EditText)findViewById(R.id.editText);
        num2Field = (EditText)findViewById(R.id.editText2);
        resultField = (TextView)findViewById(R.id.textView2);

        btnStart = (Button)findViewById(R.id.button);
        btnClose = (Button)findViewById(R.id.button1);
        btnStart.setOnClickListener(btnStartListener);
        btnClose.setOnClickListener(btnCloseListener);
    }

    private Button.OnClickListener btnStartListener = new Button.OnClickListener() {
        @Override
        public void onClick(View v) {
            thread = new Thread(Connection);  //賦予執行緒工作
            thread.start();                   //讓執行緒開始執行
        }
    };

    private Button.OnClickListener btnCloseListener = new Button.OnClickListener() {
        @Override
        public void onClick(View v) {
            System.exit(0);
        }
    };

    //連結socket伺服器做傳送與接收
    private Runnable Connection=new Runnable(){
        @Override
        public void run() {
            // TODO Auto-generated method stub
            try{

                clientSocket = new Socket("192.168.0.122",5050);

                //取得網路輸出串流
                out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
                // 取得網路輸入串流
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

                while (clientSocket.isConnected()) {

                    // 將輸入兩數傳給 addThreadServer.py
                    //数据的结尾加上换行符才可让服务器端的readline()停止阻塞
                    out.write(num1Field.getText().toString());
                    out.flush();
                    out.write(num2Field.getText().toString());
                    out.flush();
                    // 取得伺服器回傳的結果
                    line = in.readLine();   //宣告一個緩衝,從br串流讀取值

                    while (line != null) {
                        handler.post(new Runnable() {
                            public void run() {
                                resultField.setText(line);
                            }
                        });
                    }
                }
            }catch(Exception e){
                //當斷線時會跳到catch,可以在這裡寫上斷開連線後的處理
                e.printStackTrace();
                Log.e("text","Socket連線="+e.toString());
            }
        }
    };

    @Override
    protected void onDestroy() { //當銷毀該app時
        super.onDestroy();
        try {
            //關閉輸出入串流後,關閉Socket
            out.close();
            in.close();
            clientSocket.close();
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            Log.e("text","onDestroy()="+e.toString());
        }
    }
}
