	.text
	.file	"code.ll"
	.globl	fun                             # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	movq	%rdi, -48(%rsp)
	movb	-32(%rsp), %al
	andb	$1, %al
	movb	%al, -49(%rsp)
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
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$9, 4(%rsp)
	movl	$9, %edi
	callq	gun
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.globl	gun                             # -- Begin function gun
	.p2align	4, 0x90
	.type	gun,@function
gun:                                    # @gun
	.cfi_startproc
# %bb.0:
	movl	$3, -4(%rsp)
	movl	$2, -8(%rsp)
	movb	$1, %al
	testb	%al, %al
	jne	.LBB2_2
# %bb.1:                                # %if_cas_12
	xorl	%eax, %eax
	retq
.LBB2_2:                                # %else_cas_13
	movl	$1, %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
