	.text
	.file	"code.ll"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	subq	$56, %rsp
	.cfi_def_cfa_offset 64
	movl	$9, 12(%rsp)
	movl	$0, 36(%rsp)
	movl	52(%rsp), %eax
	addl	$9, %eax
	movl	%eax, 8(%rsp)
	movl	$5, %edi
	callq	gun
	addq	$56, %rsp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.globl	gun                     # -- Begin function gun
	.p2align	4, 0x90
	.type	gun,@function
gun:                                    # @gun
	.cfi_startproc
# %bb.0:
	movl	%edi, -4(%rsp)
	movl	$6, -8(%rsp)
	addl	$5, %edi
	movl	%edi, -12(%rsp)
	movl	$4, %eax
	retq
.Lfunc_end1:
	.size	gun, .Lfunc_end1-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
