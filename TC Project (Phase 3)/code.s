	.text
	.file	"code.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	movq	$.L.casual_str_cas_1, -8(%rsp)
	movl	$.L.casual_str_cas_1, %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.L.casual_str_cas_1,@object     # @.casual_str_cas_1
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.casual_str_cas_1:
	.asciz	"hello"
	.size	.L.casual_str_cas_1, 6

	.section	".note.GNU-stack","",@progbits
