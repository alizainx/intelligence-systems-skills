#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path

ASM_CODE = """
.text
.globl dot_u64_sysv
.type dot_u64_sysv, @function
dot_u64_sysv:
    xorq %rax, %rax
    testq %rdx, %rdx
    jz .Ldone
.Lloop:
    movq (%rdi), %rcx
    imulq (%rsi), %rcx
    addq %rcx, %rax
    addq $8, %rdi
    addq $8, %rsi
    decq %rdx
    jnz .Lloop
.Ldone:
    ret
.section .note.GNU-stack,"",@progbits
"""

C_CODE = """
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
extern uint64_t dot_u64_sysv(const uint64_t *a, const uint64_t *b, uint64_t n);
int main(void) {
    uint64_t a[4] = {2, 3, 4, 5};
    uint64_t b[4] = {10, 20, 30, 40};
    uint64_t res = dot_u64_sysv(a, b, 4);
    assert(res == 400ULL);
    assert(dot_u64_sysv(a, b, 0) == 0ULL);
    puts("NATIVE X86_64 ASSEMBLY ABI & EXECUTION VERIFIED");
    return 0;
}
"""

with tempfile.TemporaryDirectory() as td:
    p = Path(td)
    (p / "dot.s").write_text(ASM_CODE)
    (p / "main.c").write_text(C_CODE)
    subprocess.run(["gcc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", str(p / "dot.s"), str(p / "main.c"), "-o", str(p / "asm_test")], check=True)
    res = subprocess.run([str(p / "asm_test")], capture_output=True, text=True, check=True)
    print(res.stdout.strip())
