define i32 @lam(i32* %f) #0 {
%pont_f = alloca i32*, align 8
store i32* %f, i32** %pont_f, align 8
%load_cas_7 = load i32*, i32** %pont_f, align 8
%getelem_cas_6_f = getelementptr inbounds i32, i32* %load_cas_7, i64 5
%load_cas_5_f = load i32, i32* %getelem_cas_6_f, align 1
%pont_u = alloca i32, align 4
store i32 6, i32* %pont_u, align 4
%load_cas_8_u = load i32, i32* %pont_u, align 4
%cas_4_binopexp = add nsw i32 %load_cas_5_f, %load_cas_8_u
ret i32 %cas_4_binopexp
}
define i32 @main() #0 {
%pont_y = alloca [10 x i32], align 16
%getelem_cas_1 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 4
store i32 3, i32* %getelem_cas_1, align 8
%pont_p = alloca i32, align 4
store i32 6, i32* %pont_p, align 4
%pont_u = alloca i32, align 4
store i32 6, i32* %pont_u, align 4
%pont_john = alloca [10 x float], align 16
%getelem_cas_2 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 5
store i32 6, i32* %getelem_cas_2, align 8
%load_cas_10_y = getelementptr inbounds [10 x i32], [10 x i32]* %pont_y, i64 0, i64 0
%call_cas_9_lam = call i32 @lam(i32* %load_cas_10_y)
store i32 %call_cas_9_lam, i32* %pont_u, align 4
%load_cas_11_u = load i32, i32* %pont_u, align 4
ret i32 %load_cas_11_u
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
%load_cas_13_s = load i32, i32* %pont_s, align 4
%cas_12_binopexp = add nsw i32 %load_cas_13_s, 6
ret i32 %cas_12_binopexp
}