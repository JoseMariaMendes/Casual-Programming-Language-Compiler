define i32 @fun(i32 %i1, i32 %i2, i32 %i3, i32 %i4) #0 {
%pont_i1 = alloca i32, align 4
store i32 %i1, i32* %pont_i1, align 4
%pont_i2 = alloca i32, align 4
store i32 %i2, i32* %pont_i2, align 4
%pont_i3 = alloca i32, align 4
store i32 %i3, i32* %pont_i3, align 4
%pont_i4 = alloca i32, align 4
store i32 %i4, i32* %pont_i4, align 4
%load_cas_6_i1 = load i32, i32* %pont_i1, align 4
%load_cas_7_i2 = load i32, i32* %pont_i2, align 4
%cas_5_binopexp = icmp slt i32 %load_cas_6_i1, %load_cas_7_i2
br i1 %cas_5_binopexp, label %if_cas_1, label %else_cas_2

&&_cas_9:
%load_cas_11_i3 = load i32, i32* %pont_i3, align 4
%load_cas_12_i4 = load i32, i32* %pont_i4, align 4
%cas_10_binopexp = icmp slt i32 %load_cas_11_i3, %load_cas_12_i4
br %cas_10_binopexp, label 

&&_cas_14:
%load_cas_16_i3 = load i32, i32* %pont_i3, align 4
%load_cas_17_i1 = load i32, i32* %pont_i1, align 4
%cas_15_binopexp = icmp sge i32 %load_cas_16_i3, %load_cas_17_i1
br %cas_15_binopexp, label 

&&_cas_18:
%load_cas_20_i2 = load i32, i32* %pont_i2, align 4
%cas_19_binopexp = icmp eq i32 %load_cas_20_i2, 6
br i1 None, label %if_cas_1, label %else_cas_2

if_cas_1:
ret i32 0
br label %else_cas_2

else_cas_2:
%load_cas_21_i2 = load i32, i32* %pont_i2, align 4
ret i32 %load_cas_21_i2
}
define i32 @main() #0 {
ret i32 0
}