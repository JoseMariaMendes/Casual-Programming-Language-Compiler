define zeroext i1 @fun(i32* %y) #0 {
%pont_y = alloca i32*, align 8
store i32* %y, i32** %pont_y, align 8
%pont_t = alloca [10 x i8], align 16
%pont_b = alloca [10 x i8], align 16
%pont_o = alloca i8, align 1
store i8 1, i8* %pont_o, align 1
%getelem_cas_2_b = getelementptr inbounds [10 x i8], [10 x i8]* %pont_b, i64 0, i64 8
%load_cas_1_b = load i8, i8* %getelem_cas_2_b, align 1
%trunc_cas_3 = trunc i8 %load_cas_1_b to i1
%zext_cas_4 = zext i1 %trunc_cas_3 to i8
store i8 %zext_cas_4, i8* %pont_o, align 1
%load_cas_5_o = load i8, i8* %pont_o, align 1
%cas_6 = trunc i8 %load_cas_5_o to i1
ret i1 %cas_6
}
define i32 @main() #0 {
%pont_r = alloca i32, align 4
store i32 9, i32* %pont_r, align 4
%load_cas_8_r = load i32, i32* %pont_r, align 4
%call_cas_7_gun = call i32 @gun(i32 %load_cas_8_r)
ret i32 %call_cas_7_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
store i32 3, i32* %pont_s, align 4
%pont_r = alloca i32, align 4
store i32 2, i32* %pont_r, align 4
%load_cas_10_r = load i32, i32* %pont_r, align 4
%load_cas_11_s = load i32, i32* %pont_s, align 4
%cas_9_binopexp = icmp eq i32 %load_cas_11_s, %load_cas_10_r
br i1 %cas_9_binopexp, label %if_cas_12, label %else_cas_13

if_cas_12:
ret i32 0
br label %cont_cas_14

else_cas_13:
ret i32 1
br label %cont_cas_14

cont_cas_14:
ret i32 0
}