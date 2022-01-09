package com.example.authentication;


import android.app.Activity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;


import java.util.ArrayList;
import java.util.List;

public class AddCodeActivity extends AppCompatActivity {

    private EditText edtCode;
    private RadioButton rbAddStaff;
    private RadioButton rbAddAdmin;
    private Button btAddCode;
    private RecyclerView rvCode;

    private CodeAdapter codeAdapter;
    private List<Code> mListCode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.add_code);

        initUi();

        codeAdapter = new CodeAdapter();
        mListCode = new ArrayList<>();
        codeAdapter.setData(mListCode);

        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(this);
        rvCode.setLayoutManager(linearLayoutManager);

        rvCode.setAdapter(codeAdapter);

        btAddCode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                addUser();
            }
        });
    }

    private void addUser() {
        String strCode = edtCode.getText().toString().trim();
        Boolean blRole = rbAddAdmin.isChecked();

        if (TextUtils.isEmpty(strCode) || (!rbAddAdmin.isChecked() && !rbAddStaff.isChecked())) {
            Toast.makeText(this, "Please fill out the information completely", Toast.LENGTH_LONG).show();
            return;
        }

        Code code = new Code(strCode, blRole);
        CodeDatabase.getInstance(this).codeDAO().insertCode(code);
        Toast.makeText(this, "Add identifier code successfully", Toast.LENGTH_LONG).show();

        edtCode.setText("");
        rbAddAdmin.setChecked(false);
        rbAddStaff.setChecked(false);

        hideSoftKeyboard();

        mListCode = CodeDatabase.getInstance(this).codeDAO().getListCode();
        codeAdapter.setData(mListCode);
    }

    private void initUi() {
        edtCode = findViewById(R.id.code_add_text);
        rbAddStaff = findViewById(R.id.staff_add_button);
        rbAddAdmin = findViewById(R.id.admin_add_button);
        btAddCode = findViewById(R.id.code_add_button);
    }

    public void hideSoftKeyboard() {
        try {
            InputMethodManager inputMethodManager = (InputMethodManager) getSystemService(Activity.INPUT_METHOD_SERVICE);
            inputMethodManager.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(), 0);
        } catch (NullPointerException ex) {
            ex.printStackTrace();
        }
    }
}