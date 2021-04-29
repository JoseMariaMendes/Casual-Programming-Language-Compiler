define float @fun(float %a, float %c) #0 {
%pont_a = alloca float, align 4
store float %a, float* %pont_a, align 4
%pont_c = alloca float, align 4
store float %c, float* %pont_c, align 4
}
define float @main() #0 {
}