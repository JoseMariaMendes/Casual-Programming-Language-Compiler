	.text
	.file	"code.ll"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2                               # -- Begin function fun
.LCPI0_0:
	.long	0x40900000                      # float 4.5
	.text
	.globl	fun
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
	subq	$32, %rsp
	movss	%xmm0, -4(%rbp)
	movq	$.L.casual_str_cas_1, -16(%rbp)
	movq	$.L.casual_str_cas_1, -32(%rbp)
	movl	$1066192077, -20(%rbp)          # imm = 0x3F8CCCCD
	movl	$1079194420, -8(%rbp)           # imm = 0x40533334
	ucomiss	.LCPI0_0(%rip), %xmm0
	jne	.LBB0_1
	jnp	.LBB0_2
.LBB0_1:                                # %if_cas_7
	movss	-4(%rbp), %xmm0                 # xmm0 = mem[0],zero,zero,zero
	divss	-8(%rbp), %xmm0
	movss	%xmm0, -4(%rbp)
.LBB0_2:                                # %else_cas_8
	movq	$.L.casual_str_cas_14, -16(%rbp)
	movq	%rsp, %rax
	leaq	-16(%rax), %rsp
	movss	-4(%rbp), %xmm0                 # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -16(%rax)
	movq	%rsp, %rax
	leaq	-16(%rax), %rsp
	movb	$1, -16(%rax)
	movss	-4(%rbp), %xmm0                 # xmm0 = mem[0],zero,zero,zero
	movq	%rbp, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	fun, .Lfunc_end0-fun
	.cfi_endproc
                                        # -- End function
	.globl	dun                             # -- Begin function dun
	.p2align	4, 0x90
	.type	dun,@function
dun:                                    # @dun
	.cfi_startproc
# %bb.0:
	movl	$9, %eax
	retq
.Lfunc_end1:
	.size	dun, .Lfunc_end1-dun
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2                               # -- Begin function main
.LCPI2_0:
	.long	0x40666666                      # float 3.5999999
.LCPI2_1:
	.long	0x40b33333                      # float 5.5999999
.LCPI2_2:
	.long	0xc0b66666                      # float -5.69999981
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	subq	$440, %rsp                      # imm = 0x1B8
	.cfi_def_cfa_offset 448
	movq	$.L.casual_str_cas_17, 24(%rsp)
	movl	$1083388723, 20(%rsp)           # imm = 0x40933333
	movl	$5, 16(%rsp)
	movss	.LCPI2_0(%rip), %xmm0           # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI2_1(%rip), %xmm1           # xmm1 = mem[0],zero,zero,zero
	callq	fun
	addss	.LCPI2_2(%rip), %xmm0
	movss	%xmm0, 12(%rsp)
	movl	$3, 32(%rsp)
	movl	64(%rsp), %eax
	addq	$440, %rsp                      # imm = 0x1B8
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end2:
	.size	main, .Lfunc_end2-main
	.cfi_endproc
                                        # -- End function
	.type	.L.casual_str_cas_17,@object    # @.casual_str_cas_17
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.casual_str_cas_17:
	.asciz	"maria\n"
	.size	.L.casual_str_cas_17, 7

	.type	.L.casual_str_cas_14,@object    # @.casual_str_cas_14
.L.casual_str_cas_14:
	.asciz	"fgsdfg"
	.size	.L.casual_str_cas_14, 7

	.type	.L.casual_str_cas_1,@object     # @.casual_str_cas_1
.L.casual_str_cas_1:
	.asciz	"dfkas"
	.size	.L.casual_str_cas_1, 6

	.section	".note.GNU-stack","",@progbits
