@.casual_str_cas_12 = private unnamed_addr constant [7 x i8] c"hello\0A\00", align 1
@.casual_str_cas_2 = private unnamed_addr constant [7 x i8] c"asdasd\00", align 1
declare i32 @printf(i8*, ...)
define zeroext i1 @fun(i32* %y) #0 {
%pont_y = alloca i32*, align 8
store i32* %y, i32** %pont_y, align 8
%pont_bring = alloca i32, align 4
store i32 0, i32* %pont_bring, align 4
%cas_1 = trunc i8 1 to i1
ret i1 %cas_1
}
define i32 @main() #0 {
%pont_t = alloca [10 x i8], align 16
%pont_b = alloca [10 x i8], align 16
%pont_o = alloca i8, align 1
store i8 1, i8* %pont_o, align 1
%pont_j = alloca i32, align 4
store i32 2, i32* %pont_j, align 4
%pont_z = alloca float, align 4
store float 0x400a666660000000, float* %pont_z, align 4
%pont_ja = alloca [10 x i32], align 16
%pont_fa = alloca [10 x i8*], align 16
%pont_za = alloca [10 x float], align 16
%pont_p = alloca i8*, align 8
store i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.casual_str_cas_2, i64 0, i64 0), i8** %pont_p, align 8
%getelem_cas_5_ja = getelementptr inbounds [10 x i32], [10 x i32]* %pont_ja, i64 0, i64 8
%load_cas_4_ja = load i32, i32* %getelem_cas_5_ja, align 1
%getelem_cas_7_ja = getelementptr inbounds [10 x i32], [10 x i32]* %pont_ja, i64 0, i64 8
%load_cas_6_ja = load i32, i32* %getelem_cas_7_ja, align 1
%cas_3_binopexp = icmp sge i32 %load_cas_6_ja, %load_cas_4_ja
br i1 %cas_3_binopexp, label %if_cas_8, label %else_cas_9

if_cas_8:
%pont_jake = alloca i32, align 4
store i32 8, i32* %pont_jake, align 4
ret i32 1
br label %cont_cas_10

else_cas_9:
ret i32 2
br label %cont_cas_10

cont_cas_10:
%print_cas_13 = call i32 (i8*, ...) @printf (i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.casual_str_cas_12, i64 0, i64 0))
%load_cas_15_j = load i32, i32* %pont_j, align 4
%call_cas_14_gun = call i32 @gun(i32 %load_cas_15_j)
ret i32 %call_cas_14_gun
}
define i32 @gun(i32 %s) #0 {
%pont_s = alloca i32, align 4
store i32 %s, i32* %pont_s, align 4
ret i32 4
}