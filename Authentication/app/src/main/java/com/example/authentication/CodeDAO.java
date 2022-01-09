package com.example.authentication;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;

import com.example.authentication.Code;

import java.util.List;

public interface CodeDAO {
    @Insert
    void insertCode(Code code);

    @Query ("select * from code")
    List<Code> getListCode();

    @Delete
    void deleteUser(Code code);
}
