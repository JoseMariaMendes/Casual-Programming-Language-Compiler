	.text
	.file	"code.ll"
	.globl	fun                             # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	movq	%rdi, -48(%rsp)
	movl	$9, -52(%rsp)
	movl	$7, -40(%rsp)
	movl	$6, %eax
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
