	.text
	.file	"code.ll"
	.globl	fun                     # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	movl	%edi, -4(%rsp)
	movl	%esi, -16(%rsp)
	movl	%edx, -8(%rsp)
	movl	%ecx, -12(%rsp)
	cmpl	%esi, %edi
	jge	.LBB0_2
# %bb.1:                                # %if_cas_1
	xorl	%eax, %eax
	retq
.LBB0_2:                                # %else_cas_2
	movl	-16(%rsp), %eax
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
	xorl	%eax, %eax
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
