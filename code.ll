@.casual_str_cas_1 = private unnamed_addr constant [6 x i8] c"hello\00", align 1
define i8* @main() #0 {
%pont_d = alloca i8*, align 8
store i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.casual_str_cas_1, i64 0, i64 0), i8** %pont_d, align 8
%load_cas_2_d = load i8*, i8** %pont_d, align 8
ret i8* %load_cas_2_d
}