package com.example.authentication;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity (tableName = "code")

public class Code {
    private String code;
    private boolean role;

    public Code(String code, boolean role) {
        this.code = code;
        this.role = role;  // 0: staff, 1: admin
    }

    public String getCode() {
        return code;
    }

    public boolean getRole() {
        return role;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public void setRole(boolean role) {
        this.role = role;
    }
}
