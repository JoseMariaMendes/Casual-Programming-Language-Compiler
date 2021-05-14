@.casual_str_cas_17 = private unnamed_addr constant [7 x i8] c"maria\0A\00", align 1
@.casual_str_cas_14 = private unnamed_addr constant [7 x i8] c"fgsdfg\00", align 1
@.casual_str_cas_1 = private unnamed_addr constant [6 x i8] c"dfkas\00", align 1
define float @fun(float %a, float %c) #0 {
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
%pont_h = alloca i8*, align 8
store i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.casual_str_cas_1, i64 0, i64 0), i8** %pont_h, align 8
%pont_y = alloca i8*, align 8
%load_cas_2_h = load i8*, i8** %pont_h, align 8
store i8* %load_cas_2_h, i8** %pont_y, align 8
store float 0x3ff19999a0000000, float* %pont_c, align 4
%pont_b = alloca float, align 4
%load_cas_4_c = load float, float* %pont_c, align 4
%cas_3_binopexp = fadd float %load_cas_4_c, 0x40019999a0000000
store float %cas_3_binopexp, float* %pont_b, align 4
%load_cas_6_a = load float, float* %pont_a, align 4
%cas_5_binopexp = fcmp une float %load_cas_6_a, 0x4012000000000000
br i1 %cas_5_binopexp, label %if_cas_7, label %else_cas_8

if_cas_7:
%load_cas_12_b = load float, float* %pont_b, align 4
%load_cas_13_a = load float, float* %pont_a, align 4
%cas_11_binopexp = fdiv float %load_cas_13_a, %load_cas_12_b
store float %cas_11_binopexp, float* %pont_a, align 4
br label %else_cas_8

else_cas_8:
store i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.casual_str_cas_14, i64 0, i64 0), i8** %pont_h, align 8
%pont_fran = alloca float, align 4
%load_cas_15_a = load float, float* %pont_a, align 4
store float %load_cas_15_a, float* %pont_fran, align 4
%pont_f = alloca i8, align 1
store i8 1, i8* %pont_f, align 1
%load_cas_16_a = load float, float* %pont_a, align 4
ret float %load_cas_16_a
}
define i32 @dun() #0 {
ret i32 9
}
define i32 @main() #0 {
%pont_maria = alloca i8*, align 8
store i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.casual_str_cas_17, i64 0, i64 0), i8** %pont_maria, align 8
%pont_a = alloca float, align 4
store float 0x4012666660000000, float* %pont_a, align 4
%pont_oscar = alloca i32, align 4
store i32 5, i32* %pont_oscar, align 4
%pont_d = alloca float, align 4
%call_cas_19_fun = call float @fun(float 0x400cccccc0000000, float 0x4016666660000000)
%cas_18_binopexp = fsub float %call_cas_19_fun, 0x4016ccccc0000000
store float %cas_18_binopexp, float* %pont_d, align 4
%pont_c = alloca [100 x i32], align 16
%getelem_cas_20 = getelementptr inbounds [100 x i32], [100 x i32]* %pont_c, i64 0, i64 0
store i32 3, i32* %getelem_cas_20, align 8
%getelem_cas_22_c = getelementptr inbounds [100 x i32], [100 x i32]* %pont_c, i64 0, i64 8
%load_cas_21_c = load i32, i32* %getelem_cas_22_c, align 1
ret i32 %load_cas_21_c
}