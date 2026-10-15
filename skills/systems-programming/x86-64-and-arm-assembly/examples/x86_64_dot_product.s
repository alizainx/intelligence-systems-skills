/* System V AMD64 ABI compliant x86_64 assembly routine:
 * uint64_t asm_dot_product_u64(const uint64_t *a, const uint64_t *b, size_t n)
 * rdi = a, rsi = b, rdx = n -> returns sum in rax. Preserves rbx (callee-saved).
 */
.text
.globl asm_dot_product_u64
.type asm_dot_product_u64, @function
asm_dot_product_u64:
    pushq %rbp
    movq %rsp, %rbp
    pushq %rbx              /* Preserve callee-saved %rbx */
    xorq %rax, %rax         /* acc = 0 */
    testq %rdx, %rdx
    jz .Ldone
    xorq %rcx, %rcx         /* i = 0 */
.Lloop:
    movq (%rdi,%rcx,8), %rbx
    imulq (%rsi,%rcx,8), %rbx
    addq %rbx, %rax
    incq %rcx
    cmpq %rdx, %rcx
    jb .Lloop
.Ldone:
    popq %rbx
    popq %rbp
    ret
.size asm_dot_product_u64, .-asm_dot_product_u64
.section .note.GNU-stack,"",@progbits
