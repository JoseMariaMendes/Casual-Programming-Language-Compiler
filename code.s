	.text
	.file	"code.ll"
	.globl	fun                     # -- Begin function fun
	.p2align	4, 0x90
	.type	fun,@function
fun:                                    # @fun
	.cfi_startproc
# %bb.0:
	subq	$120, %rsp
	.cfi_def_cfa_offset 128
	movq	%rdi, -104(%rsp)
	movl	$2, -116(%rsp)
	movl	$1079194419, -120(%rsp) # imm = 0x40533333
	movq	$.L.casual_str_cas_1, -112(%rsp)
	movb	-88(%rsp), %al
	andb	$1, %al
	movb	%al, -121(%rsp)
	movb	$1, %al
	addq	$120, %rsp
	.cfi_def_cfa_offset 8
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
	.type	.L.casual_str_cas_1,@object # @.casual_str_cas_1
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.casual_str_cas_1:
	.asciz	"asdasd"
	.size	.L.casual_str_cas_1, 7

	.section	".note.GNU-stack","",@progbits
