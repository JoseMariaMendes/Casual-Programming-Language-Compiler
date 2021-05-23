	.text
	.file	"code.ll"
	.globl	lam                     # -- Begin function lam
	.p2align	4, 0x90
	.type	lam,@function
lam:                                    # @lam
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movl	20(%rdi), %eax
	movl	$5, -12(%rsp)
	addl	$5, %eax
	retq
.Lfunc_end0:
	.size	lam, .Lfunc_end0-lam
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	subq	$104, %rsp
	.cfi_def_cfa_offset 112
	movabsq	$25769803779, %rax      # imm = 0x600000003
	movq	%rax, 32(%rsp)
	movl	$5, 12(%rsp)
	leaq	16(%rsp), %rdi
	callq	lam
	movl	%eax, 12(%rsp)
	addq	$104, %rsp
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
                                        # kill: def $edi killed $edi def $rdi
	movl	%edi, -4(%rsp)
	leal	6(%rdi), %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
