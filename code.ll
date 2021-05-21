declare i32 @printf(i8*, ...)
define i32 @lam(i32 %f) #0 {
%pont_f = alloca i32, align 4
store i32 %f, i32* %pont_f, align 4
%load_cas_10_f = load i32, i32* %pont_f, align 4
%cas_9_binopexp = add nsw i32 %load_cas_10_f, 3
ret i32 %cas_9_binopexp 
}
define i32 @main() #0 {
%pont_u = alloca i32, align 4
store i32 9, i32* %pont_u, align 4
%pont_y = alloca [10 x i32], align 16
%load_cas_1_u = load i32, i32* %pont_u, align 4
%sext_cas_2 = sext i32 %load_cas_1_u to i64
%getelem_cas_3 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 %sext_cas_2
store i32 3, i32* %getelem_cas_3, align 8
%pont_j = alloca i32, align 4
%load_cas_5_u = load i32, i32* %pont_u, align 4
%sext_cas_6 = sext i32 %load_cas_5_u to i64
%getelem_cas_8_y = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 %sext_cas_6
%load_cas_7_y = load i32, i32* %getelem_cas_8_y, align 1
%cas_4_binopexp = add nsw i32 %load_cas_7_y, 9
store i32 %cas_4_binopexp, i32* %pont_j, align 4
%load_cas_12_j = load i32, i32* %pont_j, align 4
%call_cas_11_gun = call i32 @gun(i32 %load_cas_12_j)
ret i32 %call_cas_11_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
%load_cas_14_s = load i32, i32* %pont_s, align 4
%cas_13_binopexp = add nsw i32 %load_cas_14_s, 3
ret i32 %cas_13_binopexp
}