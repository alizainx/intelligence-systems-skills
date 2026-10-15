#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

__asm__(
    ".text\n"
    ".globl fnv1a64_x86_64\n"
    ".type fnv1a64_x86_64, @function\n"
    "fnv1a64_x86_64:\n"
    "    movabsq $0xcbf29ce484222325, %rax\n"
    "    movabsq $0x100000001b3, %r8\n"
    "    testq %rsi, %rsi\n"
    "    jz .Ldone\n"
    ".Lloop:\n"
    "    movzbq (%rdi), %rcx\n"
    "    xorq %rcx, %rax\n"
    "    imulq %r8, %rax\n"
    "    incq %rdi\n"
    "    decq %rsi\n"
    "    jnz .Lloop\n"
    ".Ldone:\n"
    "    ret\n"
    ".section .note.GNU-stack,\"\",@progbits\n"
);

extern uint64_t fnv1a64_x86_64(const uint8_t *data, size_t len);

int main(void) {
    const uint8_t msg[] = "hello";
    uint64_t h = fnv1a64_x86_64(msg, 5U);
    assert(h == 0xa430d84680aabd0bULL);
    assert(fnv1a64_x86_64(msg, 0U) == 0xcbf29ce484222325ULL);
    puts("VERIFIED: Native x86_64 System V ABI Assembly FNV-1a-64 executed & verified");
    return 0;
}
