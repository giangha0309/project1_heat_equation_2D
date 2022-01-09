package com.example.authentication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.MediaStore;
import android.text.TextUtils;
import android.view.View;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

public class MainActivity extends AppCompatActivity {
    private TextView tvCode;
    private RadioButton rbAdmin;
    private RadioButton rbStaff;
    private List<Code> mListCode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvCode = findViewById(R.id.code_text);
        rbAdmin = findViewById(R.id.admin_button);
        rbStaff = findViewById(R.id.staff_button);
    }

    public void Authentication(View view) {
        mListCode = CodeDatabase.getInstance(this).codeDAO().getListCode();
        String strCode = tvCode.toString();
        Boolean blRole = rbAdmin.isChecked();
        if (TextUtils.isEmpty(strCode) || (!rbAdmin.isChecked() && !rbStaff.isChecked())) {
            Toast.makeText(this, "Please fill out the information completely", Toast.LENGTH_LONG).show();
        }
        if (strCode == "admin123" && blRole == true) {
            launchAdminActivity();
            return;
        }
        if (strCode == "staff123" && blRole == false) {
            launchStaffActivity();
            return;
        }
    }

    public void launchAdminActivity() {
        Intent intent = new Intent(this, AdminActivity.class);
        startActivity(intent);
    }

    public void launchStaffActivity() {
        Intent intent = new Intent(this, StaffActivity.class);
        startActivity(intent);
    }
}