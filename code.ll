@.casual_str_cas_1 = private unnamed_addr constant [7 x i8] c"asdasd\00", align 1
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
%pont_p = alloca i8*, align 8
store i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.casual_str_cas_1, i64 0, i64 0), i8** %pont_p, align 8
%getelem_cas_3_b = getelementptr inbounds [10 x i8], [10 x i8]* %pont_b, i64 0, i64 8
%load_cas_2_b = load i8, i8* %getelem_cas_3_b, align 1
%trunc_cas_4 = trunc i8 %load_cas_2_b to i1
%zext_cas_5 = zext i1 %trunc_cas_4 to i8
store i8 %zext_cas_5, i8* %pont_o, align 1
%cas_6 = trunc i8 1 to i1
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
ret i32 4
}