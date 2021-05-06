define float @fun(float %a, float %c, i1 zeroext %y) #0 {
%pont_fun = alloca float, align 4
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
%cas_1 = alloca i8, align 1
%pont_y = zext i1 %y to i8
store i8 %pont_y, i8* %cas_1, align 1
%pont_b = alloca float, align 4
%load_c = load float, float* %pont_c, align 4
%cas_3_binopexp = fdiv float %load_c, 0x4006666660000000
%cas_2_binopexp = fmul float %cas_3_binopexp, 0x40239999a0000000
store float %cas_2_binopexp, float* %pont_b, align 4
store float 0x400e666660000000, float* %pont_b, align 4
%load_b = load float, float* %pont_b, align 4
}
define float @main() #0 {
%pont_main = alloca float, align 4
%pont_d = alloca float, align 4
%cas_4_binopexp = fadd float 0x4017333340000000, 0x40219999a0000000
store float %cas_4_binopexp, float* %pont_d, align 4
%load_d = load float, float* %pont_d, align 4
}