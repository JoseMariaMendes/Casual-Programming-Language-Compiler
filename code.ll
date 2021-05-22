define float @lam(float* %f) #0 {
%pont_f = alloca float*, align 8
store float* %f, float** %pont_f, align 8
%pont_u = alloca float, align 4
store float 0x40229999a0000000, float* %pont_u, align 4
%load_cas_4_u = load float, float* %pont_u, align 4
%load_cas_7 = load float*, float** %pont_f, align 8
%getelem_cas_6_f = getelementptr inbounds float, float* %load_cas_7, i64 1
%load_cas_5_f = load float, float* %getelem_cas_6_f, align 1
%cas_3_binopexp = fadd float %load_cas_5_f, %load_cas_4_u
ret float %cas_3_binopexp
}
define i32 @main() #0 {
%pont_u = alloca float, align 4
store float 0x40229999a0000000, float* %pont_u, align 4
%pont_y = alloca [10 x i32], align 16
%getelem_cas_1 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 4
store i32 3, i32* %getelem_cas_1, align 8
%getelem_cas_2 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 5
store i32 0, i32* %getelem_cas_2, align 8
%getelem_cas_10_y = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 5
%load_cas_9_y = load i32, i32* %getelem_cas_10_y, align 1
%call_cas_8_gun = call i32 @gun(i32 %load_cas_9_y)
ret i32 %call_cas_8_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
%load_cas_12_s = load i32, i32* %pont_s, align 4
%cas_11_binopexp = add nsw i32 %load_cas_12_s, 6
ret i32 %cas_11_binopexp
}