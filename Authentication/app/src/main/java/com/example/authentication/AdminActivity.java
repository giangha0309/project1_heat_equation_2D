package com.example.authentication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;


public class AdminActivity extends AppCompatActivity{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.admin_main);
    }

    public void launchAddActivity(View view) {
        Intent intent = new Intent(this, AddCodeActivity.class);
        startActivity(intent);
    }

    public void launchDeleteActivity(View view) {
        Intent intent = new Intent(this, DeleteCodeActivity.class);
        startActivity(intent);
    }
}
