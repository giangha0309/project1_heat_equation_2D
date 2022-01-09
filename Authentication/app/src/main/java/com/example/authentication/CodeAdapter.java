package com.example.authentication;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RadioButton;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.authentication.R;

import java.util.List;

public class CodeAdapter extends RecyclerView.Adapter<CodeAdapter.UserViewHolder>{

    private List<Code> mListCode;

    public void setData(List<Code> List) {
        this.mListCode = List;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_code, parent, false);
        return new UserViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull UserViewHolder holder, int position) {
        Code code = mListCode.get(position);
        if (code == null) return;
        holder.tvCode.setText(code.getCode());
        holder.rbStaff.setChecked(!code.getRole());
        holder.rbAdmin.setChecked(!code.getRole());
    }

    @Override
    public int getItemCount() {
        if (mListCode != null) return mListCode.size();
        return 0;
    }

    public class UserViewHolder extends RecyclerView.ViewHolder {
        private TextView tvCode;
        private RadioButton rbStaff;
        private RadioButton rbAdmin;

        public UserViewHolder(@NonNull View itemView) {
            super(itemView);

            tvCode = itemView.findViewById(R.id.code_tv);
            rbStaff = itemView.findViewById(R.id.staff_rb);
            rbAdmin = itemView.findViewById(R.id.admin_rb);
        }
    }
}