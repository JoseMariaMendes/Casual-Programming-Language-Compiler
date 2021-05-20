	.text
	.file	"code.ll"
	.globl	fun                     # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movl	$0, -12(%rsp)
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
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$224, %rsp
	movb	$1, -1(%rbp)
	movl	$2, -12(%rbp)
	movl	$1079194419, -8(%rbp)   # imm = 0x40533333
	movq	$.L.casual_str_cas_2, -24(%rbp)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB1_2
# %bb.1:                                # %if_cas_8
	movq	%rsp, %rax
	leaq	-16(%rax), %rsp
	movl	$8, -16(%rax)
	movl	$1, %eax
	jmp	.LBB1_3
.LBB1_2:                                # %else_cas_9
	movl	$2, %eax
.LBB1_3:                                # %else_cas_9
	movq	%rbp, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
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
