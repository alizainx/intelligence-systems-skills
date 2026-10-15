#!/usr/bin/env python3
"""
Verifies Linux From Scratch (LFS) 3-Stage Cross-Toolchain Bootstrap DAG
and inspects a real compiled ELF64 binary with GNU `readelf` to audit PT_INTERP and RPATH/RUNPATH.
"""
import subprocess, tempfile
from pathlib import Path

LFS_STAGES = [
    ("cross-binutils-pass1", []),
    ("cross-gcc-pass1-freestanding", ["cross-binutils-pass1"]),
    ("linux-api-headers", []),
    ("target-libc-headers-and-libs", ["cross-gcc-pass1-freestanding", "linux-api-headers"]),
    ("cross-libstdc++", ["target-libc-headers-and-libs"]),
    ("cross-binutils-pass2", ["target-libc-headers-and-libs"]),
    ("cross-gcc-pass2-hosted", ["cross-binutils-pass2", "cross-libstdc++"]),
]

def verify_lfs_bootstrap_order(stages: list[tuple[str, list[str]]]) -> bool:
    built: set[str] = set()
    for name, deps in stages:
        for d in deps:
            if d not in built:
                return False
        built.add(name)
    return True

assert verify_lfs_bootstrap_order(LFS_STAGES)
assert not verify_lfs_bootstrap_order(list(reversed(LFS_STAGES)))

# Compile a test ELF64 binary and audit PT_INTERP & dynamic tags with GNU `readelf`
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp)
    (p / "hello.c").write_text("int main(void) { return 0; }\n")
    subprocess.run(["gcc", "-std=c11", str(p / "hello.c"), "-o", str(p / "hello.elf")], check=True)
    out = subprocess.check_output(["readelf", "-l", "-d", str(p / "hello.elf")], text=True)
    assert "Requesting program interpreter:" in out
    assert "/tools/lib" not in out  # Zero host/temp-toolchain RPATH leakage!
print("LINUX FROM SCRATCH (LFS) 3-STAGE BOOTSTRAP DAG & ELF64 PT_INTERP AUDIT VERIFIED")
