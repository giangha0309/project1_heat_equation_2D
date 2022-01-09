package com.example.authentication;

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

import com.example.authentication.Code;
import com.example.authentication.CodeDAO;

@Database(entities = {Code.class}, version = 1)
public abstract class CodeDatabase extends RoomDatabase {

    private static final String DATABASE_NAME = "code.db";
    private static CodeDatabase instance;

    public static synchronized CodeDatabase getInstance(Context context) {
        if (instance == null) {
            instance = Room.databaseBuilder(context.getApplicationContext(), CodeDatabase.class, DATABASE_NAME)
                    .allowMainThreadQueries()
                    .build();

        }
        return instance;
    }
    public abstract CodeDAO codeDAO();
}