define float @fun(float %a, float %c, i1 zeroext %y) #0 {
%pont_fun = alloca float, align 4
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
%pont_y = zext i8 %y, align 1
%pont_b = alloca float, align 4
}
define float @main() #0 {
%pont_main = alloca float, align 4
%pont_d = alloca float, align 4
}