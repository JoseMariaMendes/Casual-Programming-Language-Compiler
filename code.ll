define i32 @fun(i32 %y) #0 {
%pont_y = alloca i32, align 4
store i32 %y, i32* %pont_y, align 4
%load_cas_2_y = load i32, i32* %pont_y, align 4
%cas_1_binopexp = add nsw i32 %load_cas_2_y, 6
store i32 %cas_1_binopexp, i32* %pont_y, align 4
%cas_3_binopexp = icmp eq i32 5, 0
%load_cas_4_y = load i32, i32* %pont_y, align 4
ret i32 %load_cas_4_y
}
define i32 @main() #0 {
ret i32 0
}