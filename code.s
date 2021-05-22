	.text
	.file	"code.ll"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function lam
.LCPI0_0:
	.long	1091882189              # float 9.30000019
	.text
	.globl	lam
	.p2align	4, 0x90
	.type	lam,@function
lam:                                    # @lam
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movl	$1091882189, -12(%rsp)  # imm = 0x4114CCCD
	movss	4(%rdi), %xmm0          # xmm0 = mem[0],zero,zero,zero
	addss	.LCPI0_0(%rip), %xmm0
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
	movl	$1091882189, 12(%rsp)   # imm = 0x4114CCCD
	movq	$3, 32(%rsp)
	xorl	%edi, %edi
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
	leal	6(%rdi), %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
