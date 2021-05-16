	.text
	.file	"code.ll"
	.globl	fun                     # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movb	$1, %al
	retq
.Lfunc_end0:
	.size	fun, .Lfunc_end0-fun
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	subq	$120, %rsp
	.cfi_def_cfa_offset 128
	movb	$1, -113(%rsp)
	movl	$2, -108(%rsp)
	movl	$1079194419, -112(%rsp) # imm = 0x40533333
	movq	$.L.casual_str_cas_2, -104(%rsp)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB1_2
# %bb.1:                                # %if_cas_8
	movl	$1, %eax
	addq	$120, %rsp
	.cfi_def_cfa_offset 8
	retq
.LBB1_2:                                # %else_cas_9
	.cfi_def_cfa_offset 128
	movl	$2, %eax
	addq	$120, %rsp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.globl	gun                     # -- Begin function gun
	.p2align	4, 0x90
	.type	gun,@function
gun:                                    # @gun
	.cfi_startproc
# %bb.0:
	movl	%edi, -4(%rsp)
	movl	$4, %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.type	.L.casual_str_cas_12,@object # @.casual_str_cas_12
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.casual_str_cas_12:
	.asciz	"hello\n"
	.size	.L.casual_str_cas_12, 7

	.type	.L.casual_str_cas_2,@object # @.casual_str_cas_2
.L.casual_str_cas_2:
	.asciz	"asdasd"
	.size	.L.casual_str_cas_2, 7

	.section	".note.GNU-stack","",@progbits
