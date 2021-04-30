@.casual_str_cas_1 = private unnamed_addr constant [7 x i8] c"maria\0A\00", align 1
define float @fun(float %a, float %c) #0 {
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
store float 0x3ff19999a0000000, float* %pont_c, align 4
%pont_b = alloca float, align 4
%pont_f = alloca i8, align 1
store i8 1, i8* %pont_f, align 1
}
define float @main() #0 {
%pont_maria = alloca i8*, align 8
store i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str, i64 0, i64 0), i8** %pont_maria, align 8
%pont_a = alloca float, align 4
store float 0x4012666660000000, float* %pont_a, align 4
%pont_oscar = alloca i32, align 4
store i32 5, i32* %pont_oscar, align 4
%pont_d = alloca float, align 4
}