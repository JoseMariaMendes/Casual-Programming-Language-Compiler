	.text
	.file	"code.ll"
	.globl	fun                             # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	subq	$120, %rsp
	.cfi_def_cfa_offset 128
	movq	%rdi, -104(%rsp)
	movl	$2, -108(%rsp)
	movl	$1079194419, -112(%rsp)         # imm = 0x40533333
	movb	-88(%rsp), %al
	andb	$1, %al
	movb	%al, -113(%rsp)
	movb	$1, %al
	addq	$120, %rsp
	.cfi_def_cfa_offset 8
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
	movl	%edi, -4(%rsp)
	movl	$4, %eax
	retq
.Lfunc_end2:
	.size	gun, .Lfunc_end2-gun
	.cfi_endproc
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
