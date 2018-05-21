
//
// 傳入兩數字到 addThreadServer.py 伺服器相加後, 取得結果
//
// SigninActivity.java 的 method 執行次序
//   (1) 建構子函數  : SigninActivity
//   (2) 預先執行程式: onPreExecute() (通常用來做初始化)
//   (3) 背景執行程序: DoInBackground()(AsyncTask 的主程式)
//   (4) 最後執行程序: onPostExecute()(通常用來傳最後結果給MainActivity.java)
//

package com.tom.loginpi;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import android.content.Context;
import android.os.AsyncTask;
import android.widget.TextView;
import android.widget.EditText;
import java.net.Socket;
import java.io.IOException;

// AsyncTask<傳入值型態, 更新進度型態, 結果型態>
// 傳入值型態:String 更新進度型態:Void 結果（回傳）型態: String
public class SigninActivity extends AsyncTask<String,Void,String> {

    private EditText num1Field,num2Field;
    private TextView resultField;
    private Context context;

    public SigninActivity(Context context,EditText num1Field,
                          EditText num2Field,TextView resultField) {
        this.context = context;
        this.num1Field = num1Field;
        this.num2Field = num2Field;
        this.resultField = resultField;
    }
    // 進入預先執行程式
    protected void onPreExecute(){
    }
    // 進入背景執行程序 (即 AsyncTask 的主程式)
    @Override
    protected String doInBackground(String... arg0) {

            try {
                Socket cs = new Socket("192.168.1.16",5050);

                BufferedReader in = new BufferedReader(new InputStreamReader(cs.getInputStream()));
                BufferedWriter out = new BufferedWriter(new OutputStreamWriter(cs.getOutputStream()));

                //傳入 num1, num2 給伺服器
                out.write(num1Field.getText().toString());
                out.flush(); //馬上發送


                // 讀取伺服器傳回的一個相加結果
                //String line = in.readLine(); // 讀取一行回應

                // 讀取傳回至少一行範例
                StringBuffer sb = new StringBuffer("");
                String line = "";
                while ((line = in.readLine()) != null) {
                    sb.append(line);
                    break;
                }

                in.close();
                out.close();
                cs.close();
                //將答案傳給 onPostExecute(result)的 result
                return sb.toString();
                //return line;

            } catch (Exception e) {
                //當斷線時會跳到 catch,可以在這裡寫上斷開連線後的處理
                e.printStackTrace();
                return new String("Exception: " + e.getMessage());
            }
    }
    // 執行最後執行程序, 將結果顯示到 TextView
    @Override
    protected void onPostExecute(String result){
        this.resultField.setText(result);
    }
}
