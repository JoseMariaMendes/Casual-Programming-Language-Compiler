define zeroext i1 @fun(i32* %y) #0 {
%pont_y = alloca i32*, align 8
store i32* %y, i32** %pont_y, align 8
%pont_t = alloca [10 x i8], align 16
%pont_b = alloca [10 x i8], align 16
%pont_o = alloca i8, align 1
store i8 1, i8* %pont_o, align 1
%pont_j = alloca i32, align 4
store i32 2, i32* %pont_j, align 4
%pont_z = alloca float, align 4
store float 0x400a666660000000, float* %pont_z, align 4
%pont_ja = alloca [10 x i32], align 16
%pont_fa = alloca [10 x i8*], align 16
%pont_za = alloca [10 x float], align 16
%getelem_cas_2_b = getelementptr inbounds [10 x i8], [10 x i8]* %pont_b, i64 0, i64 8
%load_cas_1_b = load i8, i8* %getelem_cas_2_b, align 1
%trunc_cas_3 = trunc i8 %load_cas_1_b to i1
%zext_cas_4 = zext i1 %trunc_cas_3 to i8
store i8 %zext_cas_4, i8* %pont_o, align 1
%cas_5 = trunc i8 1 to i1
ret i1 %cas_5
}
define i32 @main() #0 {
%pont_r = alloca i32, align 4
store i32 9, i32* %pont_r, align 4
%load_cas_7_r = load i32, i32* %pont_r, align 4
%call_cas_6_gun = call i32 @gun(i32 %load_cas_7_r)
ret i32 %call_cas_6_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
ret i32 4
}