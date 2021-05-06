define zeroext i1 @fun(float %a, float %c, i1 zeroext %y) #0 {
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
%pont_y = alloca i8, align 1
%cas_1 = zext i1 %y to i8
store i8 %cas_1, i8* %pont_y, align 1
%pont_b = alloca float, align 4
%load_cas_4_c = load float, float* %pont_c, align 4
%cas_3_binopexp = fdiv float %load_cas_4_c, 0x4006666660000000
%cas_2_binopexp = fmul float %cas_3_binopexp, 0x40239999a0000000
store float %cas_2_binopexp, float* %pont_b, align 4
store float 0x400e666660000000, float* %pont_b, align 4
%pont_f = alloca i8, align 1
store i8 1, i8* %pont_f, align 1
%load_cas_5_f = load i8, i8* %pont_f, align 1
%trunc_cas_9 = trunc i8 %load_cas_5_f to i1
br i1 %trunc_cas_9, label %if_cas_6, label %else_cas_7

if_cas_6:
%cas_10_binopexp = fadd float 0x400a666660000000, 0x4011333340000000
store float %cas_10_binopexp, float* %pont_b, align 4
br label %cont_cas_8

else_cas_7:
%cas_11_binopexp = fadd float 0x4019333340000000, 0x401d333340000000
store float %cas_11_binopexp, float* %pont_b, align 4
br label %cont_cas_8

cont_cas_8:
br label %while_cas_12

while_cas_12:
%load_cas_16_y = load i8, i8* %pont_y, align 1
%trunc_cas_15 = trunc i8 %load_cas_16_y to i1
br i1 %trunc_cas_15, label %block_cas_13, label %cont_cas_14

block_cas_13:
%pont_g = alloca i32, align 4
store i32 9, i32* %pont_g, align 4
br label %while_cas_12

cont_cas_14:
%load_cas_17_y = load i8, i8* %pont_y, align 1
%cas_18 = trunc i8 %load_cas_17_y to i1
ret i1 %cas_18
}
define i32 @main() #0 {
%pont_d = alloca i32, align 4
store i32 5, i32* %pont_d, align 4
%load_cas_19_d = load i32, i32* %pont_d, align 4
ret i32 %load_cas_19_d
}