# Verified Example: `self-hosting-and-compiler-bootstrapping` (`ddc_bootstrap_verifier.py`)

```
#!/usr/bin/env python3
"""
Verifies Self-Hosting Compiler Stage-0 -> Stage-1 -> Stage-2 -> Stage-3 Fixed-Point Bootstrap
and David A. Wheeler's Diverse Double-Compiling (DDC) defense against Thompson Trusting-Trust backdoors.
"""
import hashlib

def compile_with(compiler_id: str, compiler_is_trojaned: bool, source_code: str) -> tuple[str, bool]:
    """
    Simulates compiling `source_code`:
    - If `compiler_is_trojaned` is True, the trojaned binary injects a self-reproducing backdoor
      when compiling the compiler's own source!
    """
    effective_tag = f"compiled({source_code})"
    out_trojaned = False
    if compiler_is_trojaned and "COMPILER_SRC" in source_code:
        effective_tag += "+THOMPSON_BACKDOOR"
        out_trojaned = True
    digest = hashlib.sha256(effective_tag.encode()).hexdigest()
    return (digest, out_trojaned)

# 1. Clean Stage-0 -> Stage-1 -> Stage-2 -> Stage-3 fixed-point check: bin(Stage2) == bin(Stage3)
s1_hash, s1_t = compile_with("stage0_seed", False, "COMPILER_SRC_V1")
s2_hash, s2_t = compile_with(s1_hash, s1_t, "COMPILER_SRC_V1")
s3_hash, s3_t = compile_with(s2_hash, s2_t, "COMPILER_SRC_V1")
assert s2_hash == s3_hash and not s2_t

# 2. Thompson Trusting-Trust attack: a trojaned Stage-0 produces Stage-2 == Stage-3 (both trojaned!),
#    so standard Stage-2 == Stage-3 check ALONE cannot detect a Thompson backdoor!
#    Diverse Double-Compiling (DDC) compiles COMPILER_SRC using an independent trusted compiler `c_trusted`
#    and verifies that `compile(compile(COMPILER_SRC, c_trusted), COMPILER_SRC)` matches `s2_hash`!
t1_hash, t1_tr = compile_with("trojan_stage0", True, "COMPILER_SRC_V1")
t2_hash, t2_tr = compile_with(t1_hash, t1_tr, "COMPILER_SRC_V1")
# DDC check against independent clean compiler `gcc_independent`:
ddc1_hash, ddc1_tr = compile_with("gcc_independent", False, "COMPILER_SRC_V1")
ddc2_hash, _ = compile_with(ddc1_hash, ddc1_tr, "COMPILER_SRC_V1")
assert t2_hash != ddc2_hash, "DDC check must detect mismatch caused by Thompson backdoor in Stage-0!"
print("SELF-HOSTING COMPILER STAGE-2/3 FIXED POINT & DIVERSE DOUBLE-COMPILING (DDC) TRUST CHECK VERIFIED")

```
