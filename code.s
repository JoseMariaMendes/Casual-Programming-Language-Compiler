	.text
	.file	"code.ll"
	.globl	lam                     # -- Begin function lam
	.p2align	4, 0x90
	.type	lam,@function
lam:                                    # @lam
	.cfi_startproc
# %bb.0:
                                        # kill: def $edi killed $edi def $rdi
	movl	%edi, -4(%rsp)
	leal	3(%rdi), %eax
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
	subq	$56, %rsp
	.cfi_def_cfa_offset 64
	movl	$9, 12(%rsp)
	movl	$3, 52(%rsp)
	movl	$12, 8(%rsp)
	movl	$12, %edi
	callq	gun
	addq	$56, %rsp
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
	leal	3(%rdi), %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
