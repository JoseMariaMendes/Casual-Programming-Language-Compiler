define i32 @main() #0 {
%pont_d = alloca i32, align 4
store i32 5, i32* %pont_d, align 4
%load_cas_1_d = load i32, i32* %pont_d, align 4
ret i32 %load_cas_1_d
}