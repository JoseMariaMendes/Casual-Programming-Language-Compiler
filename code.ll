define i32 @fun(i32* %y) #0 {
%pont_y = alloca i32*, align 8
store i32* %y, i32** %pont_y, align 8
%pont_u = alloca i32, align 4
store i32 9, i32* %pont_u, align 4
%pont_t = alloca [10 x i32], align 16
%getelem_cas_1 = getelementptr inbounds [10 x i32], [10 x i32]* %pont_t, i64 0, i64 0
store i32 7, i32* %getelem_cas_1, align 8
ret i32 6
}
define i32 @main() #0 {
%pont_d = alloca i32, align 4
store i32 5, i32* %pont_d, align 4
%load_cas_2_d = load i32, i32* %pont_d, align 4
ret i32 %load_cas_2_d
}