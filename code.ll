declare i32 @printf(i8*, ...)
define i32 @main() #0 {
%pont_u = alloca i32, align 4
store i32 9, i32* %pont_u, align 4
%pont_y = alloca [10 x i32], align 16
%getelem_cas_1 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 5
store i32 0, i32* %getelem_cas_1, align 8
%pont_j = alloca i32, align 4
%load_cas_3_u = load i32, i32* %pont_u, align 4
%sext_cas_4 = sext i32 %load_cas_3_u to i64
%getelem_cas_6_y = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 %sext_cas_4
%load_cas_5_y = load i32, i32* %getelem_cas_6_y, align 1
%cas_2_binopexp = add nsw i32 %load_cas_5_y, 9
store i32 %cas_2_binopexp, i32* %pont_j, align 4
%call_cas_7_gun = call i32 @gun(i32 5)
ret i32 %call_cas_7_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
%pont_f = alloca i32, align 4
store i32 6, i32* %pont_f, align 4
%pont_r = alloca i32, align 4
%load_cas_9_s = load i32, i32* %pont_s, align 4
%cas_8_binopexp = add nsw i32 %load_cas_9_s, 5
store i32 %cas_8_binopexp, i32* %pont_r, align 4
ret i32 4
}