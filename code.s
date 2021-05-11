	.text
	.file	"code.ll"
	.globl	fun                             # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movss	%xmm0, -16(%rbp)
	movss	%xmm1, -12(%rbp)
	movb	%dil, -1(%rbp)
	movl	$1081291571, -8(%rbp)           # imm = 0x40733333
	movb	$1, -2(%rbp)
	movb	$1, %al
	testb	%al, %al
	je	.LBB0_1
# %bb.2:                                # %else_cas_7
	movl	$1096391066, -8(%rbp)           # imm = 0x4159999A
	jmp	.LBB0_3
.LBB0_1:                                # %if_cas_6
	movl	$1089680180, -8(%rbp)           # imm = 0x40F33334
.LBB0_3:                                # %cont_cas_8
	movb	-1(%rbp), %al
	testb	$1, %al
	je	.LBB0_6
	.p2align	4, 0x90
.LBB0_5:                                # %block_cas_14
                                        # =>This Inner Loop Header: Depth=1
	movq	%rsp, %rcx
	leaq	-16(%rcx), %rsp
	movl	$9, -16(%rcx)
	testb	$1, %al
	jne	.LBB0_5
.LBB0_6:                                # %cont_cas_15
	movb	-1(%rbp), %al
	andb	$1, %al
	movq	%rbp, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	fun, .Lfunc_end0-fun
	.cfi_endproc
                                        # -- End function
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	movl	$5, -4(%rsp)
	movl	$5, %eax
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
